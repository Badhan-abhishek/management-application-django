from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("auth/login/", views.login_user, name="login"),
    path("auth/register/", views.registerPage, name="register"),
    path("auth/logout/", views.logoutUser, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
]
