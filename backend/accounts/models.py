from django.db import models
from django.contrib.auth.models import AbstractUser

# custom User
class User(AbstractUser):

    def __str__(self):
        return self.username

