from rest_framework import serializers
from .models import Cart, CartProducts
from rest_framework.views import status


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "user", "products"]

        extra_kwargs = {
            "id": {"read_only": True},
            "user": {"read_only": True},
        }


class CartProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartProducts
        fields = ["id", "product", "cart", "quantity"]
        read_only_fields = ["id", "cart", "product"]

    def create(self, validated_data):
        cart = validated_data["cart"]
        product = validated_data["product"]
        quantity = validated_data["quantity"]

        if CartProducts.objects.filter(cart=cart, product=product).exists():
            cart_product = CartProducts.objects.get(cart=cart, product=product)
            quantity += cart_product.quantity

        if product.inventory < quantity:
            raise serializers.ValidationError(
                {"message": "Insufficient inventory"}, status.HTTP_400_BAD_REQUEST
            )

        return CartProducts.objects.create(**validated_data)
    
