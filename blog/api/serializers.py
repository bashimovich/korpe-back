from rest_framework import serializers
from blog.models import Blog
from channel.api.serializers import ChannelSerializer, CategorySerializer, LessonSerializer

class BlogSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()
    category = CategorySerializer()
    lesson = LessonSerializer()

    class Meta:
        model = Blog
        fields = [
            'unique_key', 'channel', 'category', 'lesson',
            'title_tm', 'title_en', 'title_ru','author', 
            'description_tm', 'description_en', 'description_ru',
            'thumbnail', 'is_active', 'is_publish',
            'created_at', 'updated_at', 'views'
        ]
        read_only_fields = ['unique_key', 'created_at', 'updated_at', 'views']

