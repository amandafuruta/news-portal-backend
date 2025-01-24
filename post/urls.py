from django.urls import path
from .views import UserApiView 
from rest_framework.authtoken import views

urlpatterns = [
    path('users', UserApiView.as_view()),
    path('token-auth', views.obtain_auth_token)
]