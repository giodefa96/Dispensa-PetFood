from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .models import Pet, PetProduct, Diet, Meal

class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

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
        

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ['food', 'quantity', 'feeding_time', 'diet', 'product']

    def create(self, validated_data):
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')
        product.quantity_in_stock -= quantity
        product.save()
        return super().create(validated_data)


class DietSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True)

    class Meta:
        model = Diet
        fields = ['pet', 'meals']

    def create(self, validated_data):
        meals_data = validated_data.pop('meals')
        diet = Diet.objects.create(**validated_data)
        for meal_data in meals_data:
            Meal.objects.create(diet=diet, **meal_data)
        return diet

