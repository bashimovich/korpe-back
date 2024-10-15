from rest_framework import generics
from channel.models import Banner, TeacherPageBanner, ParentsPageBanner, About, CategoryKids, CategoryParents, CategoryTeachers
from .serializers import BannerSerializer, AboutSerializer, CategoryKidsSerializer, CategoryParentsSerializer, CategoryTeachersSerializer

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

class TeachersCategoryView(generics.ListAPIView):
    queryset = CategoryTeachers.objects.filter(is_active = True).order_by('-id')
    serializer_class = CategoryTeachersSerializer

class ParentsCategoryView(generics.ListAPIView):
    queryset = CategoryParents.objects.filter(is_active = True).order_by('-id')
    serializer_class = CategoryParentsSerializer

class KidsVideoCategoryView(generics.ListAPIView):
    queryset = CategoryKids.objects.filter(is_active = True, category_type = 'video').order_by('-id')
    serializer_class = CategoryKidsSerializer
class KidsBookCategoryView(generics.ListAPIView):
    queryset = CategoryKids.objects.filter(is_active = True, category_type = 'book').order_by('-id')
    serializer_class = CategoryKidsSerializer
class KidsBlogCategoryView(generics.ListAPIView):
    queryset = CategoryKids.objects.filter(is_active = True, category_type = 'blog').order_by('-id')
    serializer_class = CategoryKidsSerializer