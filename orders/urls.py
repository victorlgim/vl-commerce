from django.urls import path
from .views import OrderView, OrderDetailView

urlpatterns = [
    path("orders/", OrderView.as_view()),
    path("orders/<int:order_id>/", OrderDetailView.as_view()),
]
