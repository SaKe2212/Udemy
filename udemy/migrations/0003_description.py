# Generated by Django 5.1.4 on 2024-12-24 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udemy', '0002_profile_description_profile_headline'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='Это описание, которое можно изменить.')),
            ],
        ),
    ]
