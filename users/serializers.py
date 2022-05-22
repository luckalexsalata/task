from rest_framework import serializers
from users.models import User, Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_owner', 'is_employee')




