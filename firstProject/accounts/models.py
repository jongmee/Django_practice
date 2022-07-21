from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_phone = models.CharField(max_length=12)
    user_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user_name
