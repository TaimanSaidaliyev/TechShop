from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import *
from .serializers import *


class ProductListView(APIView):
    def get(self, request):
        products = Products.objects.all()
        return Response({
            'products': ProductListSerializer(products, many=True).data
        })