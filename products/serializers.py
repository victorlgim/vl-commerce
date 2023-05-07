from rest_framework import serializers
from .models import Product, Category
from users.serializers import SellerSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]