from django.urls import reverse
from django.views.generic import CreateView, TemplateView, UpdateView
from .models import Workout, Profile, User
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(LoginRequiredMixin, TemplateView):
    template_name = 'hoosworkinout/home.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'hoosworkinout/profile.html'

class CreateUserView(LoginRequiredMixin, CreateView):
    model =  User
    fields = ('first_name', 'last_name', 'email')

class UserUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['user', 'birthday', 'body_weight', 'best_lift']
    template_name = 'hoosworkinout/user_form.html'
    def get_success_url(self):
        return reverse('home');



class CreateWorkoutView(CreateView):
    model = Workout
    fields = ('user', 'comment', 'name', 'date')
    def get_success_url(self):
        return reverse('home')

class CreateExerciseView(CreateView):
    model = Workout
    fields = ('username', 'comment', 'name', 'date')
    def get_success_url(self):
        return reverse('home')

def load_profile_page(request, uname):
    current_user = User.objects.filter(username = uname)
    current_workouts = Workout.objects.filter(username=uname)
    allUsers = User.objects.all()
    context = {
        "current_user" : current_user,
        "current_workouts" : current_workouts,
        "allProfiles" : allUsers,
        }
    return render(request, 'hoosworkinout/home.html', context)

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

        new_user.save()

    return redirect('/load_profile_page/'+username)
