# Generated by Django 4.1.5 on 2023-01-07 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_customs_region'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customs',
            name='address_en',
        ),
        migrations.RemoveField(
            model_name='customs',
            name='address_ru',
        ),
        migrations.RemoveField(
            model_name='customs',
            name='address_uz',
        ),
    ]
