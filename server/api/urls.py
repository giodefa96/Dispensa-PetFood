from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('test/', views.test_api),
    ]