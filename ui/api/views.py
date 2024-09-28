from rest_framework import generics
from ui.models import HomeDailyBlog
from .serializers import HomeDailyBlogSerializer

class HomeDailyBlogListView(generics.ListAPIView):
    queryset = HomeDailyBlog.objects.filter(is_active = True).order_by('-id')[:3]
    serializer_class = HomeDailyBlogSerializer