# Generated by Django 5.1.1 on 2024-09-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udemy', '0002_category_description_en_category_description_ky_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='banners/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_ky',
        ),
        migrations.RemoveField(
            model_name='category',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ky',
        ),
        migrations.RemoveField(
            model_name='category',
            name='name_ru',
        ),
    ]
