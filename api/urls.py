"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

from . import views
#from .views import main_spa

urlpatterns = [
    path('', views.main_spa),
    path('users/', views.user_list_view, name='user_list'),
    path('users/<int:user_id>/', views.user_api, name='user_detail'),
    path('hobby/', views.hobby_list_view, name='hobby_list'),
    path('hobby/<int:hobby_id>/', views.hobby_api, name='hobby_detail'),
    path('userhobby/', views.user_hobby_list_view, name='user_hobby_list'),
    path('userhobby/<int:user_hobby_id>/', views.user_hobby_api, name='user_hobby_detail'),
]
