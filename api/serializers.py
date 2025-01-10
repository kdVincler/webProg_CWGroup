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
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255, required=False)
    email = serializers.EmailField(unique=True)
    date_of_birth = serializers.DateField(required=False)

    hobbies = HobbySerializer(many=True, required=False)
    friends = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        """Create and return a new user"""
        return User.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """Update and return an existing user"""
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.save()
        return instance


class UserHobbySerializer(serializers.ModelSerializer):
    TODO
    pass

class FriendSerializer(serializers.ModelSerializer):
    TODO
    pass