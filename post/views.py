from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer

class UserApiView(ListCreateAPIView):
  serializer_class = UserSerializer
  queryset = User.objects.all()


