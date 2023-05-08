from .models import CartProducts, Cart
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .serializers import CartProductsSerializer
from .permissions import IsOwner
from django.shortcuts import get_object_or_404


class CartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    serializer_class = CartProductsSerializer

    def get_queryset(self):
        cart = get_object_or_404(Cart, id=self.request.user.cart.id)

        return CartProducts.objects.filter(cart_id=cart.id)