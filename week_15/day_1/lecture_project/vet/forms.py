from django import forms
from .models import Pet, Owner

class PetForm(forms.ModelForm):
    class Meta:      
        model = Pet
        fields = "__all__"
        # exclude = ["name", "age"]
    
        # To customize our input fields
        widgets = {
            'name': forms.Textarea(attrs={'class': 'textarea'}),
            'owner': forms.Textarea(attrs={'class': 'textarea'}), # Please don't do this, you are overriding the select
        }

class OwnerForm(forms.ModelForm):
    class Meta:
        model = Owner
        fields = "__all__"