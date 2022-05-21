from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# class Person(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


class User(AbstractUser):
    is_owner = models.BooleanField(default=False)
    is_employee = models.BooleanField(default=True)


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.user.username

