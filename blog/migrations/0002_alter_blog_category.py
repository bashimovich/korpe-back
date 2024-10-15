# Generated by Django 5.1 on 2024-10-13 08:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('channel', '0008_categorykids_categoryparents_categoryteachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_category', to='channel.categorykids'),
        ),
    ]