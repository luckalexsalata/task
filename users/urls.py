from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework_jwt.views import obtain_jwt_token
from .views import *

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/token/', obtain_auth_token, name='token'),
    path('list/', UserList.as_view(), name='user-list'),
    path('retrieve/<int:pk>/', UserRetrieveView.as_view()),
    path('update/<int:pk>/', UserUpdateView.as_view()),
    path('destroy/<int:pk>/', UserDestroyView.as_view()),
]