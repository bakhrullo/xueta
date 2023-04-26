# Generated by Django 4.1.5 on 2023-03-30 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0033_loaderequipments'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loaderequipments',
            name='tonn',
        ),
        migrations.AddField(
            model_name='loaderequipments',
            name='name_kr',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='loaderequipments',
            name='tonn_en',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='loaderequipments',
            name='tonn_kr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='loaderequipments',
            name='tonn_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='loaderequipments',
            name='tonn_uz',
            field=models.CharField(max_length=100, null=True),
        ),
    ]