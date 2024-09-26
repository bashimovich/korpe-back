from django.contrib import admin
from django import forms
from .models import Audio
from django.conf import settings
from django.utils.html import format_html

admin.site.site_header = "Korpe Admin"

class MusicAdminForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['audio'].widget.attrs.update({
            'class' : 'resumable-upload',
            'data-url': settings.MEDIA_URL + 'musics/',
        })

class AudioAdmin(admin.ModelAdmin):
    form = MusicAdminForm
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['resumable_script'] = format_html(
            '<script src="{}/resumable/resumable.min.js"></script>',
            settings.STATIC_URL
        )
        return super().change_view(request, object_id, form_url, extra_context=extra_context)

admin.site.register(Audio, AudioAdmin)