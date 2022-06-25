from decimal import InvalidOperation
from unicodedata import category
from django.forms import ValidationError
from django.test import TestCase
from django.db import IntegrityError
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
        with self.assertRaises(IntegrityError):
            product = Product.objects.create(name='test_product', description='test description')
            product.full_clean()

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





class TestViews(TestCase):

    def setUp(self):
        # TODO: Figure out how to create categories for use with test data
        # self.category = Product_Category.objects.create(name="weights")
        # self.category = Product_Category.objects.create(name="clothes")
        # self.category = Product_Category.objects.create(name="shoes")
        # self.category = Product_Category.objects.create(name="accessories")
        # self.category = Product_Category.objects.create(name="protein_powders")
        # self.category = Product_Category.objects.create(name="protein_bars")
        # self.category = Product_Category.objects.create(name="sports_drinks")
        # self.category = Product_Category.objects.create(name="vitamins")
        # self.category = Product_Category.objects.create(name="new_arrivals")
        # self.category = Product_Category.objects.create(name="deals")
        self.category_clearance = Product_Category.objects.create(name="clearance")

        # self.product = Product.objects.create(
        #     name="Test Product",
        #     description="Ideal",
        #     price=1.99,
        #     image="No_Image_Available.jpg")

        # self.product = Product.objects.create(
        #     name="Test Weight",
        #     description="Weight",
        #     price=1.99,
        #     category="weights")

        # self.product = Product.objects.create(
        #     name="Test Clothes",
        #     description="Clothes",
        #     price=1.99,
        #     category="clothes")

        # self.product = Product.objects.create(
        #     name="Test Shoes",
        #     description="Shoes",
        #     price=1.99,
        #     category="shoes")

        # self.product = Product.objects.create(
        #     name="Test Accessories",
        #     description="Accessories",
        #     price=1.99,
        #     category="accessories")

        # self.product = Product.objects.create(
        #     name="Test Protein Powders",
        #     description="Protein Powders",
        #     price=1.99,
        #     category="protein_powders")
            
        # self.product = Product.objects.create(
        #     name="Test Protein Bars",
        #     description="Protein Bars",
        #     price=1.99,
        #     category="protein_bars")
                        
        # self.product = Product.objects.create(
        #     name="Test Sports Drinks",
        #     description="Sports Drinks",
        #     price=1.99,
        #     category="sports_drinks")
                                    
        # self.product = Product.objects.create(
        #     name="Test Vitamins",
        #     description="Vitamins",
        #     price=1.99,
        #     category="vitamins")
                                                
        # self.product = Product.objects.create(
        #     name="Test New Arrivals",
        #     description="New Arrivals",
        #     price=1.99,
        #     category="new_arrivals")
                                                            
        # self.product = Product.objects.create(
        #     name="Test Deals",
        #     description="Deals",
        #     price=1.99,
        #     category="deals")
                                                                        
        self.product_clearance = Product.objects.create(
            name="Test Clearance",
            description="Clearance",
            price=1.99,
            category=self.category_clearance)

    def test_delete_category_of_product(self):
        """Test that when a category is deleted for a product, the category field on the product is emptied"""
        # TODO: Write test
        self.category_clearance.delete()
        with self.assertRaises(Product_Category.DoesNotExist):
            Product_Category.objects.get(name="clearance")
        product = Product.objects.get(name="Test Clearance")
        self.assertIsNone(product.category)

    def test_get_products(self):
        """ Test that when browsing to /products/ we get a 200 code, products/products.html template, context and that we have 1 product """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertIn(b'Products', response.content)
        self.assertEqual(1, response.context['products'].count())


    def test_select_categories(self):
        """ Test that when selecting categories we get a 200 code, products/products.html template and context """
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

        response = self.client.get('/products/?category=weights,clothes,shoes,accessories')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("weights,clothes,shoes,accessories", response.context['selected_categories'])
        self.assertEqual(4, response.context['products'].count())

        response = self.client.get('/products/?category=protein_powders')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("protein_powders", response.context['selected_categories'])        
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get('/products/?category=protein_bars')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("protein_bars", response.context['selected_categories'])        
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get('/products/?category=sports_drinks')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("sports_drinks", response.context['selected_categories'])        
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get('/products/?category=vitamins')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)    
        self.assertTrue("vitamins", response.context['selected_categories'])
        self.assertEqual(1, response.context['products'].count())

        response = self.client.get('/products/?category=protein_powders,protein_bars,sports_drinks,vitamins')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("protein_powders,protein_bars,sports_drinks,vitamins", response.context['selected_categories'])
        self.assertEqual(4, response.context['products'].count())

        response = self.client.get('/products/?category=new_arrivals')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("new_arrivals", response.context['selected_categories'])
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

        response = self.client.get('/products/?category=new_arrivals,deals,clearance')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("new_arrivals,deals,clearance", response.context['selected_categories']) 
        self.assertEqual(3, response.context['products'].count())
        

    def test_search_products(self):
        """ Test that when searching for 'ideal' we get a 200 code, products/products.html template, context and that we find 1 product """    
        response = self.client.get('/products/?q=ideal')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertTrue(response.context)
        self.assertTrue("ideal", response.context['search_term'])
        self.assertEqual(1, response.context['products'].count())

    
    def test_get_product_details(self):
        """ Test that when browsing to /products/1 we get a 200 code, products/product_detail.html template, context and that name and description are true """
        product_id = 1
        response = self.client.get('/products/' + str(product_id))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
        self.assertTrue(response.context)
        self.assertEqual('Test Product', response.context['product'].name)
        self.assertEqual('Ideal', response.context['product'].description)






