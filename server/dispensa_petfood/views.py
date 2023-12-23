import json
from django.forms.models import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response

from dispensa_petfood.models import PetProduct
from dispensa_petfood.serializers import PetProductSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    print("ciao!" , flush=True)
    serializer = PetProductSerializer(request.data)
    if serializer.is_valid():
        instance = serializer.save()
        print(instance, flush=True)
        return Response(instance)

# Testing API
@api_view(["GET"])
def test_api(request, *args, **kwargs):
    data = {
        "name": "Api Test",
        "content": "Success!"
    }
    return Response(data)