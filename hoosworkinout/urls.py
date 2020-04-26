"""hoosworkinout URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    # Admin and social urls
    path('admin/', admin.site.urls),
    url('', include('social_django.urls', namespace='social')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', auth_views.LoginView.as_view(), name='login'),

    # User views
    path('home/', views.HomeView.as_view(), name='home'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('edit-profile/', views.ProfileUpdate.as_view(), name='edit-profile'),
    path('new-workout/', views.CreateWorkoutView.as_view(), name='new-workout'),
    path('new-exercise/', views.CreateExerciseView.as_view(), name='new-exercise'),
    path('new-cardio-exercise/', views.CreateCardioExerciseView.as_view(), name='new-cardio-exercise'),
    path('new-strength-exercise/', views.CreateStrengthExerciseView.as_view(), name='new-strength-exercise'),
    path('new-hiit-exercise/', views.CreateHIITExerciseView.as_view(), name='new-hiit-exercise'),
    path('cardio/', views.CardioHelper.as_view(), name='cardio'),
    path('strength/', views.StrengthHelper.as_view(), name='strength'),
    path('hiit/', views.HIITHelper.as_view(), name='hiit'),
    path('new-plan/', views.CreatePlanView.as_view(), name='new-plan'),


]
