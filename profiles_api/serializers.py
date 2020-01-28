from rest_framework import serializers
from . import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=20)


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile Object"""
    class Meta:  # this is call method class
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {  # To add extra key argument
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return new user"""
        user=models.UserProfile.objects.create_user(
            validated_data['email'],
            validated_data['name'],
            validated_data['password']
        )
        return user
