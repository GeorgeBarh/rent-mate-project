from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
from products.models import Product
from django.contrib import messages

@login_required
def book_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']

            # Check for overlap
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
                messages.success(request, 'Your booking has been confirmed!')
                return redirect('product_detail', pk=product.pk)
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
