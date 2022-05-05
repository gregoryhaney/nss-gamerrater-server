from django.db import models
from django.contrib.auth.models import User

class Gamer(models.Model):
    handle = models.CharField(max_length=20)
    bio = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
