
from rest_framework.response import Response
from rest_framework import generics
from book.models import Book, BookView
from .serializers import BookSerializer
from rest_framework import filters
from django.db.models import Q

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'author')

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'author')

class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        ip_address = get_client_ip(request)
        if not BookView.objects.filter(book=instance, ip_address=ip_address).exists():
            instance.views += 1
            instance.save()
            BookView.objects.create(book=instance, ip_address=ip_address)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
