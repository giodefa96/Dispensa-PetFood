from django.conf import settings
from django.db import models


User = settings.AUTH_USER_MODEL # auth.User


class Pet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    type = models.CharField(max_length=120)
    # add any other attribute for Pet here
    
    def __str__(self):
        return self.name
    
class PetProduct(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=99.99)
    # add any other attribute for PetProduct here
    
    def __str__(self):
        return self.name