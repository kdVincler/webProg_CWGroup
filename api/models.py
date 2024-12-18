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
    description = models.TextField()

    def __str__(self):
        """String representation of the hobby"""
        return self.name
    
    def as_dict(self):
        """JSON representation of the hobby"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
     
class User(AbstractUser):
    """User model"""
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)

    # Many-to-Many relationship with Hobby
    hobbies = models.ManyToManyField(Hobby, through='UserHobby')

    password = models.CharField(max_length=255)

    # Many-to-Many relationship with Hobby
    hobbies = models.ManyToManyField(Hobby, through='UserHobby')

    def __str__(self):
        """String representation of the user"""
        return self.email
    
    def as_dict(self):
        """JSON representation of the user"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "date_of_birth": self.date_of_birth,
            "password": self.password,
            "hobbies": [hobby.as_dict() for hobby in self.hobbies.all()]
        }

class UserHobby(models.Model):
    """Model representing the relationship between a user and a hobby"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hobby = models.ForeignKey(Hobby, on_delete=models.CASCADE)

    def __str__(self):
        """String representation of the user-hobby relationship"""
        return f"{self.user} - {self.hobby}"
    
    def as_dict(self):
        """JSON representation of the user-hobby relationship"""
        return {
            "user": self.user.as_dict(),
            "hobby": self.hobby.as_dict(),
        }
  