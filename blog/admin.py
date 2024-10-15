from django import forms
from .models import Blog, CategoryKids
from django.contrib import admin

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
    category = forms.ModelChoiceField(
        queryset=CategoryKids.objects.all(),
        label="Category",
        widget=forms.Select,
    )
    def __init__(self, *args, **kwargs):
        super(BlogForm, self).__init__(*args, **kwargs)
        self.fields['category'].label_from_instance = self.get_category_label
    def get_category_label(self, obj):
        return f"{obj.name_tm} - {obj.get_category_type_display()}"

class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
admin.site.register(Blog, BlogAdmin)
