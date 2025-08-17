from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking
from products.models import Product
from django.contrib.auth.decorators import login_required

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
