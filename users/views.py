from .models import User, Address
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics, serializers
from .serializers import UserSerializer, AddressSerializer
from .permissions import IsAccountOwnerOrAdmin, IsAdminToReadLists


class UserView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminToReadLists]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdmin]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        return (
            serializers.ValidationError({"message": "Unauthorized request"}, status=401)
            if not self.request.user.is_superuser
            and "is_seller" in serializer.validated_data
            else serializer.save()
        )

class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrAdmin]
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
