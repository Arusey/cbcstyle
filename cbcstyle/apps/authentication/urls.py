from django.urls import path
from .views import UserCreateAPIView, UserLoginAPIView

urlpatterns = [
    path('user/create/', UserCreateAPIView.as_view(), name='user-create'),
    path('user/login/', UserLoginAPIView.as_view(), name='user-login'),
]
