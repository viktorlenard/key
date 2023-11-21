from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="password"),
    path('get_password/<int:password_id>', views.get_password, name='get_password'),
    path("login", views.login_page, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.register, name="register"),
    path("about", views.about, name="about")
]