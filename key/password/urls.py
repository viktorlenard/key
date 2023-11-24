from django.urls import path
from . import views

'''get_password/<int:password_id>
This is a path will change dependent on which password entry the user clicks on.
The URL should containt the password_id. Returns the get_password view.'''

urlpatterns = [
    path("", views.index, name="password"),
    path('get_password/<int:password_id>', views.get_password, name='get_password'),
    path('delete_password/<int:password_id>', views.delete_password, name='delete_password'),
    path("login", views.login_page, name="login"),
    path("logout", views.logout_user, name="logout"),
    path("register", views.register, name="register"),
    path("about", views.about, name="about")
]