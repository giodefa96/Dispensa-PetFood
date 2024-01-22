from django.contrib import admin

# Register your models here.
from .models import clinic, medicine, veterinarian, pet, pet_product, diet, stock

admin.site.register(clinic.Clinic)
admin.site.register(clinic.OpeningHours)
admin.site.register(veterinarian.Veterinarian)
admin.site.register(veterinarian.VeterinarianSchedule)
admin.site.register(medicine.Medicine)
admin.site.register(medicine.Prescription)
admin.site.register(pet.Pet)
admin.site.register(pet.Vaccination)
admin.site.register(pet_product.PetProduct)
admin.site.register(diet.Diet)
admin.site.register(diet.Meal)
admin.site.register(stock.Stock)
