from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response  


    
# Testing API
@api_view(["GET"])
def test_api(request, *args, **kwargs):
    data = {
        "name": "Api Test",
        "content": "Success!"
    }
    return Response(data)
