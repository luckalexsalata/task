from rest_framework import serializers
from .models import *


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['name', 'address']


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['restaurant', 'name', 'details']


class UploadMenuSerializer(serializers.ModelSerializer):

    def create(self, validated_data):

        menu = Menu(
            restaurant=validated_data['restaurant'],
            name=validated_data['name'],
            details=validated_data['details'],
        )
        menu.save()
        return menu

    class Meta:
        fields = [
            'restaurant',
            'name',
            'details'
        ]
        model = Menu


class ResultMenuListSerializer(serializers.ModelSerializer):

    # restaurant = serializers.CharField(read_only=True)

    class Meta:
        model = Menu
        fields = [
            'restaurant',
            'name',
            'details',
            'votes',
            'created_at'
        ]