import datetime as D
import json
from django.db.models import Count
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import authenticate, login, logout
from .models import User, Hobby, UserHobby


def main_spa(request: HttpRequest) -> HttpResponse:
    return render(request, 'api/spa/index.html', {})


# USER MODEL VIEWS


# def user_api(request: HttpRequest, user_id: int) -> HttpResponse: # TODO: Link up with frontend
#     """API endpoint for updating or deleting a single user"""
#     if request.method == 'PUT':
#         # updating a user
#         return update_user(request, user_id)
#     if request.method == 'DELETE':
#         return delete_user(request, user_id)


# def update_user(request: HttpRequest, user_id: int) -> HttpResponse: # TODO: Link up with frontend
#     """Update a user's details in the database"""
#     user = User.objects.get(id=user_id)
#     try:
#         data = json.loads(request.body)
#         user.name = data.get('name', user.name)
#         user.email = data.get('email', user.email)
#         user.date_of_birth = data.get('date_of_birth', user.date_of_birth)
#         user.password = data.get('password', user.password)
#         user.save()
#         return JsonResponse(user.as_dict())
#     except Exception as e:
#         return JsonResponse({'error': str(e)}, status=400)


# def delete_user(request: HttpRequest, user_id: int) -> HttpResponse: # TODO: Link up with frontend
#     """Delete a user from the database"""
#     user = User.objects.get(id=user_id)
#     user.delete()
#     return JsonResponse({'message': 'User deleted successfully!'})


@ensure_csrf_cookie
def log_in_view(request: HttpRequest) -> HttpResponse:
    """Log in an existing user, reject non-existing users"""
    if request.method == 'POST':
        if not request.POST['email'] or not request.POST['pw']:
            return render(request, 'api/spa/login.html',
                          {"error": "Please provide both username and password to log in"})
        try:
            user = authenticate(request, username=request.POST['email'], password=request.POST['pw'])
            if user:
                login(request, user=user)
                request.session["email"] = user.email
                response = redirect("http://localhost:5173/")
                response.set_cookie("email",
                                    user.email,
                                    expires=D.datetime.strftime(
                                        D.datetime.now() + D.timedelta(seconds=7 * 24 * 60 * 60),
                                        '%a, %d-%b-%Y %H:%M:%S GMT'
                                    ),
                                    httponly=True
                                    )
                return response
            else:
                # username or password is incorrect (authenticate failed, user is None)
                return render(request, 'api/spa/login.html', {"error": "Incorrect username or password"})
        except Exception as e:
            # catch and display any exceptions
            return render(request, 'api/spa/login.html', {"error": str(e)})
    if request.method == 'GET':
        return render(request, 'api/spa/login.html', {"error": ""})
    else:
        return JsonResponse({'error': "Incorrect method"}, status=501)


def log_out_view(request: HttpRequest) -> HttpResponse:
    """Handle logging out by flushing the session which deletes the session id cookie too and deleting the email cookie"""
    if request.method == "GET":
        logout(request)
        response = JsonResponse({'message': 'User logout successful.'}, status=200)
        response.delete_cookie("email")
        return response
    else:
        return JsonResponse({'error': "Incorrect method"}, status=501)


@ensure_csrf_cookie
def register(request: HttpRequest) -> HttpResponse:
    """Register a new user"""
    if request.method == 'POST':
        if not request.POST['name'] or not request.POST['email'] or not request.POST['dob'] or not request.POST['pw']:
            return render(request, 'api/spa/register.html', {"error": "Please fill in all fields to submit"})
        try:
            new_user = User(
                name=request.POST['name'],
                email=request.POST['email'],
                username=request.POST['email'],  # needs to be set, otherwise no new account creation will happen
                date_of_birth=D.datetime.strptime(request.POST['dob'], '%Y-%m-%d')
            )
            new_user.set_password(request.POST['pw'])
            new_user.save()
            return redirect("http://localhost:8000/login/")
        except Exception as e:
            return render(request, 'api/spa/register.html', {"error": str(e)})
    if request.method == 'GET':
        return render(request, 'api/spa/register.html', {"error": ""})
    else:
        return JsonResponse({'error': "Incorrect method"}, status=501)


def check_auth_status(request: HttpRequest) -> HttpResponse:
    """API endpoint that returns if there is a user logged in or not, and if there is returns the user info aswell"""
    if request.user.is_authenticated:
        # TODO: replace with a serializer
        return JsonResponse({'authenticated': True, 'user': request.user.as_dict()})
    return JsonResponse({'authenticated': False})


def paginate_users(request: HttpRequest, page_number: int) -> HttpResponse:
    """Return a paginated list of users ordered by the logged-in user's hobby list overlap with other users"""

    age_low = request.GET.get('age_low')
    age_high = request.GET.get('age_high')

    if request.method == 'GET':
        if request.user.is_authenticated:
            # exclude logged-in user
            people = User.objects.exclude(id=request.user.id).exclude(name=None) \
                .annotate(similar_hobbies=Count('hobbies', hobbies__in=request.user.hobbies.all())) \
                .order_by('-similar_hobbies')  # reverse order by similar_hobbies
            filtered_users = []
            for user in people:
                age = calculate_age_helper(user)
                if age_low and age < int(age_low):
                    continue
                if age_high and age > int(age_high):
                    continue
                filtered_users.append(user)
            paginator = Paginator(filtered_users, 10)  # Paginate the people QuerySet, 10 per page
            page = paginator.get_page(page_number)
            return JsonResponse({'page': {
                'current_page': page.number,
                'total_pages': paginator.num_pages,
                'total_users': paginator.count,
                'users': [
                    {
                        'id': user.id,
                        'name': user.name,
                        'age': calculate_age_helper(user),
                        'hobbies': [hobby.as_dict() for hobby in user.hobbies.all()],
                        'similar_hobbies': user.similar_hobbies
                    } for user in page
                ]
            }
            })
        else:
            return JsonResponse({'error': "User not logged in"}, status=401)
    else:
        return JsonResponse({'error': "Incorrect method"}, status=405)


def calculate_age_helper(user: User) -> int:
    if not user.date_of_birth:
        return 0
    today = D.datetime.today()
    age = today.year - user.date_of_birth.year
    if (today.month, today.day) < (user.date_of_birth.month, user.date_of_birth.day):
        age -= 1
    return age


# HOBBY MODEL VIEWS


def hobby_list_view(request: HttpRequest) -> HttpResponse:
    """API endpoint for collection of hobbies"""
    if request.method == 'GET':
        # getting all hobbies
        hobbies = Hobby.objects.all().values('id', 'name')  # Fetching all hobbies
        return JsonResponse({'hobbies': list(hobbies)})
    else:
        return JsonResponse({'error': "Incorrect method"}, status=405)


# USER-HOBBY RELATIONSHIP VIEWS


def user_hobby(request: HttpRequest) -> HttpResponse:
    """Add to the logged-in user's hobby list"""
    if request.method == 'POST':
        try:
            if request.user.is_authenticated:  # Ensure the user is authenticated
                data = json.loads(request.body)
                # Get the Hobby instance (ignoring the boolean flag)
                hob, _ = Hobby.objects.get_or_create(name=data['name'])

                # If the user-hobby relationship already exists, return an error
                if UserHobby.objects.filter(user=request.user, hobby=hob).exists():
                    print("User-hobby relationship already exists")
                    return JsonResponse({'error': 'User-hobby relationship already exists'}, status=400)

                UserHobby.objects.create(
                    user=request.user,
                    hobby=hob
                )
                return JsonResponse({'message': "Hobby added successfully"}, status=201)
            else:
                return JsonResponse({'error': "User not logged in"}, status=401)
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': "Incorrect method"}, status=501)


def user_hobby_api(request: HttpRequest, user_hobby_id: int) -> HttpResponse:
    """API endpoint for deleting a single user-hobby relationship"""
    if request.method == 'DELETE':
        try:
            # Ensure the user is authenticated
            if not request.user.is_authenticated:
                return JsonResponse({'error': 'User not authenticated'}, status=401)
            # Find the user-hobby relationship where the hobby has the given ID
            user_hobby = UserHobby.objects.filter(user=request.user, hobby_id=user_hobby_id)
            if not user_hobby.exists():
                return JsonResponse({'error': 'User-hobby relationship not found'}, status=404)
            # Delete the relationship
            user_hobby.delete()
            return JsonResponse({'message': 'User-hobby relationship deleted successfully!'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': "Incorrect method"}, status=501)
