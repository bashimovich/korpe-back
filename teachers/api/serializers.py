from rest_framework import serializers
from teachers.models import BlogforTeachers 
from channel.api.serializers import ChannelSerializer, CategorySerializer, LessonSerializer

class BlogforTeachersSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()
    category = CategorySerializer()
    lesson = LessonSerializer()

    class Meta:
        model = BlogforTeachers
        fields = [
            'unique_key', 'channel', 'category', 'lesson',
            'title_tm', 'title_en', 'title_ru','author', 
            'content_tm', 'content_en', 'content_ru',
            'thumbnail', 'is_active', 'is_publish',
            'created_at', 'updated_at', 'views'
        ]
        read_only_fields = ['unique_key', 'created_at', 'updated_at', 'views']
