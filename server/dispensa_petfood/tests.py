from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Pet, PetProduct

class PetTests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.pet = Pet.objects.create(name='Fido', type='dog')
        cls.pet_product = PetProduct.objects.create(pet=cls.pet, name='Dog Food', price=19.99)
        
    def test_list_pets(self):
        url = reverse('pet-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)