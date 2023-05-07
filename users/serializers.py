from rest_framework import serializers
from .models import User, Address

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "zip_code",
            "state",
            "city",
            "neighborhood",
            "number",
            "street"
        ]
        
        extra_kwargs = {
            "id": {
                "read_only": True
            }
        }
    
    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        felds = [
            "id",
            "first_name",
            "last_name",
            "img",
            "neighborhood",
            "email",
            "is_seller",
            "is_superuser",
            "password",
            "username",
            "address"
        ]

        extra_kwargs = {
            "id": {
                "read_only": True
            },
            "password": {
                "write_only": True
            }
        }