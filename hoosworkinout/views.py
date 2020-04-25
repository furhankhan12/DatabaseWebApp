from django.urls import reverse
from django.views.generic import CreateView, TemplateView
from .models import Workout, User
from django.contrib.auth import logout

class HomePageView(TemplateView):
    template_name = 'hoosworkinout/home.html'

class ProfileView(TemplateView):
    template_name = 'hoosworkinout/profile.html'

class CreateUserView(CreateView):
    model = User
    fields = ('username', 'first_name', 'middle_name', 'last_name', 'phone', 'email', 'birthday', 'body_weight', 'best_lift')

class CreateWorkoutView(CreateView):
    model = Workout
    fields = ('username', 'comment', 'name', 'date')

class SignIn(TemplateView):
    template_name = 'hoosworkinout/signin.html'