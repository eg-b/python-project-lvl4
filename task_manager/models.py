from django.db import models
from django.contrib.auth.models import User


class Users(models.Model):
    login = models.CharField(max_length=30)
    registration_date = models.DateTimeField(auto_now_add=True)