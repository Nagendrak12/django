from rest_framework import routers
from .api import ProductsDataAppViewSet,OrdersDataAppViewSet,Orders_Items_DataAppViewSet,UserViewSet

router = routers.DefaultRouter()
router.register('api/products', ProductsDataAppViewSet)
router.register('api/orders', OrdersDataAppViewSet)
router.register('api/orders_items', Orders_Items_DataAppViewSet)
router.register('account/register', UserViewSet)

urlpatterns = router.urls
