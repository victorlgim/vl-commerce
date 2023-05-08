from products.models import Product
from .models import CartProducts, Cart
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .serializers import CartProductsSerializer
from .permissions import IsOwner
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Response, status
from users.models import User


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

class CartProductsDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner]

    def delete(self, request, product_id):
        user = get_object_or_404(User, id=request.user.id)
        cart = get_object_or_404(Cart, id=user.cart.id)

        cart_product = CartProducts.objects.filter(
            cart_id=cart.id, product_id=product_id
        ).first()

        if not cart_product:
            return Response(
                {"message": "Product not found in cart"}, status.HTTP_404_NOT_FOUND
            )

        cart_product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)