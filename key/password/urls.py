from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="password"),
    path("login", views.login, name="login"),
    path("profile", views.profile, name="profile"),
    path("about", views.login, name="about")
]