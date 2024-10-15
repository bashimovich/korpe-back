from rest_framework import generics
from ui.models import HomeDailyBlog, HomeAudioImages
from .serializers import HomeDailyBlogSerializer, HomeAudioImagesSerializer

class HomeDailyBlogListView(generics.ListAPIView):
    queryset = HomeDailyBlog.objects.filter(is_active = True).order_by('-id')[:3]
    serializer_class = HomeDailyBlogSerializer

class HomeAudioImagesView(generics.ListAPIView):
    queryset = HomeAudioImages.objects.filter(is_active = True).order_by('order_no')[:6]
    serializer_class = HomeAudioImagesSerializer