# Generated by Django 5.0.7 on 2024-11-30 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('udemy', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='courses',
            field=models.ManyToManyField(related_name='cartss', through='udemy.CartItem', to='udemy.course'),
        ),
    ]
