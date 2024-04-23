from rest_framework import serializers
from .models import *


class ProductListSerializer(serializers.ModelSerializer):
    min_price_info = serializers.SerializerMethodField()
    min_new_price_info = serializers.SerializerMethodField()


    class Meta:
        model = Products
        fields = ('__all__')
        depth = 3

    def get_min_price_info(self, obj):
        return obj.get_min_price_info()

    def get_min_new_price_info(self, obj):
        return obj.get_min_new_price_info()


class ProductListSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('__all__')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ('__all__')


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colours
        fields = ('__all__')