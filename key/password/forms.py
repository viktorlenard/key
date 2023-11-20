from django.contrib.auth.forms import UserCreationForm # Django default creation form.
from django.contrib.auth.models import User # Django default user model.
from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from django.forms import ModelForm
from .models import *
from .utils import password_generator, request_validator

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

class AddPasswordForm(forms.Form):
    name = forms.CharField(max_length=64)
    url = forms.CharField(max_length=64)
    username = forms.CharField(max_length=1000)
    password = forms.CharField(max_length=1000)
    tags = forms.ChoiceField(choices=[
        ('blue', 'Blue'),
        ('red', 'Red'),
        ('green', 'Green'),
        ('yellow', 'Yellow'),
        ('purple', 'Purple'),
    ], required=False)
    comment = forms.CharField(max_length=1000, required=False)

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        if 'password' in initial:
            self.base_fields['password'].initial = initial['password']
        super(AddPasswordForm, self).__init__(*args, **kwargs)


# Designed to handle adding passwords to the db.
class GeneratePasswordForm(forms.Form):
    human = forms.BooleanField(initial=True, required=False)
    length = forms.IntegerField(validators=[
        MinValueValidator(3, message='Value must be at least 3.'),
        MaxValueValidator(8, message='Value must be at most 8.')
    ])
    div = forms.CharField(max_length=1)
    caps = forms.BooleanField(initial=False, required=False)
    nums = forms.BooleanField(initial=True, required=False)