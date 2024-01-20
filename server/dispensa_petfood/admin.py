from django.contrib import admin

# Register your models here.
from .models import PetProduct, Pet

admin.site.register(PetProduct)
admin.site.register(Pet)