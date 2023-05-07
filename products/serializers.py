from rest_framework import serializers
from .models import Product, Category
from users.serializers import SellerSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "stock",
            "is_available",
            "price",
            "description",
            "img",
            "categories",
            "seller",
        ]

        extra_kwargs = {
            "img": {
                "read_only": True
            }
        }
