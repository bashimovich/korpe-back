from django.contrib import admin
from django.utils.html import format_html, mark_safe, format_html_join


# Register your models here.

from .models import *

class CategoryKidsAdmin(admin.ModelAdmin):
    list_display = ( "name_tm", "category_type",)
   

admin.site.register(Channel)
admin.site.register(CategoryParents)
admin.site.register(CategoryTeachers)
admin.site.register(Lesson)
admin.site.register(Banner)
admin.site.register(ParentsPageBanner)
admin.site.register(TeacherPageBanner)
admin.site.register(About)
admin.site.register(CategoryKids, CategoryKidsAdmin)