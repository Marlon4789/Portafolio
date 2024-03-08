from rest_framework import serializers
from .models import Product

from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'products']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Product
        fields = ('url','id', 'title', 'image_url', 'description','price', 'amount', 'date', 'owner')
        read_only_fields = ('date',)