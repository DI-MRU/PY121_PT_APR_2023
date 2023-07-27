from django.db import models


# Create your models here.
class Owner(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    number_of_pets = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Pet(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    color = models.CharField(max_length=40)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} is {self.age}yo and {self.color} color with owner {self.owner}"

class Tag(models.Model):
    label = models.CharField(max_length=30)
    pet = models.ManyToManyField(Pet, related_name='tags', blank=True)

    def __str__(self):
        return f"{self.label}"

    # def clean_tag(self, tag_id):
    #     Tag.objects.filter(id=tag_id)

class Nonsense(models.Model):
    label = models.CharField(max_length=30)