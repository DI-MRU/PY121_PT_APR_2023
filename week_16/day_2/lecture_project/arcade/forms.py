from django.forms import ModelForm
from django.db import models
from .models import ImageProfile, CustomUser, UserProfile
from django.contrib.auth import get_user_model

User = get_user_model()


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password"]


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ["birth_date", "has_pet", "number_pet"]


class ImageProfileForm(ModelForm):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    class Meta:
        model = ImageProfile
        fields = "__all__"
