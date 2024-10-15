from rest_framework import serializers
from channel.models import Channel, Lesson, Banner, About, CategoryKids, CategoryParents, CategoryTeachers

class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = [
            'id', 'username', 'image', 'role',
        ]

class CategoryKidsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryKids
        fields = [
            'id', 'name_tm', 'name_en', 'name_ru', 'image',
        ]
class CategoryParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryParents
        fields = [
            'id', 'name_tm', 'name_en', 'name_ru', 'image',
        ]
class CategoryTeachersSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryTeachers
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