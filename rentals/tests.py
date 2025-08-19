from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date, timedelta
from products.models import Product
from rentals.models import Booking


class BookingTests(TestCase):
    def setUp(self):
        # Create test user and client
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.client.login(username='testuser', password='testpass123')

        # Create a test product
        self.product = Product.objects.create(
            name='Test Product',
            description='A test product for rental.',
            category='equipment',
            price_per_day=25.00
        )

    #  Model Tests
    def test_booking_model_str_returns_expected_format(self):
        booking = Booking.objects.create(
            user=self.user,
            product=self.product,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=2),
            paid=False
        )
        expected = f"{self.product.name} booked by {self.user.username} from {booking.start_date} to {booking.end_date}"
        self.assertEqual(str(booking), expected)

    #  View: Booking Form Access
    def test_user_can_access_booking_form_authenticated(self):
        url = reverse('book_product', args=[self.product.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    #  View: Create Booking - Prevent Overlapping
    def test_booking_form_rejects_overlapping_dates(self):
        Booking.objects.create(
            user=self.user,
            product=self.product,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=2),
            paid=False
        )
        response = self.client.post(reverse('book_product', args=[self.product.id]), {
            'start_date': date.today() + timedelta(days=1),
            'end_date': date.today() + timedelta(days=3)
        }, follow=True)
        self.assertContains(response, "Selected dates are unavailable.")

    #  View: My Bookings Page
    def test_my_bookings_view_shows_user_bookings(self):
        Booking.objects.create(
            user=self.user,
            product=self.product,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=2),
            paid=False
        )
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    #  View: Cancel Booking (Unpaid)
    def test_user_can_cancel_unpaid_booking(self):
        booking = Booking.objects.create(
            user=self.user,
            product=self.product,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=2),
            paid=False
        )
        url = reverse('cancel_booking', args=[booking.id])
        response = self.client.get(url, follow=True)
        self.assertContains(response, "Booking cancelled.")
        self.assertFalse(Booking.objects.filter(id=booking.id).exists())

    #  View: Cancel Booking (Paid)
    def test_user_cannot_cancel_paid_booking(self):
        booking = Booking.objects.create(
            user=self.user,
            product=self.product,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=2),
            paid=True
        )
        url = reverse('cancel_booking', args=[booking.id])
        response = self.client.get(url, follow=True)
        self.assertContains(response, "You cannot cancel a paid booking.")

    #  Access Control: Anonymous User Blocked
    def test_anonymous_user_redirected_from_booking(self):
        self.client.logout()
        response = self.client.get(reverse('book_product', args=[self.product.id]))
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.url.startswith('/accounts/login'))

    #  Access Control: User Cannot Cancel Another’s Booking
    def test_user_cannot_cancel_other_users_booking(self):
        other_user = User.objects.create_user(username='hacker', password='hackpass')
        booking = Booking.objects.create(
            user=other_user,
            product=self.product,
            start_date=date.today(),
            end_date=date.today() + timedelta(days=2),
            paid=False
        )
        url = reverse('cancel_booking', args=[booking.id])
        response = self.client.get(url, follow=True)
        self.assertEqual(response.status_code, 404)
