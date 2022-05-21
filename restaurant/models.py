from django.db import models
from users.models import User


class Restaurant(models.Model):
     name = models.CharField(max_length=200)
     address = models.CharField(
          max_length=255,
          blank=True,
          null=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)


class Menu(models.Model):
     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
     name = models.CharField(max_length=1002)
     details = models.CharField(max_length=256, blank=True, null=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     votes = models.IntegerField(default=0)


class Vote(models.Model):
    """Represents vote class model"""
    employee = models.ForeignKey('users.User', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.employee}'
