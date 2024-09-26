from django.urls import path
from .views import VideoListView, VideoDetailView, RandomVideoView


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', VideoListView.as_view(), name='video-list'),
    path('<uuid:unique_key>/', VideoDetailView.as_view(), name='video-detail'),
    path('random/', RandomVideoView.as_view(), name='video-random'),
]