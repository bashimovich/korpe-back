from rest_framework import generics
from channel.models import Banner
from .serializers import BannerSerializer

class BannerListView(generics.ListAPIView):
    queryset = Banner.objects.filter(is_active = True)[:3]
    serializer_class = BannerSerializer