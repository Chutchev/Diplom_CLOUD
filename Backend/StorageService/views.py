from rest_framework import status
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from LoginService.models import Profile
from StorageService.models import File
from .serializer import *
from requests.utils import unquote
from .helpers import delete_file

class FilesView(ListCreateAPIView, DestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = FileSerializer

    def post(self, request, *args, **kwargs):
        user = Profile.objects.get(user=self.request.user)
        files = request.FILES
        f = files['file']
        f.name = unquote(f.name)
        files.update({'user': user.pk})
        file_serializer = FileSerializer(data=files)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            deleted_file = File.objects.get(id=request.data['id'])
            delete_file(deleted_file.path.location, deleted_file.name)
            deleted_file.delete()
            return Response({"SUCCESS": "FILE WAS DELETED"}, status=status.HTTP_200_OK)
        except File.DoesNotExist:
            return Response({'ERROR': 'File matching query does not exist'}, status=status.HTTP_200_OK)

    def get_queryset(self):
        user = Profile.objects.get(user=self.request.user)
        return File.objects.filter(user=user)





