from django.db import models
import uuid
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile
from ckeditor.fields import RichTextField
from channel.models import Channel, Category, Lesson
# Create your models here.


class Book(models.Model):
    unique_key = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, null=False, blank=True, related_name='book_channel')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=True, related_name='book_category')
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=False, blank=True, related_name='book_lesson')
    description_tm = RichTextField(null=True)
    description_en = RichTextField(null=True)
    description_ru = RichTextField(null=True)
    image = models.ImageField(upload_to='images/book/')
    views = models.IntegerField(default=0)
    ebook_file = models.FileField(upload_to='ebooks/')
    book_size = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            if img.height > 600 or img.width > 300: 
                output_size = (300, 600)
                img.thumbnail(output_size)  
                img_io = BytesIO()
                img.save(img_io, format='jpeg') 
                self.image.save(self.image.name, ContentFile(img_io.getvalue()), save=False)
        if self.ebook_file:
            file_size_bytes = self.ebook_file.size
            self.book_size = file_size_bytes / (1024 * 1024)

        super().save(*args, **kwargs)

class BookView(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="book_views")
    ip_address = models.GenericIPAddressField() 
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = ("book", "ip_address")
