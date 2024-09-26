from django.db import models

class Category(models.Model):
    name_tm = models.CharField(max_length=100, unique=True)
    name_ru = models.CharField(max_length=100, unique=True)
    name_en = models.CharField(max_length=100, unique=True)

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name_tm