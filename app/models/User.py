from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser,User


class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_field  = models.BooleanField(default=False)
    
