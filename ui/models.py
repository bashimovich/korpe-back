import uuid
import os
from django.db import models
from channel.models import Channel, Category, Lesson
from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

def validate_img_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.jpeg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')

class HomeDailyBlog(models.Model):
    unique_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    content_tm = RichTextField(null=True)
    content_en = RichTextField(null=True)
    content_ru = RichTextField(null=True)
    thumbnail = models.ImageField(upload_to='images/ui/', validators=[validate_img_file_extension])
    is_active = models.BooleanField(default=False)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content_tm[:15]

    def save(self, *args, **kwargs):
        if self.thumbnail:
            img = Image.open(self.thumbnail)
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            if img.height > 600 or img.width > 600: 
                output_size = (600, 600)
                img.thumbnail(output_size)  
                img_io = BytesIO()
                img.save(img_io, format='jpeg') 
                self.thumbnail.save(self.thumbnail.name, ContentFile(img_io.getvalue()), save=False)
        
        super().save(*args, **kwargs)

