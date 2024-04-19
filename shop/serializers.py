from rest_framework import serializers
from .models import *


class ShopDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('__all__')
        depth = 3


class ShopPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('__all__')