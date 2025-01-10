from rest_framework import serializers
from .models import Hobby, User, UserHobby, Friend

class HobbySerializer(serializers.ModelSerializer):
    """Serializer for the Hobby model"""
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        """Create and return a new hobby"""
        return Hobby.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """Update and return an existing hobby"""
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
class UserSerializer(serializers.ModelSerializer):
    TODO
    pass

class UserHobbySerializer(serializers.ModelSerializer):
    TODO
    pass

class FriendSerializer(serializers.ModelSerializer):
    TODO
    pass