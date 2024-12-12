from datetime import datetime
import json
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render
from .models import User


def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})

# USER MODEL VIEWS

def user_list_view(request):
    """API endpoint for collection of users"""
    if request.method == 'GET':
        # getting all users
        return JsonResponse({
            'users': 
                [user.as_dict() for user in User.objects.all()]
        })
    elif request.method == 'POST':
        # adding a user
        return add_user(request)
    else:
        return HttpResponse(status=405)
    
def user_api(request, user_id):
    """API endpoint for a single user"""
    user = User.objects.get(id=user_id)
    if request.method == 'PUT':
        # updating a user
        return update_user(request, user_id)
    if request.method == 'DELETE':
        return delete_user(request, user_id)
    return JsonResponse(user.as_dict())

def add_user(request):
    """Add a user to the database"""
    try:
        data = json.loads(request.body)
        user = User.objects.create(
            name = data['name'],
            email = data['email'],
            date_of_birth = data['date_of_birth'],
            password = data['password']
        )
        return JsonResponse(user.as_dict())
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
def update_user(request, user_id):
    """Update a user's details in the database"""
    user = User.objects.get(id=user_id)
    try:
        data = json.loads(request.body)
        user.name = data.get('name', user.name)
        user.email = data.get('email', user.email)
        user.date_of_birth = data.get('date_of_birth', user.date_of_birth)
        user.password = data.get('password', user.password)
        user.save()
        return JsonResponse(user.as_dict())
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
def delete_user(request, user_id):
    """Delete a user from the database"""
    user = User.objects.get(id=user_id)
    user.delete()
    return JsonResponse({'message': 'User deleted successfully!'})


def login(request):
    """Log in an existing user, reject non-existing users"""
    

def register(request):
    """Register a new user"""
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        try:
            new_user = User(
                name=data['name'],
                email=data['email'],
                date_of_birth=datetime.strptime(data['dob'], '%Y-%m-%d')
            )
            new_user.set_password(data['pw'])
            new_user.save()
            return JsonResponse({'message': 'User registered successfully'}, status=200)
        except (KeyError, ValueError) as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': "Incorrect method"}, status=501)
