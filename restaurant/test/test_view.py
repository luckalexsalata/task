from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory


class TestRestaurantViews(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.user = self.setup_user()
        self.token = Token.objects.create(user=self.user)
        self.token.save()
        self.client.force_authenticate(self.user)

    @staticmethod
    def setup_user():
        User = get_user_model()
        return User.objects.create_user(
            'test',
            email='testuser@test.com',
            password='test'
        )

    def test_restaurant_list(self):
        url = reverse('restaurant-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_restaurant_create(self):
        url = reverse('create-restaurant')
        data = {'name': 'restaurant0', 'address': 'address0'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_restaurant_update(self):
        url1 = reverse('create-restaurant')
        data1 = {'name': 'restaurant0', 'address': 'address0'}
        self.client.post(url1, data1)
        url = reverse('update-restaurant', args=['1'])
        data = {'name': 'restaurant0', 'address': 'address0'}
        response = self.client.put(url, data=data)
        self.assertEqual(response.status_code, 200)

    def test_menu_list(self):
        url = reverse('menu-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_menu_upload(self):
        data1 = {'name': 'restaurant0', 'address': 'address0'}
        self.client.post(reverse('create-restaurant'), data1)
        url = reverse('upload-menu')
        data = {'restaurant': '1', 'name': 'menu0', 'details': 'details0'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

    def test_menu_today(self):
        url = reverse('menu-today')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_vote(self):
        data1 = {'name': 'restaurant0', 'address': 'address0'}
        self.client.post(reverse('create-restaurant'), data1)
        data2 = {'restaurant': '1', 'name': 'menu0', 'details': 'details0'}
        self.client.post(reverse('upload-menu'), data2)
        url = reverse('new-vote', args=['1'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_result(self):
        data1 = {'name': 'restaurant0', 'address': 'address0'}
        self.client.post(reverse('create-restaurant'), data1)
        data2 = {'restaurant': '1', 'name': 'menu0', 'details': 'details0'}
        self.client.post(reverse('upload-menu'), data2)
        self.client.get(reverse('new-vote', args=['1']))
        url = reverse('results', args=['1'])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)