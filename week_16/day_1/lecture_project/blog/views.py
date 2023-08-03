from django.shortcuts import render, HttpResponse
from django.views import generic

from blog.models import Author, Profile
from blog.forms import AuthorForm, ProfileForm

# Create your views here.

def home_page(request):
    # return HttpResponse("<html><body>Welcome to my blog.</body></html>")
    return render(request, "home_page.html")

class RegisterAuthor(generic.CreateView):
    template_name = 'register_author.html'
    form_class = AuthorForm

    def form_valid(self, form):
            author_to_add = form.cleaned_data
            return super().form_valid(form)

class CreateProfile(generic.CreateView):
    template_name = 'create_profile.html'
    form_class = ProfileForm

    def form_valid(self, form):
            profile_to_add = form.cleaned_data
            return super().form_valid(form)

class AllAuthors(generic.ListView):
    template_name = 'authors.html'
    model = Author

class AllProfiles(generic.ListView):
    template_name = 'profiles.html'
    context_object_name = 'profiles' 
    model = Profile

class DetailProfile(generic.DetailView):
    model = Profile
    template_name = 'profile_detail.html'
