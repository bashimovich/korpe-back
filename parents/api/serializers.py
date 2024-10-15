from rest_framework import serializers
from parents.models import  BlogforParents
from channel.api.serializers import ChannelSerializer, CategoryParentsSerializer, LessonSerializer

class BlogforParentsSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()
    category = CategoryParentsSerializer()
    lesson = LessonSerializer()

    class Meta:
        model = BlogforParents
        fields = [
            'unique_key', 'channel', 'category', 'lesson',
            'title_tm', 'title_en', 'title_ru','author', 
            'content_tm', 'content_en', 'content_ru',
            'thumbnail', 'is_active', 'is_publish',
            'created_at', 'updated_at', 'views'
        ]
        read_only_fields = ['unique_key', 'created_at', 'updated_at', 'views']
