from django.db import models


class Medicine(models.Model):
    name = models.CharField(max_length=200, blank=True)
    price = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True)
    

class Prescription(models.Model):
    pet_id = models.ForeignKey('pet.Pet', on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField(blank=True, null=True)
    date_start = models.DateField(blank=True, null=True)
    date_end = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True)