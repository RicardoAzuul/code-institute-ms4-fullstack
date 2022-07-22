from django.test import TestCase


class TestViews(TestCase):
    def test_get_cart(self):
        """
        When browsing to /cart/ we get
        a 200 code and cart/cart.html template
        """
        response = self.client.get("/cart/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "cart/cart.html")
