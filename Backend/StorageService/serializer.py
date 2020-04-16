from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):

    class Meta:
        model = File
        fields = ('file', 'user', )

    def create(self, validated_data):
        return File.objects.create(**validated_data)
