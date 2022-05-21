from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_jwt.views import obtain_jwt_token
from .views import *

urlpatterns = [
    path('restaurant-list/', RestaurantListView.as_view(), name='restaurant-list'),
    path('create-restaurant/', RestaurantCreateView.as_view(), name='create-restaurant'),
    path('update-restaurant/<int:pk>/', RestaurantUpdateView.as_view(), name='update-restaurant'),

    path('menu-list/', MenuListView.as_view(), name='menu-list'),
    path('menu-vote/', CurrentDayMenuList.as_view(), name='menu-vote'),
    # path('create-menu/', MenuCreateView.as_view(), name='create-menu'),
    path('update-menu/<int:pk>/', MenuUpdateView.as_view(), name='update-menu'),
    path('upload-menu/', UploadMenuAPIView.as_view(), name="upload-menu"),
    path('vote/<int:menu_id>/', VoteAPIView.as_view(), name="new-vote"),
    path('menu-today/', CurrentDayMenuList.as_view(), name="menu-today"),
    path('results/<int:pk>/', ResultsAPIView.as_view(), name="results"),
]