from django.forms import ValidationError
from django.test import TestCase
from django.db import IntegrityError
from .models import Product_Category, Product

# Create your tests here.


class TestModels(TestCase):

    def test_all_blank_product_category(self):
        """Test that when a category is created with no
        info, we get a ValidationError"""
        product_category = Product_Category.objects.create()
        with self.assertRaises(ValidationError):
            product_category.full_clean()

    def test_friendly_name_blank_product_category(self):
        """Test that when a category is created, friendly name is blank"""
        product_category = Product_Category.objects.create(
            name='test_category')
        self.assertFalse(product_category.friendly_name)

    def test_max_length_name_product_category(self):
        """Test that when a category is created with a name longer than
        254 characters, we get a ValidationError"""
        long_name = "x" * 255
        product_category = Product_Category.objects.create(name=long_name)
        with self.assertRaises(ValidationError):
            product_category.full_clean()

    def test_blank_name_product(self):
        """Test that when a product is created with no name,
        we get a ValidationError"""
        product = Product.objects.create(
            description='test description', price=1.99)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_blank_description_product(self):
        """Test that when a product is created with no description,
        we get a ValidationError"""
        product = Product.objects.create(name='test_product', price=1.99)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_blank_price_product(self):
        """Test that when a product is created with no price,
        we get a ValidationError"""
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(
                name='test_product', description='test description')
            product.full_clean()

    def test_blank_fields_product(self):
        """Test that when a product is created, category, sku,
        rating, image_url and image are blank"""
        product = Product.objects.create(
            name='test_product', description='test description', price=1.99)
        self.assertFalse(product.category)
        self.assertFalse(product.sku)
        self.assertFalse(product.rating)
        self.assertFalse(product.image_url)
        self.assertFalse(product.image)

    def test_max_length_name_product(self):
        """Test that when a product is created with a name
        longer than 254 characters, we get a ValidationError"""
        long_name = "x" * 255
        product = Product.objects.create(
            name=long_name, description='test description', price=1.99)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_max_length_sku_product(self):
        """Test that when a product is created with a sku
        longer than 254 characters, we get a ValidationError"""
        long_name = "x" * 255
        product = Product.objects.create(
            name='test_product', description='test description', price=1.99, sku=long_name)
        with self.assertRaises(ValidationError):
            product.full_clean()

    def test_max_length_image_url_product(self):
        """Test that when a product is created with an image_url
        longer than 1024 characters, we get a ValidationError"""
        long_url = "x" * 1025
        product = Product.objects.create(
            name='test_product', description='test description', price=1.99, image_url=long_url)
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
            category=self.category_clearance)

    def test_delete_category_of_product(self):
        """Test that when a category is deleted for a product,
        the category field on the product is emptied"""
        self.category_clearance.delete()
        with self.assertRaises(Product_Category.DoesNotExist):
            Product_Category.objects.get(name="clearance")
        product = Product.objects.get(name="Test Clearance")
        self.assertIsNone(product.category)

    def test_get_products(self):
        """ Test that when browsing to /products/ we get a 200 code,
        products/products.html template, context and that we have 1 product """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertIn(b'Products', response.content)
        self.assertEqual(1, response.context['products'].count())

    def test_select_categories(self):
        """ Test that when selecting categories we get a 200 code,
        products/products.html template and context """
        response = self.client.get('/products/?category=weights')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("weights", response.context['selected_categories'])
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get('/products/?category=clothes')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("clothes", response.context['selected_categories'])
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get('/products/?category=shoes')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("shoes", response.context['selected_categories'])
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get('/products/?category=accessories')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("accessories", response.context['selected_categories'])
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get(
            '/products/?category=weights,clothes,shoes,accessories')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("weights,clothes,shoes,accessories",
                        response.context['selected_categories'])
        self.assertEqual(4, response.context['products'].count())

        response = self.client.get('/products/?category=protein_powders')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("protein_powders",
                        response.context['selected_categories'])
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get('/products/?category=protein_bars')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue(
            "protein_bars", response.context['selected_categories'])
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get('/products/?category=sports_drinks')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("sports_drinks",
                        response.context['selected_categories'])
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get('/products/?category=vitamins')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("vitamins", response.context['selected_categories'])
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get(
            '/products/?category=protein_powders,protein_bars,sports_drinks,vitamins')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("protein_powders,protein_bars,sports_drinks,vitamins",
                        response.context['selected_categories'])
        self.assertEqual(4, response.context['products'].count())

        response = self.client.get('/products/?category=new_arrivals')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue(
            "new_arrivals", response.context['selected_categories'])
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get('/products/?category=deals')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("deals", response.context['selected_categories'])
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get('/products/?category=clearance')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("clearance", response.context['selected_categories'])
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get(
            '/products/?category=new_arrivals,deals,clearance')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("new_arrivals,deals,clearance",
                        response.context['selected_categories'])
        self.assertEqual(3, response.context['products'].count())

    def test_search_products(self):
        """ Test that when searching for 'ideal' we get a 200 code,
        products/products.html template, context and that we find 1 product """
        response = self.client.get('/products/?q=ideal')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("ideal", response.context['search_term'])
        self.assertEqual(1, response.context['products'].count())

    def test_get_product_details(self):
        """ Test that when browsing to /products/1 we get a 200 code,
        products/product_detail.html template, context and that name and description are true """
        product_id = 1
        response = self.client.get('/products/' + str(product_id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertTrue(response.context)
        self.assertEqual('Test Product', response.context['product'].name)
        self.assertEqual('Ideal', response.context['product'].description)
