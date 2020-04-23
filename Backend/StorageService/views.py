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
        user = Profile.objects.get(user=self.request.user)
        deleted_file = File.objects.filter(id=request.data['id'], user=user)
        if deleted_file:
            delete_file(deleted_file[0].path.location, deleted_file[0].name)
            deleted_file[0].delete()
            return Response({"SUCCESS": "FILE WAS DELETED"}, status=status.HTTP_200_OK)
        else:
            return Response({'ERROR': 'File matching query does not exist'}, status=status.HTTP_200_OK)

    def get_queryset(self):
        user = Profile.objects.get(user=self.request.user)
        return File.objects.filter(user=user)





