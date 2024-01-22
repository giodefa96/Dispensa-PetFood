from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL # auth.User


class Agend(models.Model):
    user_id = models.OneToOneRel(User, on_delete=models.CASCADE)
    pet_id = models.ForeignKey('pet.Pet', on_delete=models.CASCADE)
    

class Appointment(models.Model):
    agend_id = models.ForeignKey(Agend, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.CharField(max_length=200)
    status = models.CharField(max_length=200)
    description = models.TextField(blank=True)
