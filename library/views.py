from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import status
from .models import Product

class ProductListView(APIView):
    def get(self, request):
        try:
            products = Product.objects.filter(price__gt=50)  # Fetch only products priced above $50
            if not products.exists():
                return JsonResponse({"message": "No products available"}, status=status.HTTP_200_OK)

            product_list = list(products.values("id", "name", "price", "stock", "created_at"))
            return JsonResponse(product_list, safe=False, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
