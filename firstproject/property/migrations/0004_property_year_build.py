# Generated by Django 4.1.5 on 2023-02-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_alter_property_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='year_build',
            field=models.IntegerField(default=2019),
        ),
    ]
