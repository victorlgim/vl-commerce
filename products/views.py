from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrProductSeller
from users.permissions import IsAdminOrSellerOrReadOnly


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrSellerOrReadOnly]
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer