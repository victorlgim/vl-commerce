from rest_framework import permissions
from .models import OrderProduct


class IsProductSeller(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        order_product = OrderProduct.objects.filter(order_id=obj.id).first()
        return (
            request.method == "GET"
            or request.user.is_authenticated
            and (request.user.is_superuser or request.user.id == order_product.product.seller.id)
        )

class IsAdminOrSeller(permissions.BasePermission):
    def has_permission(self, request, view, obj=None):
        return (
            request.method == "POST"
            or request.user.is_authenticated
            and (request.user.is_superuser or request.user.is_seller)
        )

class IsAdminOrSellerOrOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.method == "PATCH"
            or request.user.is_authenticated
            and (request.user.is_superuser or request.user.is_seller or request.user.id == obj.user_id)
        )