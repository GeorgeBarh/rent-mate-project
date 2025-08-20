from django.shortcuts import render, redirect
from products.models import Product
from datetime import datetime
from django.contrib import messages
from .forms import NewsletterSignupForm


def custom_404(request, exception):
    return render(request, '404.html', status=404)

def home(request):
    products = Product.objects.all()[:3]  # Featured items
    return render(request, 'home/index.html', {
        'products': products,
        'year': datetime.now().year,
    })


def newsletter_signup(request):
    if request.method == 'POST':
        form = NewsletterSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thanks for signing up!")
            return redirect('home')
        else:
            messages.error(request, "Please enter a valid email.")
    else:
        form = NewsletterSignupForm()

    return render(request, 'home/index.html', {'form': form})
