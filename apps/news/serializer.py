from rest_framework import serializers
from .models import Category, Image, News
from user.serializer import UserSerial


class CategorySerial(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ImageSerial(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image_path']


class NewsSerial(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'created_at', 'text', 'category', 'author', 'images']

    category = CategorySerial(many=True)
    author = UserSerial(read_only=True)
    images = ImageSerial(many=True)


class NewsdetailSerial(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'created_at', 'text', 'category', 'author', 'images']
    category = CategorySerial(many=True)
    author = UserSerial(read_only=True)
    images = ImageSerial(many=True)

