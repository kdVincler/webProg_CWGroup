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

    # path('users/<int:user_id>/', views.user_api, name='user_detail'),
    path('login/', views.log_in_view, name='login'),
    path('logout/', views.log_out_view, name='logout'),
    path('register/', views.register, name='register'),
    path('auth-status/', views.check_auth_status, name='auth_status'),
    path('users/page/<int:page_number>/', views.paginate_users, name='users_pagination'),

    path('hobby/', views.hobby_list_view, name='hobby_list'),
    path('user-hobby/', views.user_hobby, name='user_hobby'),
    path('user-hobby/<int:user_hobby_id>/', views.user_hobby_api, name='user_hobby_detail'),

    path('friend-requests/', views.get_requests, name='friend_requests'),
    path('accept-friend-request/<int:user_id>/', views.accept_request, name='accept_request'),
    path('reject-friend-request/<int:user_id>/', views.reject_request, name='reject_request'),

    path('friends/', views.get_friends, name='friends'),
]
