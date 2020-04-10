from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import *


class FilesView(APIView):
    def get(self, request):
        files = File.objects.all()
        serializer = FileSerializer(files, many=True)
        return Response({'files': serializer.data})

    def post(self, request):
        files = request.data.get('files')
        saved_files = []
        for f in files:
            serializer = FileSerializer(data=f)
            if serializer.is_valid(raise_exception=True):
                file_saved = serializer.save()
                saved_files.append(file_saved.title)
        return Response({'success': f'File {files} is saved'})