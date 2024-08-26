"""
User management URL dispatcher.

login: User login.
logout: User logout.
register: User registration.
"""
from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

app_name = "users"
urlpatterns = [
    path("login/", views.UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", views.UserRegistrationView.as_view(), name="register"),
]
