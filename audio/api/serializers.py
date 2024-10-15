from rest_framework import serializers
from audio.models import Audio
from channel.api.serializers import ChannelSerializer, CategoryKidsSerializer, LessonSerializer

class AudioSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()
    category = CategoryKidsSerializer()
    lesson = LessonSerializer()

    class Meta:
        model = Audio
        fields = [
            'unique_key', 'channel', 'category', 'lesson',
            'title_tm', 'title_en', 'title_ru',
            'thumbnail', 'audio', 'is_active',
            'created_at', 'updated_at', 'views'
        ]
        read_only_fields = ['unique_key', 'created_at', 'updated_at', 'views']

