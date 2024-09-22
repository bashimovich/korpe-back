from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('', BlogListView.as_view(), name='video-list'),
    path('<uuid:unique_key>/', BlogDetailView.as_view(), name='video-detail'),
]