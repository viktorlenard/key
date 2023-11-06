from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import request_validator, password_generator, password_request
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import CreateUserForm

@login_required(login_url='login') # User must be logged in. If not, redirect them to 'login'.
def index(request):
    request_validator(password_request)
    password = password_generator(password_request)

    return render(request, "password/index.html", {
        "password": password
    })

def login_page(request):  
    if request.user.is_authenticated: # If out user is logged in, redicet them to 'password'.
        return redirect('password')
    else:
        if request.method == 'POST': 
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None: 
                login(request, user)
                return redirect('password')
            else:
                messages.info(request, 'Username or password is incorrect.')

        return render(request, "password/login.html")


# Log user out. Redirect to 'login'.
def logout_user(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.user.is_authenticated: # If out user is logged in, redicet them to 'password'.
        return redirect('password')
    else:
        reg_form = CreateUserForm() # Get an object of out custom class.
        if request.method == 'POST':
            reg_form = CreateUserForm(request.POST) # Store POST data in our form.
            if reg_form.is_valid(): # Validate the form.
                reg_form.save() # Save the form, crateing the user.
                user = reg_form.cleaned_data.get('username') # Get the username, pass that with a message for feedback.
                messages.success(request, 'Account was created ' + user)
                return redirect('login')

        # Sending our reg_form to be filled out.
        return render(request, "password/register.html", {
            "reg_form": reg_form
        })

def about(request):
    return render(request, "password/about.html")