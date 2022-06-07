from django.test import TestCase
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

selenium = webdriver.Chrome()

# Create your tests here.
class TestViews(TestCase):

    def test_get_home(self):
        """ Test that when browsing to / we get a 200 code and home/index.html template"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_get_signup(self):
        """ Test that when browsing to /accounts/signup we get a 200 code and account/signup.html template"""
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_get_login(self):
        """ Test that when browsing to /accounts/login we get a 200 code and account/login.html template"""
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/login.html')

    def test_get_password_reset(self):
        """ Test that when browsing to /accounts/password/reset we get a 200 code and account/password_reset.html template"""
        response = self.client.get('/accounts/password/reset/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/password_reset.html')

class SeleniumTests(LiveServerTestCase):            
    
    def test_click_home(self):
        """Test that clicking on the brand logo in the navbar takes us back to / """        
        url = 'https://code-institute-ms4.herokuapp.com/'

        selenium.get(url)
        home_element = selenium.find_element(By.XPATH, "/html/body/header/div[1]/div[1]/a/h1")
        home_element.click

        assert url == selenium.current_url        
    

    
    

        
