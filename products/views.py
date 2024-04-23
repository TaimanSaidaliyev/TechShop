from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import *
from .serializers import *
from rest_framework import status


class ProductListView(APIView):
    def get(self, request):
        products = Products.objects.all()
        return Response({
            'products': ProductListSerializer(products, many=True).data
        })


class ProductSearchList(APIView):
    def get(self, request):
        categories_ids = request.query_params.get('category_ids')
        shops_ids = request.query_params.get('shops_ids')
        products = Products.objects.all().order_by('-pk')

        page = int(request.query_params.get('page'))
        count = int(request.query_params.get('count'))
        text_field = request.query_params.get('text_field')

        if page:
            products = products[(page - 1) * count:page * count]

        if text_field:
            products = Products.objects.filter(title__contains=text_field)

        if shops_ids:
            shops_ids = [int(id) for id in shops_ids.split(',')]
            products = Products.objects.filter(ordercart__shop__get_shop_product__in=shops_ids)

        if categories_ids:
            categories_ids = [int(id) for id in categories_ids.split(',')]
            products = products.filter(category_id__in=categories_ids)

        serializer = ProductListSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductById(APIView):
    def get(self, request, product_id):
        product = Products.objects.filter(pk=product_id).first()

        if not product:
            return Response({'error': 'ID продукта не найден'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductListSerializer(product)

        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )

    def delete(self, request, product_id):
        product = Products.objects.filter(pk=product_id).first()

        if not product:
            return Response({'error': 'ID продукта не найден'}, status=status.HTTP_404_NOT_FOUND)

        product.delete()

        return Response({'status': 'Успешно удалено'}, status=status.HTTP_200_OK)

    def put(self, request, product_id):
        product = Products.objects.filter(pk=product_id).first()

        if not product:
            return Response({'error': 'ID продукта не найден'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductListSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Успешно отредактирован'}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = ProductListSerializerPost(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({
                    'status': 'Успешно добавлено'
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({
                    'status': 'Добавление невозможно',
                    'error': str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoriesList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        return Response(CategorySerializer(categories, many=True).data)


class BrandList(APIView):
    def get(self, request):
        brands = Brand.objects.all()
        return Response(BrandSerializer(brands, many=True).data)


class ColorList(APIView):
    def get(self, request):
        colors = Colours.objects.all()
        return Response(ColorSerializer(colors, many=True).data)

