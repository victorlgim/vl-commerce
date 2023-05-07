from rest_framework import permissions
from .models import User


class IsAdminSellerOrClient(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (
            request.user.is_authenticated and (request.user.is_superuser or request.user.is_seller)
        )
    
class IsAdminToReadLists(permissions.BasePermission):
    def has_permission(self, request, view):
        if (request.method in permissions.SAFE_METHODS):
            return (request.user.is_authenticated and (request.user.is_superuser or request.user.is_seller)
        )
        return True
    
class IsAdminOrAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_superuser:
            return True
        
        return (request.user.is_authenticated and request.user.id == obj.id)