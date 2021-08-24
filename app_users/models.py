from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# class User(models.Model):
#     fname = models.CharField(max_length=50)
#     lname = models.CharField(max_length=50)
#     email = models.EmailField()
#     username = models.CharField(max_length=50)
#     wins = models.IntegerField()
#     losses = models.IntegerField()

class CustomUser(AbstractUser):

    username = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    user_image = models.ImageField()

    def __str__(self):
        return self.username
