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