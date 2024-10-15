from django.urls import path
from .views import BlogListView, BlogDetailView, BlogListThreeView, TopBlogListView

urlpatterns = [
    path('', BlogListView.as_view(), name='blog-list'),
    path('three', BlogListThreeView.as_view(), name='blog-list-three'),
    path('<uuid:unique_key>/', BlogDetailView.as_view(), name='blog-detail'),
    path('top-blogs', TopBlogListView.as_view(), name='top-list'),
]