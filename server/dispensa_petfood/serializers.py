from rest_framework import serializers

from .models import PetProduct

class PetProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = PetProduct
        fields = [
            'title',
            'content',
            'price',
            "sale_price",
            "my_discount"
        ]
    def get_my_discount(self, obj):
        try:
            return obj.get_discount()
        except:
            return None