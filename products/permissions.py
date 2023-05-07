from rest_framework import permissions
from rest_framework.views import Request, View
from .models import Product


class IsSellerProductOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: Product):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_authenticated and request.user.is_superuser:
            return True

        return request.user.is_authenticated and request.user.id == obj.seller.id
