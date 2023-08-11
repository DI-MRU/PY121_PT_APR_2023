from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import test_view, ImageProfileSubmit, RegisterView

urlpatterns = [
    # path("", include("django.contrib.auth.urls")),
    # re_path(r"^accounts/login/$", views.LoginView.as_view(), name="login"),
    # re_path(r"^accounts/logout/$", views.LogoutView.as_view(), name="logout"),
    # re_path(
    #     r"^accounts/password_change/$",
    #     views.PasswordChangeView.as_view(),
    #     name="password_change",
    # ),
    # --- Customized views ----
    path(
        "login/",
        LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "logout/",
        LogoutView.as_view(template_name="registration/logout.html"),
        name="logout",
    ),
    path("test/", test_view, name="test_view"),
    path("register_image/", ImageProfileSubmit.as_view(), name="register_image"),
    path("register/", RegisterView.as_view(), name="register_user"),
]
