from django.urls import path
from .views import BlogListView, BlogDetailView, BlogListThreeView

urlpatterns = [
    path('', BlogListView.as_view(), name='video-list'),
    path('three', BlogListThreeView.as_view(), name='video-list-three'),
    path('<uuid:unique_key>/', BlogDetailView.as_view(), name='video-detail'),
]