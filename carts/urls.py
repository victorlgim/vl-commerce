from django.urls import path
from .views import CartView, CartProductsView

urlpatterns = [
    path("carts/", CartView.as_view()),
    path("carts/<int:pk>/", CartProductsView.as_view())
]