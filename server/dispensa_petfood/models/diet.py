from django.db import models


class Diet(models.Model):
    diet_name = models.CharField(max_length=200, blank=True)
    pet_id = models.ForeignKey('pet.Pet', on_delete=models.CASCADE)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)


class Meal(models.Model):
    diet_id = models.ForeignKey(Diet, on_delete=models.CASCADE)
    product_id = models.ForeignKey('pet_product.PetProduct', on_delete=models.CASCADE)
    meal_time = models.DateTimeField(blank=True, null=True)
    meal_description = models.TextField(blank=True)
    meal_photo = models.ImageField(upload_to='images/', blank=True)