from allauth.account.adapter import get_adapter
from rest_framework import serializers
# from django.contrib.auth.models import User
from users.models import User, Employee
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_owner', 'is_employee')




