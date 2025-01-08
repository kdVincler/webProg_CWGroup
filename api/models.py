from django.db import models
from django.contrib.auth.models import AbstractUser
from typing import Dict, Optional, List


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
    
    def as_dict(self) -> Dict[str, Optional[int | str]]:
        """JSON representation of the hobby"""
        return {
            "id": self.id,
            "name": self.name,
        }
     
class User(AbstractUser):
    """User model"""
    name: str = models.CharField(max_length=255, blank=True, null=True)
    email: str = models.EmailField(unique=True)
    date_of_birth: str = models.DateField(blank=True, null=True)

    # Many-to-Many relationship with Hobby
    hobbies: models.ManyToManyField = models.ManyToManyField(Hobby, through='UserHobby')

    def __str__(self) -> str:
        """String representation of the user"""
        return self.email
    
    def as_dict(self) -> Dict[str, Optional[int | str | List[Dict[str, Optional[int | str]]]]]:
        """JSON representation of the user"""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "date_of_birth": self.date_of_birth,
            "hobbies": [hobby.as_dict() for hobby in self.hobbies.all()]
        }

class UserHobby(models.Model):
    """Model representing the relationship between a user and a hobby"""
    user: models.ForeignKey = models.ForeignKey(User, on_delete=models.CASCADE)
    hobby: models.ForeignKey = models.ForeignKey(Hobby, on_delete=models.CASCADE)

    def __str__(self) -> str:
        """String representation of the user-hobby relationship"""
        return f"{self.user} - {self.hobby}"
    
    def as_dict(self) -> Dict[str, Optional[Dict[str, Optional[int | str]]]]:
        """JSON representation of the user-hobby relationship"""
        return {
            "user": self.user.as_dict(),
            "hobby": self.hobby.as_dict(),
        }
  