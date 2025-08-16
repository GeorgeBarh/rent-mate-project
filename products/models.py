from django.db import models

CATEGORY_CHOICES = [
    ('vehicle', 'Vehicle'),
    ('equipment', 'Equipment'),
]

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name
