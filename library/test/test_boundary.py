from rest_framework.test import APITestCase
from library.test.TestUtils import TestUtils
from library.models import Product
from django.urls import reverse


class ProductBoundaryTest(APITestCase):

    def test_boundary_price_value(self):
        """Test if ListView includes a product with exactly $50 price"""
        test_obj = TestUtils()
        try:
            Product.objects.create(name="Boundary Product", price=50.00, stock=10)

            response = self.client.get(reverse("product-list"))
            if "Boundary Product" not in str(response.content):
                test_obj.yakshaAssert("TestBoundaryPriceValue", True, "boundary")
                print("TestBoundaryPriceValue = Passed")
            else:
                test_obj.yakshaAssert("TestBoundaryPriceValue", False, "boundary")
                print("TestBoundaryPriceValue = Failed")
        except:
            test_obj.yakshaAssert("TestBoundaryPriceValue", False, "boundary")
            print("TestBoundaryPriceValue = Failed")

    def test_large_stock_value(self):
        """Test if a product with a very large stock value can be created"""
        test_obj = TestUtils()
        try:
            product = Product.objects.create(name="Bulk Item", price=500.00, stock=999999)
            if product and product.stock == 999999:
                test_obj.yakshaAssert("TestLargeStockValue", True, "boundary")
                print("TestLargeStockValue = Passed")
            else:
                test_obj.yakshaAssert("TestLargeStockValue", False, "boundary")
                print("TestLargeStockValue = Failed")
        except:
            test_obj.yakshaAssert("TestLargeStockValue", False, "boundary")
            print("TestLargeStockValue = Failed")
