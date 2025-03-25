from django.urls import path

from . import views

app_name = "checkdeploy"
urlpatterns = [
    path("", views.index, name="index"),
    path("run", views.run, name="run"),
]