from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.api_home),
    path('test/', views.test_api),
    ]