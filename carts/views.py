from products.models import Product
from .models import CartProducts, Cart
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .serializers import CartProductsSerializer
from .permissions import IsOwner
from django.shortcuts import get_object_or_404
from rest_framework.views import Response
from users.models import User


class CartView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    serializer_class = CartProductsSerializer

    def get_queryset(self):
        cart = get_object_or_404(Cart)

        return CartProducts.objects.filter(cart_id=cart.id)
    
class CartProductsView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    queryset = CartProducts.objects.all()
    serializer_class = CartProductsSerializer

    def perform_create(self, serializer):
        self.check_object_permissions(self.request, self.request.user)
        product = get_object_or_404(Product, pk=self.kwargs["pk"])

        if not Cart.objects.filter(user_id=self.request.user.id).exists():
            cart = Cart.objects.create(user=self.request.user)
            serializer.save(cart=cart, product=product)
        else:
            serializer.save(
                cart=self.request.user.cart, product=product
            )

class CartProductDeleteView(generics.DestroyAPIView):
    queryset = CartProducts.objects.all()
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]
    serializer_class = CartProductsSerializer

    def get_object(self):
        user = get_object_or_404(User, id=self.request.user.id)
        cart = get_object_or_404(Cart, id=user.cart.id)
        return get_object_or_404(CartProducts, cart_id=cart.id, product_id=self.kwargs['product_id'])

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=204)