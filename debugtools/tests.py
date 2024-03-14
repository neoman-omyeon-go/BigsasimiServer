from django.test import TestCase
from rest_framework.test import APIClient


class Test(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_funtion(self):
        x = self.client.get('/test')
        self.assertEqual(x.status_code, 301)

    def test_success(self):
        a = 1
        b = 1
        assert (a + b == 2)
