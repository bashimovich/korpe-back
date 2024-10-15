from django.urls import path
from .views import AudioListView, AudioDetailView

urlpatterns = [
    path('', AudioListView.as_view(), name='audio-list'),
    path('<uuid:unique_key>/', AudioDetailView.as_view(), name='audio-detail'),
]