from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import  get_object_or_404, redirect

from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from .models import Workout, User
from django.contrib.auth import logout


def index(request):
    return HttpResponse("Welcome to the Workout App")

class HomePageView(TemplateView):
    template_name = 'hoosworkinout/home.html'

class MyProfileView(TemplateView):
    template_name = 'hoosworkinout/profile.html'

def load_profile_page(request, uname):
        current_user = User.objects.filter(username = uname)
        allUsers = User.objects.all()
        context = {
            "current_user" : current_user,
            "allProfiles" : allUsers,
            }
        return render(request, 'hoosworkinout/profile.html', context)

class CreateUserView(CreateView):
    model = User
    fields = ('username', 'first_name', 'middle_name', 'last_name', 'phone', 'email', 'birthday', 'body_weight', 'best_lift')

class CreateWorkoutView(CreateView):
    model = Workout
    fields = ('username', 'comment', 'name', 'date')

class AddExerciseView(TemplateView):
    template_name = 'hoosworkinout/add-exercise.html'

class OAuthCheckView(TemplateView):
    template_name = 'hoosworkinout/oauth-check.html'

class SignIn(TemplateView):
    template_name = 'hoosworkinout/signin.html'

def authenticate(request):
 #Check to see if this is a new user
    #If it is, create a new user model and save it to the database

    get_email = request.user.email
    at_symbol_index = get_email.find('@')
    username = get_email[:at_symbol_index]

    initialized = False
    all_users = User.objects.all()

    for user in all_users:
        if user.username == username:
            initialized = True
    if initialized == False:
        new_user = User(username, 'first_name', 'middle_name', 'last_name', 'phone', 'email', '2000-01-01', 0.0, 0)
        new_user.save()

    return redirect('/load_profile_page/'+username)


def logout_user(request):
    logout(request)
    return redirect('/oauth/')

def logout_user(request):
    logout(request)
    return redirect('/signin/')
