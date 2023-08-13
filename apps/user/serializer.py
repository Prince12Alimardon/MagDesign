from rest_framework import serializers
from .models import Author, Suscie


class UserSerial(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'profession', 'icon_path', 'icon']

    icon = serializers.FileField(write_only=True)
    icon_path = serializers.CharField(read_only=True)


class SuscieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscie
        fields = ['id', 'email']
