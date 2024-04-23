from rest_framework import serializers
from .models import Shop, ProductPrice


class ShopSerializer(serializers.ModelSerializer):
    price = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ['id', 'title', 'address', 'telephone', 'image', 'price']

    def get_price(self, obj):
        product_id = self.context['product_id']
        product_price = ProductPrice.objects.filter(product_id=product_id, shop=obj).first()
        return product_price.price if product_price else None


class ProductPriceSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='product.title')
    description = serializers.CharField(source='product.description')
    image = serializers.CharField(source='product.image')

    class Meta:
        model = ProductPrice
        fields = ['product_id', 'title', 'description', 'price', 'new_price', 'image']


class ProductPriceMySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ('__all__')
        depth = 4


class ProductPricePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ('__all__')