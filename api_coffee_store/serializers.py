from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'title', 'image_url', 'description', 'amount', 'date')
        read_only_fields = ('date',)