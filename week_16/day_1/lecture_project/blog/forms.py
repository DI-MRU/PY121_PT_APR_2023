from django.forms import ModelForm
from blog.models import Author, Profile

class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = "__all__"

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
