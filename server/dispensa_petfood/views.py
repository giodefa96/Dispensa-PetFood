import json

from rest_framework import generics, mixins

from api.mixins import (
    StaffEditorPermissionMixin,
    UserQuerySetMixin)
from .models import PetProduct
from .serializers import PetProductSerializer



class ProductDetailAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.RetrieveAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer
    # lookup_field = "id" # slug, id, pk, uuid


class ProductListCreateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer
    print("ProductListCreateAPIView", flush=True)

    def perform_create(self, serializer):
        print(serializer.validated_data, flush=True)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(user=self.request.user, content=content)
    
    #def get_queryset(self, *args, **kwargs):
    #    qs = super().get_queryset(*args, **kwargs)
    #    request = self.request
    #    user = request.user
    #    if not user.is_authenticated:
    #        return PetProduct.objects.none()
    #    #print(request.user, flush=True)
    #    return qs.filter(user=request.user)
    


product_create_api_view = ProductListCreateAPIView.as_view()


class ProductUpdateAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer

    def performe_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()

product_update_api_view = ProductUpdateAPIView.as_view()


class ProductDeleteAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer
    
    def perform_destroy(self, instance):
        super().perform_destroy(instance)
        

product_delete_api_view = ProductDeleteAPIView.as_view()


class ProductListAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
    generics.ListAPIView):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer

product_list_api_view = ProductListAPIView.as_view()


class ProductMixAPIView(
    UserQuerySetMixin,
    StaffEditorPermissionMixin,
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