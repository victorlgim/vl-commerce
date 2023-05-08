from rest_framework import permissions
from users.models import User


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, _, obj: User):

        return request.user.is_authenticated and obj == request.user