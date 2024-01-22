from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models.pet_product import PetProduct

#def validate_title(value):
#    qs = PetProduct.objects.filter(title__iexact=value)
#    if qs.exists():
#        raise serializers.ValidationError(f"{value} already exists")
#    return value

def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationError("Hello is not allowed")
    return value

unique_product_title = UniqueValidator(queryset=PetProduct.objects.all(),
                                       lookup='iexact',
                                       message="This title already exists")