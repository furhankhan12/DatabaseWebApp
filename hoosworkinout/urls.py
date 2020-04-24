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
from django.contrib.auth import logout, login
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('oauth/', views.OAuthCheckView.as_view(), name='oauth_check'),
    url('', include('social_django.urls')),
    path('', views.SignIn.as_view(), name='signin'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('profile/', views.MyProfileView.as_view(), name='profile'),

    path('edit-profile/', views.CreateUserView.as_view(), name='edit-profile'),
    path('new-workout/', views.CreateWorkoutView.as_view(), name='new-workout'),
    # path('add-strength-exercise/<int:wid>/', views.AddStrengthExerciseView.as_view(), name='add-strength-exercise'),
    # path('add-cardio-exercise/<int:wid>/', views.AddCardioExerciseView.as_view(), name='add-cardio-exercise'),
    # path('add-hiit-exercise/<int:wid>/', views.AddHIITExerciseView.as_view(), name='add-hiit-exercise'),
    path('add-exercise/<int:wid>/', views.AddExerciseView.as_view(), name='add-exercise'),
]
