from django.shortcuts import render
from rest_framework.views import APIView, Response
from feedback.models import Feedback
from feedback.serializers import FeedBackByProductSerializer


class FeedBackByProduct(APIView):
    def get(self, request, product_id):
        products = Feedback.objects.filter(product_id=product_id)
        return Response({
            'feedbacks': FeedBackByProductSerializer(products, many=True).data
        })