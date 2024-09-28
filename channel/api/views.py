from rest_framework import generics
from channel.models import Banner, TeacherPageBanner, ParentsPageBanner, About
from .serializers import BannerSerializer, AboutSerializer

class BannerListView(generics.ListAPIView):
    queryset = Banner.objects.filter(is_active = True)[:3]
    serializer_class = BannerSerializer

class TeacherPageBannerListView(generics.ListAPIView):
    queryset = TeacherPageBanner.objects.filter(is_active = True).order_by('-id')[:2]
    serializer_class = BannerSerializer

class ParentsPageBannerListView(generics.ListAPIView):
    queryset = ParentsPageBanner.objects.filter(is_active = True).order_by('-id')[:2]
    serializer_class = BannerSerializer

class AboutView(generics.ListAPIView):
    queryset = About.objects.filter(is_active = True).order_by('-id')[:1]
    serializer_class = AboutSerializer