from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import OrderSerializer
from .models import Order
from rest_framework import generics
from carts.permissions import IsOwner
from .permissions import IsAdminOrSeller, IsProductSeller, IsAdminOrSellerOrOwner


class OrderView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwner, IsAdminOrSeller]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        self.check_object_permissions(self.request, self.request.user)
        serializer.save(user_id=self.request.user.id)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsProductSeller, IsAdminOrSellerOrOwner]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    lookup_url_kwarg = "order_id"
