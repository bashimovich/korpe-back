from rest_framework import serializers
from video.models import Video
from channel.api.serializers import ChannelSerializer, CategoryKidsSerializer, LessonSerializer

class VideoSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()
    category = CategoryKidsSerializer()
    lesson = LessonSerializer()
    related_videos = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = [
            'unique_key', 'channel', 'category', 'lesson',
            'title_tm', 'title_en', 'title_ru',
            'description_tm', 'description_en', 'description_ru',
            'thumbnail', 'video', 'is_active', 'is_publish',
            'created_at', 'updated_at', 'views', 'related_videos'
        ]
        read_only_fields = ['unique_key', 'created_at', 'updated_at', 'views']

    def get_related_videos(self, obj):
        return []

class RelatedVideoSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()
    category = CategoryKidsSerializer()
    lesson = LessonSerializer()
    class Meta:
        model = Video
        fields = [
            'unique_key', 'channel', 'category', 'lesson',
            'title_tm', 'title_en', 'title_ru','thumbnail',
            'created_at','views'
        ]
        read_only_fields = ['unique_key', 'created_at', 'updated_at', 'views']