import uuid
import os
from django.db import models
from channel.models import Channel, Category, Lesson
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def validate_audio_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp3']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

def validate_img_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')
TYPE_CHOICES = [
    ('english', 'English'),
    ('turkmen', 'Turkmen'),
    ('russian', 'Russian'),
    ('traditional', 'Traditional'),
    ('tale', 'Tales'),
    ('huwdi', 'Huwdi'),
]
    

class Audio(models.Model):
    unique_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=False, blank=True, related_name='audio_channel')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=True, related_name='audio_category')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=False, blank=True, related_name='audio_lesson')
    type_audio= models.CharField(max_length=100, choices=TYPE_CHOICES, default='turkmen')


    title_tm = models.CharField(max_length=255, null=False)
    title_en = models.CharField(max_length=255, null=False)
    title_ru = models.CharField(max_length=255, null=False)

    thumbnail = models.ImageField(upload_to='images/thumbnail/', validators=[validate_img_file_extension])
    audio = models.FileField(upload_to='audios/', validators=[validate_audio_file_extension])

    is_active = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title_tm

    def save(self, *args, **kwargs):
        if self.thumbnail:
            img = Image.open(self.thumbnail)
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            if img.height > 300 or img.width > 600: 
                output_size = (600, 300)
                img.thumbnail(output_size)  
                img_io = BytesIO()
                img.save(img_io, format='jpeg') 
                self.thumbnail.save(self.thumbnail.name, ContentFile(img_io.getvalue()), save=False)
        
        super().save(*args, **kwargs)

class AudioView(models.Model):
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, related_name="audio_views")
    ip_address = models.GenericIPAddressField() 
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("audio", "ip_address")
