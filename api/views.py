import datetime as D
import json
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from .models import User
from django.views.decorators.csrf import ensure_csrf_cookie
from django.shortcuts import render
from .models import User, Hobby, UserHobby

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


@ensure_csrf_cookie
def login(request: HttpRequest) -> HttpResponse:
    """Log in an existing user, reject non-existing users"""
    if request.method == 'POST':
        try:
            user_login = User.objects.get(email=request.POST['email'])
            if user_login.check_password(request.POST['pw']):
                request.session["email"] = user_login.email
                response = redirect("http://localhost:5173/")
                response.set_cookie("email", 
                                    user_login.email, 
                                    expires= D.datetime.strftime(
                                                                D.datetime.now() + D.timedelta(seconds=7*24*60*60),
                                                                '%a, %d-%b-%Y %H:%M:%S GMT'
                                                            ),
                                    httponly=True
                                    )
                return response
            else:
                return render(request, 'api/spa/login.html', {})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    if request.method == 'GET':
        return render(request, 'api/spa/login.html', {})
    else:
        return JsonResponse({'error': "Incorrect method"}, status=501)
    

def logout(request: HttpRequest) -> HttpResponse:
    """Handle logging out by flushing the session which deletes the session id cookie too and deleting the email cookie"""
    if request.method == "GET":
        request.session.flush()
        response = JsonResponse({'message': 'User logout successful.'}, status=200)
        response.delete_cookie("email")
        return response
    else:
        return JsonResponse({'error': "Incorrect method"}, status=501)


@ensure_csrf_cookie
def register(request: HttpRequest) -> HttpResponse:
    """Register a new user"""
    if request.method == 'POST':
        try:
            new_user = User(
                name=request.POST['name'],
                email=request.POST['email'],
                username=request.POST['email'], # needs to be set, otherwise no new account creation will happen
                date_of_birth=D.datetime.strptime(request.POST['dob'], '%Y-%m-%d')
            )
            new_user.set_password(request.POST['pw'])
            new_user.save()
            return redirect("http://localhost:8000/login/")
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    if request.method == 'GET':
        return render(request, 'api/spa/register.html', {})
    else:
        return JsonResponse({'error': "Incorrect method"}, status=501)

# HOBBY MODEL VIEWS

def hobby_list_view(request):
    """API endpoint for collection of hobbies"""
    if request.method == 'GET':
        # getting all hobbies
        return JsonResponse({
            'hobbies': 
                [hobby.as_dict() for hobby in Hobby.objects.all()]
        })
    elif request.method == 'POST':
        # adding a hobby
        return add_hobby(request)
    else:
        return HttpResponse(status=405)
    
def hobby_api(request, hobby_id):
    """API endpoint for a single hobby"""
    hobby = Hobby.objects.get(id=hobby_id)
    if request.method == 'PUT':
        # updating a hobby
        return update_hobby(request, hobby_id)
    if request.method == 'DELETE':
        return delete_hobby(request, hobby_id)
    return JsonResponse(hobby.as_dict())

def add_hobby(request):
    """Add a hobby to the database"""
    try:
        data = json.loads(request.body)
        hobby = Hobby.objects.create(
            name = data['name'],
            description = data['description']
        )
        return JsonResponse(hobby.as_dict())
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
def update_hobby(request, hobby_id):
    """Update a hobby's details in the database"""
    hobby = Hobby.objects.get(id=hobby_id)
    try:
        data = json.loads(request.body)
        hobby.name = data.get('name', hobby.name)
        hobby.description = data.get('description', hobby.description)
        hobby.save()
        return JsonResponse(hobby.as_dict())
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
def delete_hobby(request, hobby_id):
    """Delete a hobby from the database"""
    hobby = Hobby.objects.get(id=hobby_id)
    hobby.delete()
    return JsonResponse({'message': 'Hobby deleted successfully!'})

# USER-HOBBY RELATIONSHIP VIEWS

def user_hobby_list_view(request):
    """API endpoint for collection of user-hobby relationships"""
    if request.method == 'GET':
        # getting all user-hobby relationships
        return JsonResponse({
            'user_hobbies': 
                [user_hobby.as_dict() for user_hobby in UserHobby.objects.all()]
        })
    elif request.method == 'POST':
        # adding a user-hobby relationship
        return add_user_hobby(request)
    else:
        return HttpResponse(status=405)
    
def user_hobby_api(request, user_hobby_id):
    """API endpoint for a single user-hobby relationship"""
    user_hobby = UserHobby.objects.get(id=user_hobby_id)
    #if request.method == 'PUT':
        # updating a user-hobby relationship
    #    return update_user_hobby(request, user_hobby_id)
    if request.method == 'DELETE':
        return delete_user_hobby(request, user_hobby_id)
    return JsonResponse(user_hobby.as_dict())

def add_user_hobby(request):
    """Add a user-hobby relationship to the database"""
    try:
        data = json.loads(request.body)

        # get user and hobby objects from the database
        user = User.objects.get(id=data['user_id'])
        hobby = Hobby.objects.get(id=data['hobby_id'])

        user_hobby = UserHobby.objects.create(
            user = user,
            hobby = hobby
        )
        return JsonResponse(user_hobby.as_dict())
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
    
def delete_user_hobby(request, user_hobby_id):
    """Delete a user-hobby relationship from the database"""
    user_hobby = UserHobby.objects.get(id=user_hobby_id)
    user_hobby.delete()
    return JsonResponse({'message': 'User-hobby relationship deleted successfully!'})