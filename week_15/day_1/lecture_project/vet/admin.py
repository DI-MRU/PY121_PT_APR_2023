from django.contrib import admin
from .models import Owner, Pet, Tag, Nonsense

# Register your models here.
admin.site.register(Owner)
admin.site.register(Pet)
admin.site.register(Tag)
# admin.site.register(Nonsense)
