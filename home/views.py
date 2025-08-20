from django.shortcuts import render, redirect
from products.models import Product
from datetime import datetime
from django.contrib import messages
from .forms import NewsletterSignupForm
from .models import NewsletterSignup


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
            email = form.cleaned_data['email']
            if not NewsletterSignup.objects.filter(email=email).exists():
                form.save()
                messages.success(request, "Thanks for signing up!")
            else:
                messages.info(request, "You're already subscribed.")
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, error)
    return redirect(request.META.get('HTTP_REFERER', 'home'))