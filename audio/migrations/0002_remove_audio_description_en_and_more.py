# Generated by Django 5.1 on 2024-09-16 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audio', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='audio',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='audio',
            name='description_tm',
        ),
    ]
