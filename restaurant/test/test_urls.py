from rest_framework.test import APISimpleTestCase
from django.urls import reverse, resolve
from restaurant.views import *


class TestUrls(APISimpleTestCase):

    def test_restaurant_list_url_is_resolves(self):
        url = reverse('restaurant-list')
        self.assertEquals(resolve(url).func.view_class, RestaurantListView)

    def test_restaurant_create_url_is_resolves(self):
        url = reverse('create-restaurant')
        self.assertEquals(resolve(url).func.view_class, RestaurantCreateView)

    def test_restaurant_update_url_is_resolves(self):
        url = reverse('update-restaurant', args=['1'])
        self.assertEquals(resolve(url).func.view_class, RestaurantUpdateView)

    def test_menu_list_url_is_resolves(self):
        url = reverse('menu-list')
        self.assertEquals(resolve(url).func.view_class, MenuListView)

    def test_menu_update_url_is_resolves(self):
        url = reverse('update-menu', args=['1'])
        self.assertEquals(resolve(url).func.view_class, MenuUpdateView)

    def test_menu_today_url_is_resolves(self):
        url = reverse('menu-today')
        self.assertEquals(resolve(url).func.view_class, CurrentDayMenuList)

    def test_vote_url_is_resolves(self):
        url = reverse('new-vote', args=['1'])
        self.assertEquals(resolve(url).func.view_class, VoteAPIView)

    def test_result_url_is_resolves(self):
        url = reverse('results', args=['1'])
        self.assertEquals(resolve(url).func.view_class, ResultsAPIView)