from rest_framework import serializers
from .models import Hobby, User, UserHobby, Friend

class HobbySerializer(serializers.ModelSerializer):
    """Serializer for the Hobby model"""
    class Meta:
        model = Hobby
        fields = ['name']
    
class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model"""
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'date_of_birth', 'hobbies', 'friends']


class UserHobbySerializer(serializers.ModelSerializer):
    """Serializer for the UserHobby model"""
    class Meta:
        model = UserHobby
        fields = ['user', 'hobby']

class FriendSerializer(serializers.ModelSerializer):
    """Serializer for the Friend model"""
    class Meta:
        model = Friend
        fields = ['user1', 'user2', 'accepted', 'created_at', 'updated_at']
    