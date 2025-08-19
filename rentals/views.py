from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
from products.models import Product
from django.contrib import messages
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def book_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    booking = None

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            conflicting = Booking.objects.filter(
                product=product,
                start_date__lte=end_date,
                end_date__gte=start_date
            ).exists()

            if conflicting:
                messages.error(request, 'This product is already booked for the selected dates.')
            else:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.product = product
                booking.save()
                messages.success(request, 'Booking created! Please proceed to payment.')
                return render(request, 'rentals/book_product.html', {
                    'form': form,
                    'product': product,
                    'booking': booking
                })
    else:
        form = BookingForm()

    return render(request, 'rentals/book_product.html', {
        'form': form,
        'product': product
    })


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-start_date')
    return render(request, 'rentals/my_bookings.html', {'bookings': bookings})


@login_required
def create_checkout_session(request, booking_id):
    booking = get_object_or_404(Booking, pk=booking_id, user=request.user)

    domain_url = 'http://127.0.0.1:8000/'  # Replace with live domain on deployment

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            mode='payment',
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'unit_amount': int(booking.total_price() * 100),  # Stripe needs cents
                    'product_data': {
                        'name': f'Rental: {booking.product.name}',
                    },
                },
                'quantity': 1,
            }],
            metadata={'booking_id': booking.id},
            success_url=domain_url + 'rentals/payment-success/',
            cancel_url=domain_url + 'rentals/payment-cancel/',
        )
        return redirect(checkout_session.url)
    except Exception as e:
        return JsonResponse({'error': str(e)})


def payment_success(request):
    return render(request, 'rentals/payment_success.html')


def payment_cancel(request):
    return render(request, 'rentals/payment_cancel.html')


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    endpoint_secret = settings.STRIPE_WEBHOOK_SECRET
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, endpoint_secret
        )
    except ValueError as e:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError as e:
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        booking_id = session['metadata'].get('booking_id')

        if booking_id:
            try:
                booking = Booking.objects.get(id=booking_id)
                booking.paid = True
                booking.save()
            except Booking.DoesNotExist:
                pass

    return HttpResponse(status=200)
