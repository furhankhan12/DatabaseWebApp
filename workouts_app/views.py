from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  get_object_or_404, redirect
from django.views.generic import TemplateView

def index(request):
    return HttpResponse("Welcome to the Workout App")

class HomePageView(TemplateView):
    template_name = 'workouts_app/home.html'
