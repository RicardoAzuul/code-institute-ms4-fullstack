from django.forms import ValidationError
from django.test import TestCase
from django.db import IntegrityError
from .models import Product_Category, Product, ShopAlert


class TestModels(TestCase):
    def test_blank_shopalert(self):
        """
        When a shopalert is created with no
        info, we get a ValidationError
        """
        test_shopalert = ShopAlert.objects.create()
        with self.assertRaises(ValidationError):
            test_shopalert.full_clean()

    def test_max_length_name_shopalert(self):
        """
        When a shopalert is created with a name longer than
        254 characters, we get a ValidationError
        """
        long_name = "x" * 255
        test_shopalert = ShopAlert.objects.create(name=long_name)
        with self.assertRaises(ValidationError):
            test_shopalert.full_clean()

    def test_all_blank_product_category(self):
        """
        When a category is created with no
        info, we get a ValidationError
        """
        product_category = Product_Category.objects.create()
        with self.assertRaises(ValidationError):
            product_category.full_clean()

    def test_friendly_name_blank_product_category(self):
        """
        When a category is created, friendly name is blank
        """
        product_category = Product_Category.objects.create(
            name="test_category")
        self.assertFalse(product_category.friendly_name)

    def test_max_length_name_product_category(self):
        """
        When a category is created with a name longer than
        254 characters, we get a ValidationError
        """
        long_name = "x" * 255
        product_category = Product_Category.objects.create(name=long_name)
        with self.assertRaises(ValidationError):
            product_category.full_clean()

    def test_blank_name_product(self):
        """
        When a product is created with no name,
        we get a ValidationError
        """
        product = Product.objects.create(
            description="test description", price=1.99)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_blank_description_product(self):
        """
        When a product is created with no description,
        we get a ValidationError
        """
        product = Product.objects.create(name="test_product", price=1.99)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_blank_price_product(self):
        """
        When a product is created with no price,
        we get a ValidationError
        """
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                name="test_product", description="test description"
            )
            product.full_clean()

    def test_blank_fields_product(self):
        """
        When a product is created, category, sku,
        rating, image_url and image are blank
        """
        product = Product.objects.create(
            name="test_product", description="test description", price=1.99
        )
        self.assertFalse(product.category)
        self.assertFalse(product.sku)
        self.assertFalse(product.rating)
        self.assertFalse(product.image_url)
        self.assertFalse(product.image)

    def test_max_length_name_product(self):
        """
        When a product is created with a name
        longer than 254 characters, we get a ValidationError
        """
        long_name = "x" * 255
        product = Product.objects.create(
            name=long_name, description="test description", price=1.99
        )
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_max_length_sku_product(self):
        """
        When a product is created with a sku
        longer than 254 characters, we get a ValidationError
        """
        long_name = "x" * 255
        product = Product.objects.create(
            name="test_product",
            description="test description",
            price=1.99,
            sku=long_name,
        )
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_max_length_image_url_product(self):
        """
        When a product is created with an image_url
        longer than 1024 characters, we get a ValidationError
        """
        long_url = "x" * 1025
        product = Product.objects.create(
            name="test_product",
            description="test description",
            price=1.99,
            image_url=long_url,
        )
        with self.assertRaises(ValidationError):
            product.full_clean()


class TestViews(TestCase):
    def setUp(self):
        self.category_clearance = Product_Category.objects.create(
            name="clearance")

        self.product_clearance = Product.objects.create(
            name="Test Clearance",
            description="Clearance",
            price=1.99,
            category=self.category_clearance,
        )

    def test_delete_category_of_product(self):
        """
        When a category is deleted for a product,
        the category field on the product is emptied
        """
        self.category_clearance.delete()
        with self.assertRaises(Product_Category.DoesNotExist):
            Product_Category.objects.get(name="clearance")
        product = Product.objects.get(name="Test Clearance")
        self.assertIsNone(product.category)
