# Generated by Django 4.1.5 on 2023-02-01 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='image',
            field=models.ImageField(default='image_8.jpg', upload_to='static/images'),
        ),
    ]
