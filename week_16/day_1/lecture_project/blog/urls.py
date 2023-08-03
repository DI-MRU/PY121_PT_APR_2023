from django.contrib import admin
from django.urls import include, path
from . import views


urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("register_author", views.RegisterAuthor.as_view(), name="register_author"),
    path("create_profile", views.CreateProfile.as_view(), name="create_profile"),
    path("authors/", views.AllAuthors.as_view(), name="all_authors"),
    path("profiles/", views.AllProfiles.as_view(), name="all_profiles"),
    path("profiles/<int:pk>", views.DetailProfile.as_view(), name="detail_profile")
    # path(".jpg", uploaded_images),
    # path(".png"),
    # path(".PNG")
]
