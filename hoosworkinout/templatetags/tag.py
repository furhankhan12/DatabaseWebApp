import datetime
from django import template

register = template.Library()

@register.simple_tag
def showUser():
    current_user = request.user
    return 'hi'