from django.urls import include, path
from . import views

urlpatterns = [
    path('<int:pk>', views.product_mix_api_view, name='product-detail'),
    path('<int:pk>/update', views.product_update_api_view, name='product-edit'),
    path('<int:pk>/delete', views.product_delete_api_view),
    path('', views.product_create_api_view, name='product-list')
    ] 