from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication  

from django.contrib.auth.models import User
from django.contrib.auth import get_user_model  

from .models.pet_product import PetProduct
from .models.pet import Pet
from .models.diet import Diet, Meal
from .serializers import UserSerializer, PetSerializer, PetProductSerializer, DietSerializer, MealSerializer


class UserList(generics.ListCreateAPIView):    
    serializer_class = UserSerializer    
    authentication_classes = [TokenAuthentication]    
    permission_classes = [permissions.IsAuthenticated]  
  
    def get_queryset(self):  
        user = self.request.user  
        if user.is_staff:  
            return get_user_model().objects.all()  
        return get_user_model().objects.filter(id=user.id) 


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PetList(generics.ListCreateAPIView):
    serializer_class = PetSerializer
    authentication_classes = [TokenAuthentication]    
    permission_classes = [permissions.IsAuthenticated] 
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Pet.objects.all()
        return Pet.objects.filter(user=user)
    
    def perform_create(self, serializer):  
        serializer.save(user=self.request.user)  


class PetDetail(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer


class ProductDetail(generics.RetrieveAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer


class ProductUpdate(generics.UpdateAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer


class ProductDelete(generics.DestroyAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer


class DietCreate(generics.CreateAPIView):
    queryset = Diet.objects.all()
    serializer_class = DietSerializer

    def perform_create(self, serializer):
        serializer.save(pet=self.request.user.pet)


class PetDietList(generics.ListAPIView):
    serializer_class = DietSerializer
    authentication_classes = [TokenAuthentication]    
    permission_classes = [permissions.IsAuthenticated] 

    def get_queryset(self):
        pet_id = self.kwargs['pk']  # Get the pet ID from the URL
        return Diet.objects.filter(pet__id=pet_id)  # Return the diets associated with the pet
