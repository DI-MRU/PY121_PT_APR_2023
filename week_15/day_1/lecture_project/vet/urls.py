from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
    path("owner/", views.owner, name="owner"),
    path("owner/register/", views.newOwner, name="owner_register"),
    path("pet/register/", views.newPet, name="pet_register"),
    path("pet/<int:pet_id>/", views.pet, name="pet"),
    path("dog/", views.dog, name="dog"),
]
