from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000, null=True)
    img = models.CharField(max_length=200, blank=True)
    inventory = models.IntegerField()
    price = models.FloatField()
    seller = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="products")


class Category(models.Model):
    name = models.CharField(max_length=30)

    products = models.ManyToManyField("products.Product", related_name="categories")
