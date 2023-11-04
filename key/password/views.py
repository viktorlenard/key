from django.shortcuts import render
from django.http import HttpResponse
from .utils import request_validator, password_generator, password_request
from django.contrib.auth.decorators import login_required

# Create your views here. Logic goes here.

def index(request):
    # @login_required
    request_validator(password_request)
    password = password_generator(password_request)

    return render(request, "password/index.html", {
        "password": password
    })

def login(request):
    return render(request, "password/login.html")

def register(request):
    return render(request, "password/register.html")

def about(request):
    return render(request, "password/about.html")