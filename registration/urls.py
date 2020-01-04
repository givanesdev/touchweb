from django.urls import path

app_name = "registration"

from . import views

urlpatterns = [
    path("", views.IndexPage.as_view(), name="index")
]
