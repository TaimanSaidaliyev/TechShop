from django.shortcuts import render
from rest_framework.views import APIView, Response
from feedback.models import Feedback
from feedback.serializers import *
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import get_authorization_header
from products.models import *


class FeedBackByProduct(APIView):
    def get(self, request, product_id):
        products = Feedback.objects.filter(product_id=product_id)
        return Response({
            'feedbacks': FeedBackByProductSerializer(products, many=True).data
        })

    def delete(self, request, review_id):
        review = Feedback.objects.get(pk=review_id)
        review.delete()
        return Response(status=status.HTTP_200_OK)

    def post(self, request, product_id):
        auth = get_authorization_header(request).split()
        product = Products.objects.get(pk=product_id)
        if auth and len(auth) == 2 and auth[0].lower() == b'token':
            token_key = auth[1].decode('utf-8')
            try:
                token = Token.objects.get(key=token_key)
                user = token.user
            except Token.DoesNotExist:
                return Response({
                    'status': 'Токен не действителен или пользователь не найден.'
                }, status=status.HTTP_401_UNAUTHORIZED)

            serializer = FeedBackByProductPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=user, product=product)
                return Response({
                    'status': 'Успешно добавлено'
                }, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({
                'status': 'Требуется аутентификация.'
            }, status=status.HTTP_401_UNAUTHORIZED)

