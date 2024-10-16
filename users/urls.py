from . import views
from django.urls import path
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("register/", views.user_register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path("logout/", views.user_logout, name="logout"),
    path("profile/", views.profile, name="profile"),
]
