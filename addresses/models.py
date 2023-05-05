from django.db import models


class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.IntegerField()
    complement = models.IntegerField()
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=20)
    
    user = models.OneToOneField(
        "users.User",
        on_delete=models.CASCADE,
    )
