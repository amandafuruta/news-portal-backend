from rest_framework import serializers
from django.contrib.auth.models import User
from .models import PostList

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensure password is write-only

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']

    def create(self, validated_data):
        # Remove the password field temporarily before creating the user
        password = validated_data.pop('password')

        # Create the user
        user = User(**validated_data)

        # Set the password (this automatically hashes it)
        user.set_password(password)

        # Save the user instance
        user.save()

        return user
    
class PostListSerializer(serializers.ModelSerializer):
    datePublished = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    
    class Meta:
        model = PostList
        fields = ['id','category', 'title', 'subtitle', 'datePublished', 'dateUpdated', 'auth', 'body', 'image', 'alt', 'section', 'order']
    
    def update(self, instance, validated_data):
        # Handle image field in case it's not provided in the request
        image = validated_data.get('image', None)
        if not image:
            validated_data.pop('image', None)

        # Update the instance with other fields
        return super().update(instance, validated_data)