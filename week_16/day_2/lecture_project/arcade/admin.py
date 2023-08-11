from django.contrib import admin
from .models import UserProfile, CustomUser, ImageProfile

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(CustomUser)
admin.site.register(ImageProfile)
