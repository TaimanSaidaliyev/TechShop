from rest_framework import serializers
from .models import *


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('__all__')
        depth = 3


class ProductListSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('__all__')