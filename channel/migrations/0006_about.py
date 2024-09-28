# Generated by Django 5.1 on 2024-09-27 17:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0005_parentspagebanner_teacherpagebanner'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_tm', ckeditor.fields.RichTextField(null=True)),
                ('content_en', ckeditor.fields.RichTextField(null=True)),
                ('content_ru', ckeditor.fields.RichTextField(null=True)),
                ('image', models.ImageField(upload_to='images/about/')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
