from rest_framework import routers
from .api import ProductViewSet

router = routers.DefaultRouter()

# aqui se crea 4 rutas- post, delete, put, get
router.register('api/products', ProductViewSet, 'products')

urlpatterns = router.urls