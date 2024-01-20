from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL # auth.User


class Pet(models.Model):  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    name = models.CharField(max_length=200)  
    type = models.CharField(max_length=200)  
    breed = models.CharField(max_length=200)  
    age = models.IntegerField()  
    weight = models.DecimalField(max_digits=5, decimal_places=2)  
    special_care = models.BooleanField(default=False)  
  
    def __str__(self):  
        return self.name  
    
class PetProduct(models.Model):  
    name = models.CharField(max_length=200)  
    price = models.DecimalField(max_digits=5, decimal_places=2)  
    description = models.TextField()  
    quantity_in_stock = models.IntegerField()  
  
    def __str__(self):  
        return self.name
    

class Appointment(models.Model):  
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)  
    date = models.DateField()  
    time = models.TimeField()  
    reason = models.CharField(max_length=200)  
  
    def __str__(self):  
        return f"Appointment for {self.pet.name} on {self.date}"  


class MedicalRecord(models.Model):  
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)  
    date = models.DateField()  
    details = models.TextField()  
  
    def __str__(self):  
        return f"Medical record for {self.pet.name} on {self.date}" 


class Diet(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    def __str__(self):
        return f"Diet for {self.pet.name}"
    

class Meal(models.Model):
    diet = models.ForeignKey(Diet, related_name='meals', on_delete=models.CASCADE)
    product = models.ForeignKey(PetProduct, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    feeding_time = models.TimeField()

    def __str__(self):
        return f"Meal for {self.diet.pet.name} at {self.feeding_time}"


