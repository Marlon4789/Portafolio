# ViewSet => Esto nos permite establecer quien puede hacer colsultas sobre esto, ejemplo enviar una serie de autenticación para poder acceder.

from .models import Product
from rest_framework import viewsets, permissions
from .serializers import ProductSerializer

# Que tipo de consultas se podran hacer desde product
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny] # cambiar esto Auth.
    serializer_class = ProductSerializer
