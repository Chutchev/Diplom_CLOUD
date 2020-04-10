from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework.authtoken.views import obtain_auth_token, ObtainAuthToken
from .serialize import *
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class UserList(ListCreateAPIView):
    serializer_class = ProfileSerializer

    def get_queryset(self):
        return Profile.objects.all()

    def post(self, request, *args, **kwargs):
        data = request.data.get('user')
        serializer = UserSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
           user_saved = serializer.save()
           return Response({'success': f'User {user_saved.username} is added'})
        return Response({'success': f'User is not added'})


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response

class GetToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        try:
            return super().post(request, *args, **kwargs)
        except Exception:
            return Response({'FAILED': True})