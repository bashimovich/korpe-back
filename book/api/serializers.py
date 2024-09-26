from rest_framework import serializers
from book.models import Book
from channel.api.serializers import ChannelSerializer, CategorySerializer, LessonSerializer

class BookSerializer(serializers.ModelSerializer):
    channel = ChannelSerializer()
    category = CategorySerializer()
    lesson = LessonSerializer()

    class Meta:
        model = Book
        fields = [
            'unique_key', 'channel', 'category', 'lesson', 'name',
            'description_tm', 'description_en', 'description_ru',
            'image', 'ebook_file', 'book_size', 'author', 'is_active',
            'created_at', 'updated_at', 'views', 
        ]
        read_only_fields = ['unique_key', 'created_at', 'updated_at', 'views']
