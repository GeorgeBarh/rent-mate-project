from django.test import TestCase
from products.models import Product


class ProductModelTests(TestCase):

    def setUp(self):
        self.product = Product.objects.create(
            name="Test Product",
            description="Test description",
            category="equipment",
            price_per_day=25.00
        )

    def test_product_model_str(self):
        self.assertEqual(str(self.product), "Test Product")