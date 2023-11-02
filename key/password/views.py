from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, "password/index.html")

def login(request):
    return render(request, "password/login.html")

def profile(request):
    return HttpResponse("User profile page")

def about(request):
    return HttpResponse("About page")