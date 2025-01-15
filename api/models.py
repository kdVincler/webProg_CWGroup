from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class PageView(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Page view count: {self.count}"

class Hobby(models.Model):
    """Hobby model"""
    name = models.CharField(max_length=255)

    def __str__(self):
        """String representation of the hobby"""
        return self.name
    
     
class User(AbstractUser):
    """User model"""
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)

    # Many-to-Many relationship with Hobby
    hobbies = models.ManyToManyField(Hobby, through='UserHobby')

    # Many-to-Many relationship with User
    friends = models.ManyToManyField('self', through='Friend', symmetrical=False)

    def __str__(self):
        """String representation of the user"""
        return self.email
    

class UserHobby(models.Model):
    """Model representing the relationship between a user and a hobby"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of the user-hobby relationship"""
        return f"{self.user} - {self.hobby}"
    

class Friend(models.Model):
    """Model representing the relationship between two users"""
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships_initiated')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships_received')
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """String representation of the friend relationship"""
        return f"{self.user1} {'friends with' if self.accepted else 'requested'} {self.user2}"


    class Meta:
        unique_together = ('user1', 'user2')

