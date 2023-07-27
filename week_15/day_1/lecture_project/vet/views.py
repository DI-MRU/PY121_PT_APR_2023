from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404

from .forms import OwnerForm, PetForm
from .models import Nonsense, Owner, Pet

# Create your views here.


def owner(request):
    owners = Owner.objects.all()
    for owner in owners:
        pets = Pet.objects.filter(owner=owner)
        owner.pets = pets

    context = {'owners': owners}

    return render(request, "owner.html", context)

def pet(request, pet_id):
    # nonsense = get_list_or_404(Nonsense, label="dfkjghdkfjl")

    # pet = Pet.objects.filter(id=pet_id).first()
    pet = get_object_or_404(Pet, id=pet_id)
    context = {'pet': pet, 'tags': pet.tags.all()}

    return render(request, "pet.html", context)

def newPet(request):
    context = {}

    if request.method == 'POST':
        form = PetForm(request.POST)
        if form.is_valid():
            pet_name = form.cleaned_data['name']
            pet_age = form.cleaned_data['age']
            pet_color = form.cleaned_data['color']
            pet_owner = form.cleaned_data['owner']

            new_pet = Pet(
                name=pet_name,
                age=pet_age,
                color=pet_color,
                owner=pet_owner
            )
            new_pet.save()

            # new_pet = Pet.objects.create(
            #     name=pet_name,
            #     age=pet_age,
            #     color=pet_color,
            #     owner=pet_owner
            # )

            return redirect('pet', pet_id=new_pet.id)
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'new_pet.html', context)
    else:
        context['form'] = PetForm()
        return render(request, 'new_pet.html', context)

def newOwner(request):
    context = {}

    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            owner_first_name = form.cleaned_data['first_name']
            owner_last_name = form.cleaned_data['last_name']
            owner_number_of_pets = form.cleaned_data['number_of_pets']

            new_owner = Owner.objects.create(
                first_name=owner_first_name,
                last_name=owner_last_name,
                number_of_pets=owner_number_of_pets,
            )

            return redirect('owner')
        else:
            print("---ERRORS---", form.errors)
            context['form'] = form
            return render(request, 'new_owner.html', context)
    else:
        context['form'] = OwnerForm()
        return render(request, 'new_owner.html', context)

def dog(request):
    return redirect("pet", pet_id=1)