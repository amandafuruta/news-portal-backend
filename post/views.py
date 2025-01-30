from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth.models import User
from .serializers import UserSerializer, PostListSerializer
from .models import PostList
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth.models import Group
from rest_framework.exceptions import AuthenticationFailed

class UserApiView(ListCreateAPIView):
  serializer_class = UserSerializer
  queryset = User.objects.all()

class PostListApiView(ListCreateAPIView):
  serializer_class = PostListSerializer
  queryset = PostList.objects.all()

# Delete post
class PostDetailApiView(RetrieveUpdateDestroyAPIView):
  serializer_class = PostListSerializer
  queryset = PostList.objects.all()
  def perform_update(self, serializer):
    # Any additional custom logic for updating posts
    serializer.save()

class CustomObtainAuthToken(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
      # Obtain the regular token
      response = super().post(request, *args, **kwargs)
      
      # Get the user from the request data
      username = request.data.get('username')
      user = User.objects.get(username=username)
      
      # Check if the user belongs to a group (team)
      team_group = Group.objects.get(name="Editor")  # Replace with the actual team name
      
      if not user.groups.filter(name=team_group.name).exists():
        raise AuthenticationFailed('You are not a member of the team.')
      
      return response
