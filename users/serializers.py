from rest_framework import serializers
from .models import User, Address

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
          model = User
          fields = [
             "id",
             "first_name",
             "last_name",
             "email"
          ]

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
        fields = [
            "id",
            "first_name",
            "last_name",
            "img",
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

    address = AddressSerializer()

    def create(self, validated_data):
        address = validated_data.pop("address")
        address_obj = Address.objects.create(**address)

        user = {
            User.objects.create_superuser
            if validated_data.get("is_superuser")
            else User.objects.create_user
        }
        
        return user(**validated_data, address=address_obj)
    
    def update(self, instance, validated_data):
        password = validated_data.pop("password")
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

