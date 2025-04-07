
from rest_framework.test import APITestCase
from django.db import IntegrityError
from library.test.TestUtils import TestUtils
from django.urls import reverse
from unittest.mock import patch
from django.urls import get_resolver
class ProductExceptionalTest(APITestCase):

    def test_empty_product_list(self):
        """Test if ListView handles an empty product list gracefully"""
        test_obj = TestUtils()
        try:
            response = self.client.get(reverse("product-list"))
            if response.status_code == 200 and "No products available" in str(response.content):
                test_obj.yakshaAssert("TestEmptyProductList", True, "exceptional")
                print("TestEmptyProductList = Passed")
            else:
                test_obj.yakshaAssert("TestEmptyProductList", False, "exceptional")
                print("TestEmptyProductList = Failed")
        except Exception as e:
            test_obj.yakshaAssert("TestEmptyProductList", False, "exceptional")
            print("TestEmptyProductList = Failed")

    def test_invalid_url(self):
        """Test if an incorrect URL returns a 404 error"""
        test_obj = TestUtils()
        try:
            response = self.client.get("/invalid-url/")
            if response.status_code == 404:
                test_obj.yakshaAssert("TestInvalidURL", True, "exceptional")
                print("TestInvalidURL = Passed")
            else:
                test_obj.yakshaAssert("TestInvalidURL", False, "exceptional")
                print("TestInvalidURL = Failed")
        except:
            test_obj.yakshaAssert("TestInvalidURL", False, "exceptional")
            print("TestInvalidURL = Failed")
