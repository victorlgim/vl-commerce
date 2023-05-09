from rest_framework import permissions
from .models import OrderProduct


class IsProductSeller(permissions.BasePermission):
    def has_object_permission(self, request, _, obj):
        order_product = OrderProduct.objects.filter(order_id=obj.id).first()
        return (
            request.method == "GET"
            or request.user.is_authenticated
            and (request.user.is_superuser or request.user.id == order_product.product.seller.id)
        )
