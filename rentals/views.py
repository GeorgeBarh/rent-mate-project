from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import BookingForm
from .models import Booking
from products.models import Product

@login_required
def book_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.product = product
            booking.save()
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
