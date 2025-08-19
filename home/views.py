from django.shortcuts import render
from products.models import Product
from datetime import datetime

def home(request):
    products = Product.objects.all()[:3]  # Featured items
    return render(request, 'home/index.html', {
        'products': products,
        'year': datetime.now().year,
    })
