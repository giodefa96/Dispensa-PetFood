from rest_framework import serializers
from rest_framework.reverse import reverse
from django.contrib.auth.models import User
from .models.pet import Pet
from .models.pet_product import PetProduct
from .models.diet import Diet, Meal


class UserSerializer(serializers.ModelSerializer):
    
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        
        
class PetSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = Pet  
        fields = ['id', 'name', 'type', 'breed', 'age', 'weight', 'special_care']
  
    def create(self, validated_data):  
        # Pop the user from validated_data and create the Pet with the remaining data  
        user = validated_data.pop('user')  
        pet = Pet.objects.create(user=user, **validated_data)  
        pet.save()  
        return pet   


class PetProductSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = PetProduct  
        fields = ['id', 'name', 'price', 'description', 'quantity_in_stock']  
        

class MealSerializer(serializers.ModelSerializer):
    class Meta:  
        model = Meal  
        fields = ['product', 'quantity', 'feeding_time', 'diet']

    def create(self, validated_data):
        product = validated_data.get('product')
        quantity = validated_data.get('quantity')
        product.quantity_in_stock -= quantity
        product.save()
        return super().create(validated_data)


class DietSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True)
    pet = PetSerializer(read_only=True)  
    class Meta:
        model = Diet
        fields = ['pet', 'meals']

    def create(self, validated_data):
        meals_data = validated_data.pop('meals')
        diet = Diet.objects.create(**validated_data)
        for meal_data in meals_data:
            Meal.objects.create(diet=diet, **meal_data)
        return diet
