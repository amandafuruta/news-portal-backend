from rest_framework import serializers
from django.contrib.auth.models import User

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