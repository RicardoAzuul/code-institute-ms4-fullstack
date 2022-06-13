from decimal import InvalidOperation
from unicodedata import category
from django.forms import ValidationError
from django.test import TestCase
from psycopg2 import IntegrityError
from .models import Product_Category, Product

# Create your tests here.
class TestModels(TestCase):

    def test_all_blank_product_category(self):
        """Test that when a category is created with no info, we get a ValidationError"""
        product_category = Product_Category.objects.create()
        with self.assertRaises(ValidationError):
            product_category.full_clean()

    def test_friendly_name_blank_product_category(self):
        """Test that when a category is created, friendly name is blank"""
        product_category = Product_Category.objects.create(name='test_category')
        self.assertFalse(product_category.friendly_name)

    def test_max_length_name_product_category(self):
        """Test that when a category is created with a name longer than 254 characters, we get a ValidationError"""
        long_name = "x" * 255
        product_category = Product_Category.objects.create(name=long_name)
        with self.assertRaises(ValidationError):
            product_category.full_clean()
    
    def test_all_blank_product(self):
        """Test that when a product is created with no info, we get a ValidationError"""
        # TODO: Write test


    def test_blank_name_product(self):
        """Test that when a product is created with no name, we get a ValidationError"""
        product = Product.objects.create(description='test description', price=1.99)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_blank_description_product(self):
        """Test that when a product is created with no description, we get a ValidationError"""
        product = Product.objects.create(name='test_product', price=1.99)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_blank_price_product(self):
        """Test that when a product is created with no price, we get a ValidationError"""
        # TODO: Write test

    def test_blank_fields_product(self):
        """Test that when a product is created, category, sku, rating, image_url and image are blank"""
        product = Product.objects.create(name='test_product', description='test description', price=1.99)
        self.assertFalse(product.category)
        self.assertFalse(product.sku)
        self.assertFalse(product.rating)
        self.assertFalse(product.image_url)
        self.assertFalse(product.image)

    def test_max_length_name_product(self):
        """Test that when a product is created with a name longer than 254 characters, we get a ValidationError"""
        long_name = "x" * 255
        product = Product.objects.create(name=long_name, description='test description', price=1.99)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_max_length_sku_product(self):
        """Test that when a product is created with a sku longer than 254 characters, we get a ValidationError"""
        long_name = "x" * 255
        product = Product.objects.create(name='test_product', description='test description', price=1.99, sku=long_name)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_max_length_price_product(self):
        """Test that when a product is created with a price longer than 6 characters, we get a ValidationError"""
        # TODO: Write test: this generates decimal.InvalidOperation



    def test_max_length_rating_product(self):
        """Test that when a product is created with a rating longer than 6 characters, we get a ValidationError"""
        # TODO: Write test: this generates decimal.InvalidOperation

    
    def test_max_length_image_url_product(self):
        """Test that when a product is created with an image_url longer than 1024 characters, we get a ValidationError"""
        long_url = "x" * 1025
        product = Product.objects.create(name='test_product', description='test description', price=1.99, image_url=long_url)
        with self.assertRaises(ValidationError):
            product.full_clean()


    def test_delete_category_of_product(self):
        """Test that when a category is deleted for a product, the category field on the product is emptied"""
        # TODO: Write test
        category_name = 'test_category'
        product_category = Product_Category.objects.create(name=category_name)
        product_category.full_clean()
        product = Product.objects.create(name='test_product', description='test description', price=1.99, category=category_name)
        self.assertTrue(product.category)
        Product_Category.objects.delete(name=category_name)
        self.assertFalse(product.category)


class TestViews(TestCase):

    def test_get_products(self):
        """ Test that when browsing to /products/ we get a 200 code, products/products.html template and context """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertIn(b'Products', response.content)






