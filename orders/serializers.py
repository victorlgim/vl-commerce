from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = [
            "id",
            "price",
            "status",
            "buyed_at",
            "buyer",
            "products",
        ]

        extra_kwargs = {
            "id": {"read_only": True},
            "buyed_at": {"read_only": True},
            "buyer": {"read_only": True},
            "products": {"read_only": True},
            "price": {"read_only": True},
        }