from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType




class Stock(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    quantity = models.IntegerField()


#stock1 = Stock.objects.create(content_object=pet_product, quantity=10)  
#stock2 = Stock.objects.create(content_object=medicine, quantity=20) 