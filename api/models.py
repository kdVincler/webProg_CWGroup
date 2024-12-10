from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class PageView(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Page view count: {self.count}"
    
class User(AbstractUser):
    name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(blank=True, null=True)
    # hobbies as another class ?
    password = models.CharField(max_length=255)

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
            "password": self.password
        }
