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




