from django.urls import path
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url('', views.HomePageView.as_view(), name='home'),
    path('', views.index, name='index'),
]
