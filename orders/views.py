from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.authentication import get_authorization_header
from person.views import *
from person.models import *


class CreateOrderCartView(APIView):
    def post(self, request):
        serializer = OrderCartSerializer(data=request.data)
        status_order = OrderStatus.objects.get(pk=1)
        if serializer.is_valid():
            fullname = serializer.validated_data['fullname']
            telephone = serializer.validated_data['telephone']
            delivery_date = serializer.validated_data['deliveryDate']
            order_items = serializer.validated_data['order']
            address = serializer.validated_data['address']
            for item in order_items:
                OrderCart.objects.create(
                    product=item['product'],
                    count=item['count'],
                    shop=item['shop'],
                    price=item['price'] if 'price' in item else None,
                    fullname=fullname,
                    telephone=telephone,
                    delivery_date=delivery_date,
                    address=address,
                    status=status_order
                )
            return Response({"message": "Order created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderListView(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token_value = auth[1].decode('utf-8')

            user = get_user_by_token(token_value)
            person = Person.objects.get(user_id=user.pk)
            shop = Shop.objects.get(pk=person.shop.pk)
            orders = OrderCart.objects.filter(shop=shop.pk)

        return Response(OrdersSerializer(orders, many=True).data, status=status.HTTP_200_OK)


class OrderChange(APIView):
    def put(self, request, order_id):
        order = OrderCart.objects.filter(pk=order_id).first()

        if not order:
            return Response({'error': 'ID продукта не найден'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrdersPutSerializer(order, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'Успешно отредактирован'}, status=status.HTTP_200_OK)

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
