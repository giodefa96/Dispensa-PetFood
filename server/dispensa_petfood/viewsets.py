from rest_framework import viewsets, mixins

from .models import PetProduct
from .serializers import PetProductSerializer


class PetProductViewSet(viewsets.ModelViewSet):
    """
    get -> list -> queryset
    post -> create -> serializer.save()
    put -> update -> serializer.save()
    patch -> partial_update -> serializer.save()
    delete -> destroy -> perform_destroy()
    """
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer
    lockup_field = 'pk'


class ProductGenericViewSet(mixins.ListModelMixin,
                            mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset = PetProduct.objects.all()
    serializer_class = PetProductSerializer
    lockup_field = 'pk'


#product_list_api_view = ProductGenericViewSet.as_view({"get": "list"})
#product_product_detail_view = ProductGenericViewSet.as_view({"get": "retrieve"})