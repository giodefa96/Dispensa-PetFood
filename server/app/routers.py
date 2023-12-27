from rest_framework.routers import DefaultRouter 

from dispensa_petfood.viewsets import ProductGenericViewSet


router = DefaultRouter()
router.register('dispensa_pet_food', ProductGenericViewSet, basename='products')


urlpatterns = router.urls