from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('profile/', views.MyProfileView.as_view(), name='profile'),
    path('new-workout/', views.NewWorkoutView.as_view(), name='new-workout'),
    path('add-strength-exercise/<int:wid>/', views.AddStrengthExerciseView.as_view(), name='add-strength-exercise'),
    path('add-cardio-exercise/<int:wid>/', views.AddCardioExerciseView.as_view(), name='add-cardio-exercise'),
    path('add-hiit-exercise/<int:wid>/', views.AddHIITExerciseView.as_view(), name='add-hiit-exercise'),
    path('add-exercise/<int:wid>/', views.AddExerciseView.as_view(), name='add-exercise'),
]
