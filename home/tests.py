from .models import Feature
from django.forms import ValidationError
from django.test import TestCase


class TestModels(TestCase):
    def test_blank_feature(self):
        """
        When a feature is created with no
        info, we get a ValidationError
        """
        test_feature = Feature.objects.create()
        with self.assertRaises(ValidationError):
            test_feature.full_clean()

    def test_max_length_name_feature(self):
        """
        When a feature is created with a header longer than
        254 characters, we get a ValidationError
        """
        long_header = "x" * 255
        test_feature = Feature.objects.create(header=long_header)
        with self.assertRaises(ValidationError):
            test_feature.full_clean()


class TestViews(TestCase):
    def test_get_home(self):
        """
        When browsing to / we get a 200 code,
        context and home/index.html template
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")
        self.assertTrue(response.context)

    def test_get_signup(self):
        """
        When browsing to /accounts/signup we
        get a 200 code and account/signup.html template
        """
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/signup.html")

    def test_get_login(self):
        """
        When browsing to /accounts/login we
        get a 200 code and account/login.html template
        """
        response = self.client.get("/accounts/login/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/login.html")

    def test_get_password_reset(self):
        """
        When browsing to /accounts/password/reset
        we get a 200 code and account/password_reset.html template
        """
        response = self.client.get("/accounts/password/reset/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "account/password_reset.html")
