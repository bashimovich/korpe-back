from rest_framework.response import Response
from rest_framework import generics
from audio.models import Audio, AudioView
from .serializers import AudioSerializer
from rest_framework import filters
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import AudioFilter

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AudioListView(generics.ListAPIView):
    queryset = Audio.objects.filter(is_active = True, is_publish = True)
    serializer_class = AudioSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('title_tm', 'title_en', 'title_ru')
    filterset_class = AudioFilter

class AudioDetailView(generics.RetrieveAPIView):
    queryset = Audio.objects.filter(is_active = True, is_publish = True)
    serializer_class = AudioSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ip_address = get_client_ip(request)
        if not AudioView.objects.filter(video=instance, ip_address=ip_address).exists():
            instance.views += 1
            instance.save()
            AudioView.objects.create(video=instance, ip_address=ip_address)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
