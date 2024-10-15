from django.contrib import admin
from django import forms
from .models import Video
from channel.models import CategoryKids
from django.conf import settings
from django.utils.html import format_html


class VideoAdminForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = '__all__'
    category = forms.ModelChoiceField(
        queryset=CategoryKids.objects.all(),
        label="Category",
        widget=forms.Select,
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['video'].widget.attrs.update({
            'class' : 'resumable-upload',
            'data-url': settings.MEDIA_URL + 'videos/',
        })
        self.fields['category'].label_from_instance = self.get_category_label
    def get_category_label(self, obj):
        return f"{obj.name_tm} - {obj.get_category_type_display()}"

class VideoAdmin(admin.ModelAdmin):
    form = VideoAdminForm
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['resumable_script'] = format_html(
            '<script src="{}/resumable/resumable.min.js"></script>',
            settings.STATIC_URL
        )
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(Video, VideoAdmin)
