from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import PetProduct
from . import validators

class PetProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    title = serializers.CharField(required=True,
                                  validators=[validators.validate_title_no_hello,
                                              validators.unique_product_title])
    name = serializers.CharField(source='title', read_only=True)
    class Meta:
        model = PetProduct
        fields = [
            'user',
            'url',
            'edit_url',
            'pk',
            'title',
            'name',
            'content',
            'price',
            "sale_price",
            "my_discount"
        ]
        
    #def validate_title(self, value):
    #    request = self.context.get('request')
    #    user = request.user
    #    qs = PetProduct.objects.filter(user=user, title__iexact=value)
    #    if qs.exists():
    #        raise serializers.ValidationError(f"{value} already exists")
    #    return value
    
    #def create(self, validated_data):
    #    #return PetProduct.objects.create(**validated_data)
    #    #email = validated_data.pop("email")
    #    obj = super().create(validated_data)
    #    print("obj", obj, flush=True)
    #    #print("email", email, flush=True)
    #    return obj
    
    #def update(self, instance, validated_data):
    #    email = validated_data.pop("email")
    #    return super().update(instance, validated_data)
    
    def get_edit_url(self, obj):
        #return f"/api/dispensa_pet_food/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
    
    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None