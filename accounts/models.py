from django.db import models
from django.core.exceptions import ValidationError


class Login(models.Model):
  username = models.CharField(max_length=18, unique=True)
  password = models.CharField(max_length=10)
