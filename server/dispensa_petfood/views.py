import json

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import authentication, generics, mixins, permissions

from api.authentication import TokenAuthentication

from .models import PetProduct
from ..api.permissions import IsStaffEditorPermission
from .serializers import PetProductSerializer



class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer
    # lookup_field = "id" # slug, id, pk, uuid


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer
    permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission]
    
    def perform_create(self, serializer):
        print(serializer.validated_data, flush=True)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)


product_create_api_view = ProductListCreateAPIView.as_view()


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer

    def performe_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()

product_update_api_view = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        

product_delete_api_view = ProductDeleteAPIView.as_view()


class ProductListAPIView(generics.ListAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer

product_list_api_view = ProductListAPIView.as_view()


class ProductMixAPIView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView):

    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer
    lookup_field = "pk"
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = 'this is a single view stuff'
        serializer.save(content=content)
        
product_mix_api_view = ProductMixAPIView.as_view()