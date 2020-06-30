from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path("", views.index, name="index"),
    path("auth/login/", views.login_user, name="login"),
    path("auth/register/", views.registerPage, name="register"),
    path("auth/logout/", views.logoutUser, name="logout"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("add_person/", views.addPerson, name="add_person"),
    path("update_person/<str:pk>", views.updatePerson, name="update_person"),
    path("delete/<str:pk>", views.deletePerson, name="delete"),


    path("reset_password/", auth_views.PasswordResetView.as_view(template_name='manageApp/reset_password.html'), name="reset_password"),
    path("reset_password/sent/", auth_views.PasswordResetDoneView.as_view(template_name='manageApp/email_sent.html'), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='manageApp/set-password.html'), name="password_reset_confirm"),
    path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(template_name='manageApp/reset_complete.html'), name="password_reset_complete"),
]
