from django.db import models
from django.shortcuts import reverse

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    
    def get_absolute_url(self):
        return reverse('create_profile') 

class Profile(models.Model):
    avatar = models.ImageField(upload_to="./uploaded_images/", max_length=150)
    description = models.CharField(max_length=500)
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
