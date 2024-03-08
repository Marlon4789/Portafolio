from rest_framework import routers
from api_coffee_store import views
from django.urls import path, include
from .api import ProductViewSet

router = routers.DefaultRouter()

# aqui se crea 4 rutas- post, delete, put, get
router.register('api/products', ProductViewSet, 'products')

urlpatterns = [
    path('', views.api_root),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
]

urlpatterns += router.urls

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]