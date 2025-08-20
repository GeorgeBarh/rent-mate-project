from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from products.models import Product

class StaticViewSitemap(Sitemap):
    def items(self):
        return ['home', 'product_list']

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    def items(self):
        return Product.objects.all()
