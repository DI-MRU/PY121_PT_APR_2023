from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("homepage", views.homepage, name="homepage"),
    path("about_website", views.about, name="about_website"),
    path("profile", views.profile, name="user_profile"),
]
