from django.urls import path
from .views import HomeDailyBlogListView, HomeAudioImagesView

urlpatterns = [
    path('daily', HomeDailyBlogListView.as_view(), name='home-daily-list'),
    path('audio/images', HomeAudioImagesView.as_view(), name='home-audio-images'),
]