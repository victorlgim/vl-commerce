from rest_framework import serializers
from .models import Cart, CartProducts
from rest_framework.views import status


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["id", "client", "products"]

        extra_kwargs = {
            "id": {"read_only": True},
            "client": {"read_only": True},
        }
