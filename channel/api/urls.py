from django.urls import path
from .views import BannerListView, ParentsPageBannerListView, TeacherPageBannerListView, AboutView, TeachersCategoryView, ParentsCategoryView, KidsBlogCategoryView, KidsBookCategoryView, KidsVideoCategoryView

urlpatterns = [
    path('', BannerListView.as_view(), name='banner-list'),
    path('t', TeacherPageBannerListView.as_view(), name='teachers-banner-list'),
    path('p', ParentsPageBannerListView.as_view(), name='parents-banner-list'),
    path('a', AboutView.as_view(), name='about-view'),
    path('teachers', TeachersCategoryView.as_view(), name='category-teachers'),
    path('parents', ParentsCategoryView.as_view(), name='category-parents'),

    path('kids/video', KidsVideoCategoryView.as_view(), name='category-kids-video'),
    path('kids/book', KidsBookCategoryView.as_view(), name='category-kids-book'),
    path('kids/blog', KidsBlogCategoryView.as_view(), name='category-kids-blog'),
]