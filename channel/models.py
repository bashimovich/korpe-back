from django.db import models
from django.contrib.auth.models import Group
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile

class Channel(models.Model):
    username = models.CharField(max_length=255, null=False, unique=True)
    image = models.ImageField(upload_to='images/profile/')
    role = models.ForeignKey(Group, on_delete=models.CASCADE, null=False, blank=True)

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            if img.height > 300 or img.width > 300: 
                output_size = (300, 300)
                img.thumbnail(output_size)  
                img_io = BytesIO()
                img.save(img_io, format='jpg') 
                self.image.save(self.image.name, ContentFile(img_io.getvalue()), save=False)
        
        super().save(*args, **kwargs)

class Category(models.Model):
    name_tm = models.CharField(max_length=255, null=False, unique=True)
    name_en = models.CharField(max_length=255, null=False, unique=True)
    name_ru = models.CharField(max_length=255, null=False, unique=True)
    image = models.ImageField(upload_to='images/category/')

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_tm

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            if img.height > 300 or img.width > 300: 
                output_size = (300, 300)
                img.thumbnail(output_size)  
                img_io = BytesIO()
                img.save(img_io, format='jpg') 
                self.image.save(self.image.name, ContentFile(img_io.getvalue()), save=False)
        
        super().save(*args, **kwargs)

class Lesson(models.Model):
    name_tm = models.CharField(max_length=255, null=False, unique=True)
    name_en = models.CharField(max_length=255, null=False, unique=True)
    name_ru = models.CharField(max_length=255, null=False, unique=True)
    image = models.ImageField(upload_to='images/lesson/')

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name_tm

    def save(self, *args, **kwargs):
        if self.image:
            img = Image.open(self.image)
            if img.height > 600 or img.width > 600: 
                output_size = (600, 600)
                img.thumbnail(output_size)  
                img_io = BytesIO()
                img.save(img_io, format='jpg') 
                self.image.save(self.image.name, ContentFile(img_io.getvalue()), save=False)
        
        super().save(*args, **kwargs)


class Banner(models.Model):
    name = models.CharField(max_length=255, null=False, unique=True)
    url = models.CharField(max_length=255, null=False)
    image = models.ImageField(upload_to='images/banners/')
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name