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
            "inventory",
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
    def create(self, validated_data):
            categories_data = validated_data.pop("categories")
            product = Product.objects.create(**validated_data)

            for category in categories_data:
                categoryExists = Category.objects.get_or_create(name__iexact=category["name"])
                product.categories.add(categoryExists)

            return product
    

    def update(self, instance, validated_data):
            categories_data = validated_data.pop("categories")

            for category in categories_data:
                categoryExists = Category.objects.get_or_create(name__iexact=category["name"])
                instance.categories.add(categoryExists)

            instance.__dict__.update(validated_data)
            instance.save()
            return instance 
    
    categories = CategorySerializer(many=True)
    seller = SellerSerializer(read_only=True)

    is_available = serializers.SerializerMethodField()

    def get_is_available(self, obj) -> bool:
        return bool(obj.stock)