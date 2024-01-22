from django.db import models


class Pet(models.Model):
    pet_name = models.CharField(max_length=200, blank=True)
    pet_owner = models.ForeignKey('user.User', on_delete=models.CASCADE)
    pet_breed = models.CharField(max_length=200, blank=True)
    pet_birth_date = models.DateField(blank=True, null=True)
    pet_description = models.TextField(blank=True)
    pet_photo = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.pet_name


class HistoricalPetCondition(models.Model):
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    weight = models.FloatField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    pet_description = models.TextField(blank=True)
    date = models.DateField(blank=True, null=True)


class Vaccination(models.Model):
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    vaccine_name = models.CharField(max_length=200, blank=True)
    vaccine_date = models.DateField(blank=True, null=True)
    vaccine_description = models.TextField(blank=True)