from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsSellerProductOrAdmin
from users.permissions import IsClientSellerAdmin


class ProductView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsClientSellerAdmin]
    queryset = Product.objects.all().order_by("id")
    serializer_class = ProductSerializer

    def get_queryset(self):
        name = self.request.query_params.get("name")
        category = self.request.query_params.get("category")

        if name:
            return Product.objects.filter(name__icontains=name)

        if category:
            return Product.objects.filter(categories__name__icontains=category)

        return super().get_queryset()

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSellerProductOrAdmin]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_url_kwarg = "product_id"
