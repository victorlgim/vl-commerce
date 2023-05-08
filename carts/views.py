from products.models import Product
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
    
class CartProductsView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    queryset = CartProducts.objects.all()
    serializer_class = CartProductsSerializer

    def perform_create(self, serializer):
        self.check_object_permissions(self.request, self.request.user)
        product = get_object_or_404(Product, pk=self.kwargs["pk"])

        if not Cart.objects.filter(client_id=self.request.user.id).exists():
            cart = Cart.objects.create(client=self.request.user)
            serializer.save(cart=cart, product=product, seller=product.seller)
        else:
            serializer.save(
                cart=self.request.user.cart, product=product, seller=product.seller
            )
