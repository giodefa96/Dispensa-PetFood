from django.urls import include, path
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('pets/', views.PetList.as_view(), name='pet-list'),
    path('pets/<int:pk>/', views.PetDetail.as_view(), name='pet-detail'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='product-delete'),
]
