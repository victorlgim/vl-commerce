from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    img = models.CharField(max_length=127, blank=True)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(max_length=127, unique=True)
    is_seller = models.BooleanField(default=False)

    address = models.OneToOneField(
        "users.Address", on_delete=models.CASCADE, related_name="user"
    )

   
