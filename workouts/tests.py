from django.test import TestCase

# Create your tests here.
# TODO: use tests in products as basis

class TestViews(TestCase):

    def test_get_workouts(self):
        """ Test that when browsing to /workouts/ we get a 200 code,
        workouts/workouts.html template and context """
        response = self.client.get('/workouts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workouts/workouts.html')
        self.assertTrue(response.context)