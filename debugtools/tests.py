from django.test import TestCase
from rest_framework.test import APIClient
from utils.apihelper import FJR, FormatResponse
from rest_framework import status
from django.http import JsonResponse


class Test(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_funtion(self):
        x = self.client.get('/test/')
        self.assertEqual(x.status_code, 200)
        x = self.client.get('/test/?json=ture')
        self.assertEqual(x.status_code, 200)

    def test_success(self):
        a = 1
        b = 1
        assert (a + b == 2)

    def test_ResponseValue(self):
        rawdata = {"a":1, "b":1.1234567890, "c":{"1":1234}}
        a = FJR(error="error", msg="test test\n\0%%$", data=rawdata, status=status.HTTP_202_ACCEPTED)
        b = JsonResponse(FormatResponse(error="error", msg="test test\n\0%%$", data=rawdata), status=status.HTTP_202_ACCEPTED)
        assert (not (a is b))
        assert (a.content == b.content)
