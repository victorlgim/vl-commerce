from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdminOrProductSeller
from users.permissions import IsAdminOrSellerOrReadOnly
