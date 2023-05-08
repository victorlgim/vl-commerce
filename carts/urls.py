from django.urls import path
from .views import CartView, CartProductsView, CartProductDetailView

urlpatterns = [
    path("carts/", CartView.as_view()),
    path("carts/<int:pk>/", CartProductsView.as_view()),
    path("carts/product/<int:product_id>/", CartProductDetailView.as_view()),
]