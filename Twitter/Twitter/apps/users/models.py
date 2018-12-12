from django.contrib.auth.models import AbstractBaseUser
from django.db import models

from Twitter.apps.users.manager import UserManager


class User(AbstractBaseUser):
    username = models.CharField(max_length=50, unique=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)

    objects = UserManager()
    USERNAME_FIELD = 'username'
