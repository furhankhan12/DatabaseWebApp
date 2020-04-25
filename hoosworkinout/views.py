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
    get_email = request.user.email
    at_symbol_index = get_email.find('@')
    username = get_email[:at_symbol_index]
    return redirect('/profile/'+username)

def logout_user(request):
    logout(request)
    return redirect('/oauth/')
