from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Person


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')
        depth = 4


class UserMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
        depth = 4