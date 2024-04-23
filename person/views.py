from rest_framework.views import APIView
from .serializers import *
from person.models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authentication import get_authorization_header
from rest_framework.authtoken.models import Token


def get_user_by_token(token):
    token = Token.objects.get(key=token)
    user = token.user
    return user


class UserListView(APIView):
    def get(self, request):
        users = Person.objects.all()
        return Response(UserSerializer(users, many=True).data, status=status.HTTP_200_OK)


class UserMyProfile(APIView):
    def get(self, request):
        auth = get_authorization_header(request).split()

        if auth and len(auth) == 2:
            token_value = auth[1].decode('utf-8')
            user = get_user_by_token(token_value)
            person = Person.objects.get(user_id=user.pk)
            return Response(UserSerializer(person, many=False).data)
        else:
            return Response("Заголовок Authorization отсутствует или некорректен", status=status.HTTP_400_BAD_REQUEST)
