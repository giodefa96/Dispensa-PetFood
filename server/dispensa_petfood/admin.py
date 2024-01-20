from django.contrib import admin

# Register your models here.
from .models import PetProduct, Pet, Diet, Meal, MedicalRecord, Appointment

admin.site.register(PetProduct)
admin.site.register(Pet)
admin.site.register(Diet)
admin.site.register(Meal)
admin.site.register(MedicalRecord)
admin.site.register(Appointment)
