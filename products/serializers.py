from rest_framework import serializers
from .models import Product
from users.serializers import SellerSerializer


class ProductSerializer(serializers.ModelSerializer):
    seller = SellerSerializer(read_only=True)

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
            "category",
            "seller",
        ]

        extra_kwargs = {
            "id": {
                "read_only": True
            }
        }
    def create(self, validated_data):
            product = Product.objects.create(**validated_data)

            return product
    

    def update(self, instance, validated_data):
            instance.__dict__.update(validated_data)
            instance.save()
            return instance 
    
    is_available = serializers.SerializerMethodField()

    def get_is_available(self, obj) -> bool:
        return bool(obj.inventory)