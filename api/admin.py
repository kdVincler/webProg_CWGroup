from django.contrib import admin
from .models import PageView, User

# Register your models here.
admin.site.register(PageView, User)
