from django.db import models


class PetProduct(models.Model):
    product_name = models.CharField(max_length=200, blank=True)
    price = models.FloatField(blank=True, null=True)
    description = models.TextField(blank=True)