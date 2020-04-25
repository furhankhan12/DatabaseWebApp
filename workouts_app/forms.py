from django.forms import ModelForm

from .models import User

class NewProfileForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'middle_name', 'last_name', 'phone', 'email', 'birthday', 'body_weight', 'best_lift'];
