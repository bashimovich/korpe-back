from rest_framework import serializers
from channel.models import Channel, Category, Lesson, Banner, About

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            'id', 'username', 'image', 'role',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'id', 'name_tm', 'name_en', 'name_ru', 'image',
        ]

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = [
            'id', 'name_tm', 'name_en', 'name_ru', 'image',
        ]

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
            'name', 'url', 'image'
        ]

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__' 