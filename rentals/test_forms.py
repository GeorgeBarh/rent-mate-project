from django.test import TestCase
from rentals.forms import BookingForm
from products.models import Product
from django.contrib.auth.models import User
from datetime import date, timedelta

class BookingFormTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='formuser', password='formpass')
        self.product = Product.objects.create(
            name='Test Generator',
            description='Backup power generator.',
            category='equipment',
            price_per_day=50.00
        )

    def test_valid_booking_form(self):
        form_data = {
            'product': self.product.id,
            'start_date': date.today() + timedelta(days=1),
            'end_date': date.today() + timedelta(days=3),
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_date_range(self):
        form_data = {
    'product': self.product.id,
    'start_date': date.today() + timedelta(days=5),
    'end_date': date.today() + timedelta(days=2),
}
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())

