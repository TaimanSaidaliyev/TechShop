from .serializers import *
from person.views import *
from rest_framework.authentication import get_authorization_header


class ShopsByProductId(APIView):
    def get(self, request, product_id):
        prices = ProductPrice.objects.filter(product_id=product_id).select_related('shop')

        shops = [price.shop for price in prices if price.shop]

        serializer = ShopSerializer(shops, many=True, context={'product_id': product_id})
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsByShopId(APIView):
    def get(self, request, shop_id):
        product_prices = ProductPrice.objects.filter(shop_id=shop_id).select_related('product')

        serializer = ProductPriceSerializer(product_prices, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductPriceList(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token_value = auth[1].decode('utf-8')
            user = get_user_by_token(token_value)
            person = Person.objects.get(user_id=user.pk)
            product_price_list = ProductPrice.objects.filter(shop=person.shop.pk)
            return Response(ProductPriceMySerializer(product_price_list, many=True).data)


class ProductPriceOper(APIView):
    def post(self, request):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token_value = auth[1].decode('utf-8')
            user = get_user_by_token(token_value)
            try:
                person = Person.objects.get(user=user)
            except Person.DoesNotExist:
                return Response({
                    'status': 'Person not found.'
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer = ProductPricePostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.validated_data['shop'] = person.shop
                product_id = serializer.validated_data.get('product')
                if ProductPrice.objects.filter(product_id=product_id, shop_id=person.shop).exists():
                    return Response({
                        'status': 'Товар с такой ценой в этом магазине уже существует.'
                    }, status=status.HTTP_400_BAD_REQUEST)

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

    def put(self, request, product_price_id):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token_value = auth[1].decode('utf-8')
            user = get_user_by_token(token_value)
            try:
                person = Person.objects.get(user=user)
            except Person.DoesNotExist:
                return Response({
                    'status': 'Неверный токен.'
                }, status=status.HTTP_404_NOT_FOUND)

            try:
                product_price = ProductPrice.objects.get(pk=product_price_id, shop=person.shop)
            except ProductPrice.DoesNotExist:
                return Response({
                    'status': 'Цена не найдена.'
                }, status=status.HTTP_404_NOT_FOUND)

            serializer = ProductPricePostSerializer(product_price, data=request.data, partial=True)
            if serializer.is_valid():
                try:
                    serializer.save()
                    return Response({
                        'status': 'Успешно отредактировано.'
                    }, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({
                        'status': 'Произошла ошибка.',
                        'error': str(e)
                    }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, product_price_id):
        auth = get_authorization_header(request).split()
        if auth and len(auth) == 2:
            token_value = auth[1].decode('utf-8')
            user = get_user_by_token(token_value)

            try:
                person = Person.objects.get(user=user)
            except Person.DoesNotExist:
                return Response({
                    'status': 'Пользователь не найден.'
                }, status=status.HTTP_404_NOT_FOUND)

            try:
                product_price = ProductPrice.objects.get(pk=product_price_id, shop=person.shop)
                product_price.delete()
                return Response({
                    'status': 'Успешно удалено'
                }, status=status.HTTP_204_NO_CONTENT)
            except ProductPrice.DoesNotExist:
                return Response({
                    'status': 'Не хватает прав.'
                }, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({
                    'status': 'Ошибка при удалении',
                    'error': str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status': 'Неправильный токен.'
            }, status=status.HTTP_400_BAD_REQUEST)
