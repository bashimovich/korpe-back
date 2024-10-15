from rest_framework.response import Response
from rest_framework import generics
from video.models import Video, VideoView
from .serializers import VideoSerializer, RelatedVideoSerializer
from rest_framework import filters
from django.db.models import Q
import random
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import VideoFilter

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class VideoListView(generics.ListAPIView):
    queryset = Video.objects.filter(is_active = True, is_publish = True)
    serializer_class = VideoSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('title_tm', 'title_en', 'title_ru')
    filterset_class = VideoFilter

class VideoDetailView(generics.RetrieveAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ip_address = get_client_ip(request)
        
        if not VideoView.objects.filter(video=instance, ip_address=ip_address).exists():
            instance.views += 1
            instance.save()
            VideoView.objects.create(video=instance, ip_address=ip_address)
        
        related_videos = Video.objects.filter(
            Q(category=instance.category) |
            Q(channel=instance.channel) |
            Q(lesson=instance.lesson)
        ).exclude(id=instance.id)[:15]

        serializer = self.get_serializer(instance)
        response_data = serializer.data
        response_data['related_videos'] = RelatedVideoSerializer(related_videos, many=True).data
        return Response(response_data)

class RandomVideoView(generics.ListAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    def get_queryset(self):
        return Video.objects.order_by('?')[:20]
