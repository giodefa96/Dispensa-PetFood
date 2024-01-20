from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserProductInlineSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk',
        read_only=True
    )
    title = serializers.CharField(read_only=True)
   

class UserPublicSerializer(serializer.Serializer):
    username = serializers.CharField(red_only=True)
    id = serializers.IntegerField(red_only=True)
    #other_products = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = User
        fields = [
            'username',
            'this_is_not_real',
            'id'
            #'other_products'
        ]
    #
    #def get_other_products(self, obj):
    #    request = self.context.get('request')
    #    print(obj, flush=True)
    #    user = obj
    #    my_products_qs = user.product_set.all()[:5]
    #    return UserProductInlineSerializer(my_products_qs,
    #                                       many=True,
    #                                       context=self.context).data