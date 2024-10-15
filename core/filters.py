import django_filters
from audio.models import Audio
from blog.models import Blog
from book.models import Book
from video.models import Video
from teachers.models import BlogforTeachers
from parents.models import BlogforParents

class AudioFilter(django_filters.FilterSet):
    class Meta:
        model = Audio
        fields = {
            'type_audio': ['iexact'],
            'lang_audio': ['iexact'],
            'category': ['exact'],
            'lesson': ['exact'],
        }

class BlogFilter(django_filters.FilterSet):
    class Meta:
        model = Blog
        fields = {
            'category': ['exact'],
            'lesson': ['exact'],
        }

class BookFilter(django_filters.FilterSet):
    class Meta:
        model = Book
        fields = {
            'category': ['exact'],
        }

class VideoFilter(django_filters.FilterSet):
    class Meta:
        model = Video
        fields = {
            'category': ['exact'],
            'lesson': ['exact'],
        }

class TeachersFilter(django_filters.FilterSet):
    class Meta:
        model = BlogforTeachers
        fields = {
            'category': ['exact'],
            'lesson': ['exact'],
        }

class ParentsFilter(django_filters.FilterSet):
    class Meta:
        model = BlogforParents
        fields = {
            'category': ['exact'],
            'lesson': ['exact'],
        }