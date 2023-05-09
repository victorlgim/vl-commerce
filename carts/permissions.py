from rest_framework import permissions

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, _, obj):

        return request.user.is_authenticated and obj == request.user