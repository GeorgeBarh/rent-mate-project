from django.db import models
from cloudinary.models import CloudinaryField  # Import this

CATEGORY_CHOICES = [
    ('vehicle', 'Vehicle'),
    ('equipment', 'Equipment'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2, default=10.00)
    image = CloudinaryField('image', blank=True, null=True)  # Use Cloudinary image field
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
