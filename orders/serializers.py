from rest_framework import serializers
from .models import OrderCart, Products, Shop


class OrderItemSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Products.objects.all(),
        source='product'
    )
    shop_id = serializers.PrimaryKeyRelatedField(
        queryset=Shop.objects.all(),
        source='shop'
    )

    class Meta:
        model = OrderCart
        fields = ['product_id', 'count', 'shop_id', 'price']


class OrderCartSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=100)
    telephone = serializers.CharField(max_length=100)
    address = serializers.CharField(max_length=100)
    deliveryDate = serializers.DateField()
    order = OrderItemSerializer(many=True)


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCart
        fields = ('__all__')
        depth = 3


class OrdersPutSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderCart
        fields = ('__all__')