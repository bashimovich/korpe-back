from django.urls import path
from .views import BannerListView, ParentsPageBannerListView, TeacherPageBannerListView, AboutView

urlpatterns = [
    path('', BannerListView.as_view(), name='banner-list'),
    path('t', TeacherPageBannerListView.as_view(), name='teachers-banner-list'),
    path('p', ParentsPageBannerListView.as_view(), name='parents-banner-list'),
    path('a', AboutView.as_view(), name='about-view'),
]