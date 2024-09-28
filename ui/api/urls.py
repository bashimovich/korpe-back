from django.urls import path
from .views import HomeDailyBlogListView

urlpatterns = [
    path('daily', HomeDailyBlogListView.as_view(), name='home-daily-list'),
]