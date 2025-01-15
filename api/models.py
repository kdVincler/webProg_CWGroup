from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class PageView(models.Model):
    count: int = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"Page view count: {self.count}"

class Hobby(models.Model):
    """Hobby model"""
    name: str = models.CharField(max_length=255)

    def __str__(self) -> str:
        """String representation of the hobby"""
        return self.name
    
     
class User(AbstractUser):
    """User model"""
    name: str = models.CharField(max_length=255, blank=True, null=True)
    email: str = models.EmailField(unique=True)
    date_of_birth: str = models.DateField(blank=True, null=True)

    # Many-to-Many relationship with Hobby
    hobbies: models.ManyToManyField = models.ManyToManyField(Hobby, through='UserHobby')

    # Many-to-Many relationship with User
    friends: models.ManyToManyField = models.ManyToManyField('self', through='Friend', symmetrical=False)

    def __str__(self) -> str:
        """String representation of the user"""
        return self.email
    

class UserHobby(models.Model):
    """Model representing the relationship between a user and a hobby"""
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    hobby: models.ForeignKey = models.ForeignKey(Hobby, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """String representation of the user-hobby relationship"""
        return f"{self.user} - {self.hobby}"
    

class Friend(models.Model):
    """Model representing the relationship between two users"""
    user1: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships_initiated')
    user2: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friendships_received')
    accepted: bool = models.BooleanField(default=False)
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """String representation of the friend relationship"""
        return f"{self.user1} {'friends with' if self.accepted else 'requested'} {self.user2}"


    class Meta:
        unique_together: tuple[str, str] = ('user1', 'user2')

