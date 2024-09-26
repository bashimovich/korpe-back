from rest_framework.response import Response
from rest_framework import generics
from teachers.models import BlogforTeachers, BlogforTeachersView
from .serializers import BlogforTeachersSerializer
from rest_framework import filters
from django.db.models import Q

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class BlogforTeachersListView(generics.ListAPIView):
    queryset = BlogforTeachers.objects.filter(is_active=True)
    serializer_class = BlogforTeachersSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title_tm', 'title_en', 'title_ru')

class BlogforTeachersDetailView(generics.RetrieveAPIView):
    queryset = BlogforTeachers.objects.filter(is_active=True)
    serializer_class = BlogforTeachersSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ip_address = get_client_ip(request)
        
        if not BlogforTeachersView.objects.filter(blog=instance, ip_address=ip_address).exists():
            instance.views += 1
            instance.save()
            BlogforTeachersView.objects.create(blog=instance, ip_address=ip_address)

        serializer = self.get_serializer(instance)
        response_data = serializer.data
        return Response(response_data)