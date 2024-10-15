# Generated by Django 5.1 on 2024-10-13 08:39

import django.db.models.deletion
import teachers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0008_categorykids_categoryparents_categoryteachers'),
        ('teachers', '0002_remove_blogforteachers_description_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogforteachers',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='blogforteachers_category', to='channel.categoryteachers'),
        ),
        migrations.AlterField(
            model_name='blogforteachers',
            name='thumbnail',
            field=models.ImageField(upload_to='images/teachers/', validators=[teachers.models.validate_img_file_extension]),
        ),
    ]
