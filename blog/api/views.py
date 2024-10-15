from rest_framework.response import Response
from rest_framework import generics
from blog.models import Blog, BlogView
from .serializers import BlogSerializer
from rest_framework import filters
from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from core.filters import BlogFilter

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.filter(is_active=True, is_publish=True)
    serializer_class = BlogSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter,)
    search_fields = ('title_tm', 'title_en', 'title_ru')
    filterset_class = BlogFilter

class BlogListThreeView(generics.ListAPIView):
    queryset = Blog.objects.filter(is_active=True).order_by('-id')[:3]
    serializer_class = BlogSerializer

class BlogDetailView(generics.RetrieveAPIView):
    queryset = Blog.objects.filter(is_active=True)
    serializer_class = BlogSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ip_address = get_client_ip(request)
        
        if not BlogView.objects.filter(blog=instance, ip_address=ip_address).exists():
            instance.views += 1
            instance.save()
            BlogView.objects.create(blog=instance, ip_address=ip_address)

        serializer = self.get_serializer(instance)
        response_data = serializer.data
        return Response(response_data)

class TopBlogListView(generics.ListAPIView):
    queryset = Blog.objects.filter(is_active=True, is_publish=True).order_by('views')[:8]
    serializer_class = BlogSerializer