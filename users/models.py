from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    is_seller = models.BooleanField(default=False, blank=True)
    is_superuser = models.BooleanField(default=False, blank=True)
    is_costumer = models.BooleanField(default=True, blank=True)
    email = models.EmailField(max_length=127, unique=True)
    username = models.CharField(max_length=30, blank=True, null=True)
