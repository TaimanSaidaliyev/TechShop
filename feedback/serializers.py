from rest_framework import serializers
from feedback.models import Feedback


class FeedBackByProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('__all__')
        depth = 4


class FeedBackByProductPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ('__all__')