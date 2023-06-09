from datetime import timezone
from django.db import models


class StatusOrder(models.TextChoices):
    PEDIDO_REALIZADO = "Pedido Realizado"
    PEDIDO_EM_ANDAMENTO = "Pedido em Andamento"
    ENTREGUE = "Entregue"


class Order(models.Model):
    status = models.CharField(
        max_length=20, choices=StatusOrder.choices, default=StatusOrder.PEDIDO_REALIZADO
    )
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    buyed_at = models.DateTimeField(auto_now_add=True)
    buyer = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )
    products = models.ManyToManyField(
        "products.Product", through="orders.OrderProduct", related_name="orders"
    )


class OrderProduct(models.Model):
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=0)
    order = models.ForeignKey(
        "orders.Order", on_delete=models.CASCADE, related_name="order_products"
    )
    product = models.ForeignKey(
        "products.Product", on_delete=models.CASCADE
    )
