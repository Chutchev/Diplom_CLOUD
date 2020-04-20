from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(use_url=True)

    class Meta:
        model = File
        fields = ('file', 'user', 'name', 'id',)

    def create(self, validated_data):
        return File.objects.create(**validated_data)




