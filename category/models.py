from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=80)

    products = models.ManyToManyField(
        'products.Product',
        related_name='categories'
    )

