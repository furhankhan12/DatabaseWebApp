import datetime
from django import template
from django.contrib.auth import views as auth_views

register = template.Library()

@register.simple_tag
def showUser():
    return request.user.get_full_name()