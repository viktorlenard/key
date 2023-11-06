from django.contrib.auth.forms import UserCreationForm # Django default creation form.
from django.contrib.auth.models import User # Django default user model.
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm
from .models import *


# Custom class, inheriting from the built in UserCreationForm. Created for customisation.
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]

class PasswordForm(forms.Form):
        password = forms.CharField(max_length=100)
        human = forms.BooleanField(initial=True)
        length = forms.IntegerField(validators=[
            MinValueValidator(3, message='Value must be at least 3.'),
            MaxValueValidator(8, message='Value must be at most 8.')
        ])
        div = forms.CharField(max_length=1)
        caps = forms.BooleanField(initial=False)
        nums = forms.BooleanField(initial=True)