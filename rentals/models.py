from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    paid = models.BooleanField(default=False)  

    def __str__(self):
        return f"{self.product.name} booked by {self.user.username} from {self.start_date} to {self.end_date}"

    def total_days(self):
        return (self.end_date - self.start_date).days + 1

    def total_price(self):
        if self.start_date and self.end_date and self.product:
            duration = (self.end_date - self.start_date).days
            if duration > 0:
                return int(self.product.price_per_day * duration)
        return 0
