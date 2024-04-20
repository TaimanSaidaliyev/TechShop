import json
from django.http import HttpResponse, JsonResponse

from rest_framework.views import APIView, Response
from feedback.models import Feedback
from feedback.serializers import FeedBackByProductSerializer
from django.contrib.auth.models import User

from django.views.decorators.csrf import csrf_exempt

from products.models import Products


class FeedbackView(APIView):
    def get(request, product_id):
        products = Feedback.objects.filter(product_id=product_id)
        return JsonResponse(
            {"feedbacks": FeedBackByProductSerializer(products, many=True).data}
        )

    @csrf_exempt
    def add(request, product_id):
        body = request.body

        json_object = json.loads(body)

        product = Products.objects.filter(pk=product_id).first()
        user_id = json_object["user"]

        user = User.objects.filter(pk=user_id).first()

        feedback = Feedback()
        feedback.product = product
        feedback.rating = json_object["rating"]
        feedback.description = json_object["description"]
        feedback.title = json_object["title"]
        feedback.user = user
        feedback.save()
        return HttpResponse("OK")
