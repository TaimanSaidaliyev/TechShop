from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import *
from .serializers import *
from rest_framework import status


class ShopListView(APIView):
    def get(self, request):
        shop = Shop.objects.all()
        return Response({
            'shops': ShopDetailSerializer(shop, many=True).data
        })


class ShopSearchList(APIView):
    def get(self, request, shop_id):
        categories_ids = request.query_params.get('category_ids')
        shops = Shop.objects.all()

        if(categories_ids):
            categories_ids = [int(id) for id in categories_ids.split(',')]
            shops = shops.filter(categories_ids=categories_ids)

        serializer = ShopDetailSerializer(shops)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShopById(APIView):
    def get(self, request, shop_id):
        shop = Shop.objects.filter(pk=shop_id).first()

        if not shop:
            return Response({'error': 'ID продукта не найден'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ShopDetailSerializer(shop_id)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def delete(self, request, shop_id):
        shop = Shop.objects.filter(pk=shop_id).first()

        if not shop:
            return Response({'error': 'ID магазина не найден'}, status=status.HTTP_404_NOT_FOUND)

        shop.delete()

        return Response({'status': 'Успешно удалено'}, status=status.HTTP_200_OK)

    def put(self, request, shop_id):
        shop = Shop.objects.filter(pk=shop_id).first()

        if not shop:
            return Response({'error': 'ID магазина не найден'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ShopDetailSerializer(shop, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Успешно отредактирован'}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

