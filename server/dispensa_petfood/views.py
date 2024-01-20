from rest_framework import generics, permissions
from rest_framework.authentication import TokenAuthentication  

from django.contrib.auth.models import User

from .models import Pet, PetProduct
from .serializers import UserSerializer, PetSerializer, PetProductSerializer


class UserList(generics.ListCreateAPIView):  
    queryset = User.objects.all()  
    serializer_class = UserSerializer  
    authentication_classes = [TokenAuthentication]  

    def get_permissions(self):
        if self.request.method == 'POST':
            # Allow any user (authenticated or not) to create a new user
            return [permissions.AllowAny()]
        else:
            # Only allow authenticated users to list users
            return [permissions.IsAuthenticated()]


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class PetList(generics.ListCreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer

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
