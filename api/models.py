from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


class PageView(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return f"Page view count: {self.count}"
    
class User(AbstractUser):
    pass
