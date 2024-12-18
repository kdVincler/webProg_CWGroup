from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import PageView, User, Hobby, UserHobby

# Register your models here.
admin.site.register(PageView)
admin.site.register(User, UserAdmin)
admin.site.register(Hobby)
admin.site.register(UserHobby)
