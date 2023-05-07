from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=127, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11, unique=True)
    is_seller = models.BooleanField(default=False, blank=True)
    is_superuser = models.BooleanField(default=False, blank=True)

   
