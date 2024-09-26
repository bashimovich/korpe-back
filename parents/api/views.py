from rest_framework.response import Response
from rest_framework import generics
from parents.models import BlogforParents, BlogforParentsView
from .serializers import BlogforParentsSerializer
from rest_framework import filters
from django.db.models import Q

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class BlogforParentsListView(generics.ListAPIView):
    queryset = BlogforParents.objects.filter(is_active=True)
    serializer_class = BlogforParents
    filter_backends = (filters.SearchFilter,)
    search_fields = ('title_tm', 'title_en', 'title_ru')

class BlogforParentsDetailView(generics.RetrieveAPIView):
    queryset = BlogforParents.objects.filter(is_active=True)
    serializer_class = BlogforParentsSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ip_address = get_client_ip(request)
        
        if not BlogforParentsView.objects.filter(blog=instance, ip_address=ip_address).exists():
            instance.views += 1
            instance.save()
            BlogforParentsView.objects.create(blog=instance, ip_address=ip_address)

        serializer = self.get_serializer(instance)
        response_data = serializer.data
        return Response(response_data)
