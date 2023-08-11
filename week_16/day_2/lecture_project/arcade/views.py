from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.contrib.auth import get_user_model
from django.views import View
from .forms import ImageProfileForm, UserProfileForm, UserForm


# Create your views here.


def test_view(request):
    if not request.user.is_authenticated:
        return redirect("%s?next=%s" % (settings.LOGIN_URL, request.path))
    else:
        return render(request, "test.html")


class ImageProfileSubmit(View):
    def get(self, request, *args, **kwargs):
        context = {
            "user": {
                "is_authenticated": request.user.is_authenticated,
                "username": request.user.email,
            },
            "form": ImageProfileForm(),
        }
        print(request.user)
        return render(request, "register_image.html", context)

    def post(self, request, *args, **kwargs):
        form = ImageProfileForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = request.user
            image.save()
            return redirect("profile")
        return render(
            request,
            "register_image.html",
            {
                "user": {
                    "is_authenticated": request.user.is_authenticated,
                    "username": request.user.email,
                },
                "form": form,
            },
        )


User = get_user_model()


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        # define the 2 forms
        user_form = UserForm()
        profile_form = UserProfileForm()
        # GET, generate blank form
        return render(
            request,
            "register.html",
            {"user_form": user_form, "profile_form": profile_form},
        )

    def post(self, request, *args, **kwargs):
        # define the 2 forms
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        # check if the 2 forms are valid:
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect("index")
        return render(
            request,
            "register.html",
            {"user_form": user_form, "profile_form": profile_form},
        )
