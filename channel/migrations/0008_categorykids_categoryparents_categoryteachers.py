# Generated by Django 5.1 on 2024-10-13 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0007_category_type_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryKids',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tm', models.CharField(max_length=255, unique=True)),
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_ru', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='images/category/')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryParents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tm', models.CharField(max_length=255, unique=True)),
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_ru', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='images/category/')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='CategoryTeachers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_tm', models.CharField(max_length=255, unique=True)),
                ('name_en', models.CharField(max_length=255, unique=True)),
                ('name_ru', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='images/category/')),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]