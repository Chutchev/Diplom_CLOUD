from rest_framework import serializers
from .models import File

class FileSerializer(serializers.Serializer):
    md5_hash = serializers.CharField()
    title = serializers.CharField()
    fullpath = serializers.CharField()
    username_id = serializers.IntegerField()
    url = serializers.CharField()

    def create(self, validated_data):
        return File.objects.create(**validated_data)