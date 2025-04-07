from django.urls import reverse
from rest_framework.test import APITestCase
from library.models import Product
from library.test.TestUtils import TestUtils

class ProductFunctionalTest(APITestCase):

    def test_create_product(self):
        """Test if a product is created successfully"""
        test_obj = TestUtils()
        try:
            product = Product.objects.create(name="Laptop", price=999.99, stock=10)
            if product:
                test_obj.yakshaAssert("TestCreateProduct", True, "functional")
                print("TestCreateProduct = Passed")
            else:
                test_obj.yakshaAssert("TestCreateProduct", False, "functional")
                print("TestCreateProduct = Failed")
        except:
            test_obj.yakshaAssert("TestCreateProduct", False, "functional")
            print("TestCreateProduct = Failed")

    def test_list_view_returns_filtered_products(self):
        """Test if ListView correctly filters products with price > $50"""
        test_obj = TestUtils()
        try:
            Product.objects.create(name="Expensive Laptop", price=999.99, stock=5)
            Product.objects.create(name="Cheap Mouse", price=30.00, stock=15)

            response = self.client.get(reverse("product-list"))
            if "Expensive Laptop" in str(response.content) and "Cheap Mouse" not in str(response.content):
                test_obj.yakshaAssert("TestListViewFiltering", True, "functional")
                print("TestListViewFiltering = Passed")
            else:
                test_obj.yakshaAssert("TestListViewFiltering", False, "functional")
                print("TestListViewFiltering = Failed")
        except:
            test_obj.yakshaAssert("TestListViewFiltering", False, "functional")
            print("TestListViewFiltering = Failed")
