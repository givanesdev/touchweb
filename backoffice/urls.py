from django.urls import path

from . import views

app_name = "backoffice"

urlpatterns = [
    path("", views.AccountView.as_view(), name="index"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.LogoutView.as_view(), name="logout")
]
