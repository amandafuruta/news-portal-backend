from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer, PostListSerializer
from .models import PostList

class UserApiView(ListCreateAPIView):
  serializer_class = UserSerializer
  queryset = User.objects.all()

class PostListApiView(ListCreateAPIView):
  serializer_class = PostListSerializer
  queryset = PostList.objects.all()

# Delete post
class PostDetailApiView(RetrieveDestroyAPIView):
    serializer_class = PostListSerializer
    queryset = PostList.objects.all()
