from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking
from .forms import BookingForm
from products.models import Product
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse, HttpResponse
from django.conf import settings
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY


@login_required
def book_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    # Get all existing bookings for this product
    bookings = Booking.objects.filter(product=product)

    # Create list of unavailable date ranges
    booked_dates = [
        {"start": booking.start_date, "end": booking.end_date}
        for booking in bookings
    ]

    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start_date']
            end = form.cleaned_data['end_date']

            # Check for overlap
            overlap = bookings.filter(
                start_date__lte=end,
                end_date__gte=start
            ).exists()

            if overlap:
                messages.error(request, "Selected dates are unavailable.")
            else:
                booking = form.save(commit=False)
                booking.user = request.user
                booking.product = product
                booking.save()

                return redirect('create_checkout_session', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'rentals/book_product.html', {
        'form': form,
        'product': product,
        'booked_dates': booked_dates,
    })


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-start_date')
    return render(request, 'rentals/my_bookings.html', {'bookings': bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)

    if booking.paid:
        messages.error(request, "You cannot cancel a paid booking.")
    else:
        booking.delete()
        messages.success(request, "Booking cancelled.")

    return redirect('my_bookings')


@login_required
def create_checkout_session(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    domain = request.build_absolute_uri('/')

    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': booking.product.name,
                    },
                    'unit_amount': int(booking.product.price * 100),
                },
                'quantity': 1,
            }],
            mode='payment',
            success_url=domain + 'rentals/payment-success/',
            cancel_url=domain + 'rentals/payment-cancel/',
            metadata={
                'booking_id': booking.id
            }
        )
        return redirect(checkout_session.url)
    except Exception as e:
        messages.error(request, "An error occurred while starting checkout.")
        return redirect('my_bookings')


def payment_success(request):
    return render(request, 'rentals/payment_success.html')


def payment_cancel(request):
    return render(request, 'rentals/payment_cancel.html')


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    sig_header = request.META.get('HTTP_STRIPE_SIGNATURE')
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except (ValueError, stripe.error.SignatureVerificationError):
        return HttpResponse(status=400)

    # Handle the checkout.session.completed event
    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']
        booking_id = session.get('metadata', {}).get('booking_id')

        if booking_id:
            try:
                booking = Booking.objects.get(id=booking_id)
                booking.paid = True
                booking.save()
            except Booking.DoesNotExist:
                pass

    return HttpResponse(status=200)
