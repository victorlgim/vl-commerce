from django.db import models


class Cart(models.Model):
    products = models.ManyToManyField("products.Product", related_name="carts")
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
        null=True
    )


class CartProducts(models.Model):
    cart = models.ForeignKey(
        "carts.Cart", on_delete=models.CASCADE, related_name="products_item"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE, related_name="cart_item"
    )
    quantity = models.PositiveIntegerField(default=0)
