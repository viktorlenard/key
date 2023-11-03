from django.shortcuts import render
from django.http import HttpResponse
from utils import request_validator, password_generator, password_request

# Create your views here. Logic goes here.

def index(request):
    request_validator(password_request)
    password = password_generator(password_request)

    return render(request, "password/index.html", {
        "password": password
    })

def login(request):
    return render(request, "password/login.html")

def profile(request):
    return render(request, "password/profile.html")

def about(request):
    return render(request, "password/about.html")