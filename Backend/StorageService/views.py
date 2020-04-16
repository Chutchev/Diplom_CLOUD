from django.shortcuts import render
from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from LoginService.models import Profile
from .serializer import *
from requests.utils import quote, unquote

class UploadFileView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FileSerializer
    parser_classes = [FileUploadParser, ]

    def post(self, request, *args, **kwargs):
        user = Profile.objects.get(user=self.request.user)
        files = request.FILES
        data = request.data
        f = files['file']
        f.name = unquote(f.name)
        files.update({'user': user.pk})
        file_serializer = FileSerializer(data=files)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FilesView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = FileSerializer
    parser_classes = [FileUploadParser]

    def get_queryset(self):
        user = Profile.objects.get(user=self.request.user)
        return File.objects.filter(user=user)




