from django.test import TestCase
from home.forms import NewsletterSignupForm

class NewsletterFormTests(TestCase):

    def test_valid_email(self):
        form = NewsletterSignupForm(data={'email': 'user@example.com'})
        self.assertTrue(form.is_valid())

    def test_invalid_email_format(self):
        form = NewsletterSignupForm(data={'email': 'invalid-email'})
        self.assertFalse(form.is_valid())
