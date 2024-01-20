from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .models import Pet, PetProduct

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    
    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email']
        )
        
        user.set_password(validated_data['password'])
        user.save()
        
        return user

class PetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Pet
        fields = ['id', 'user', 'name', 'type']

class PetProductSerializer(serializers.ModelSerializer):
    pet = PetSerializer(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='pk'
    )
    class Meta:
        model = PetProduct
        fields = ['id', 'pet', 'name', 'price', 'url']
