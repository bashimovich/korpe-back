from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Channel)
admin.site.register(Category)
admin.site.register(Lesson)
admin.site.register(Banner)
admin.site.register(ParentsPageBanner)
admin.site.register(TeacherPageBanner)
admin.site.register(About)