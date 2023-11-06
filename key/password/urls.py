from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="password"),
    path("login", views.login_page, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.register, name="register"),
    path("about", views.about, name="about")
]