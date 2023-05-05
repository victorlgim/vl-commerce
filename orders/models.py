from django.db import models


class StatusOrder(models.TextChoices):
    PEDIDO_REALIZADO = "Pedido Realizado"
    PEDIDO_EM_ANDAMENTO = "Pedido em Andamento"
    ENTREGUE = "Entregue"


class Order(models.Model):
    status = models.CharField(
        max_length=20, choices=StatusOrder.choices, default=StatusOrder.PEDIDO_REALIZADO
    )
    total_price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total_quantity = models.PositiveIntegerField(default=0)
    buyed_at = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    users = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="orders"
    )


class OrderProduct(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.PositiveIntegerField(default=1)
    buyer = models.IntegerField()
    order = models.ForeignKey(
        "orders.Order", on_delete=models.CASCADE, related_name="order_products"
    )
