from django.contrib.auth.forms import UserCreationForm # Django default creation form.
from django.contrib.auth.models import User # Django default user model.
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