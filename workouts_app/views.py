from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  get_object_or_404, redirect
from django.views.generic import TemplateView

def index(request):
    return HttpResponse("Welcome to the Workout App")

class HomePageView(TemplateView):
    template_name = 'workouts_app/home.html'

class MyProfileView(TemplateView):
    template_name = 'workouts_app/profile.html'

class NewWorkoutView(TemplateView):
    template_name = 'workouts_app/new-workout.html'

class AddExerciseView(TemplateView):
    template_name = 'workouts_app/add-exercise.html'

class AddStrengthExerciseView(TemplateView):
    template_name = 'workouts_app/add-strength-exercise.html'

class AddCardioExerciseView(TemplateView):
    template_name = 'workouts_app/add-cardio-exercise.html'

class AddHIITExerciseView(TemplateView):
    template_name = 'workouts_app/add-hiit-exercise.html'

class OAuthCheckView(TemplateView):
    template_name = 'workouts_app/oauth-check.html'