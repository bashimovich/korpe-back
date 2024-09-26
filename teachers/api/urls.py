from django.urls import path
from .views import  BlogforTeachersListView, BlogforTeachersDetailView

urlpatterns = [
    path('', BlogforTeachersListView.as_view(), name='parents-list'),
    path('<uuid:unique_key>/', BlogforTeachersDetailView.as_view(), name='parents-detail'),
]