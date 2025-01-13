from rest_framework import serializers
from .models import Hobby, User, UserHobby, Friend

class HobbySerializer(serializers.ModelSerializer):
    """Serializer for the Hobby model"""
    class Meta:
        model = Hobby
        fields = ['id','name']
    
class UserSerializer(serializers.ModelSerializer):
    """Serializer for the User model"""
    hobbies = HobbySerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'date_of_birth', 'hobbies']


class UserHobbySerializer(serializers.ModelSerializer):
    """Serializer for the UserHobby model"""
    class Meta:
        model = UserHobby
        fields = ['user', 'hobby']


class FriendUserSerializer(serializers.ModelSerializer):
    """Helper serializer for the Friend model's user1 and user2 fields"""
    class Meta:
        model = User
        fields = ['id', 'username', 'name']


class FriendSerializer(serializers.ModelSerializer):
    """Serializer for the Friend model"""
    user1 = FriendUserSerializer(read_only=True)
    user2 = FriendUserSerializer(read_only=True)

    class Meta:
        model = Friend
        fields = ['user1', 'user2', 'accepted']
    