from django.urls import path
from .views import BlogforParentsListView, BlogforParentsDetailView

urlpatterns = [
    path('', BlogforParentsListView.as_view(), name='parents-list'),
    path('<uuid:unique_key>/', BlogforParentsDetailView.as_view(), name='parents-detail'),
]