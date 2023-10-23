from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Index page")

def login(request):
    return HttpResponse("Login page")

def profile(request):
    return HttpResponse("User profile page")

def about(response):
    return HttpResponse("About page")