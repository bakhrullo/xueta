# Generated by Django 4.1.4 on 2023-01-07 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_postservice_address_en_postservice_address_ru_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loaderservice',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='loaderservice',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='loaderservice',
            name='description_uz',
        ),
        migrations.RemoveField(
            model_name='loaderservice',
            name='name_en',
        ),
        migrations.RemoveField(
            model_name='loaderservice',
            name='name_ru',
        ),
        migrations.RemoveField(
            model_name='loaderservice',
            name='name_uz',
        ),
        migrations.AddField(
            model_name='loaderservice',
            name='phone',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='loaderservice',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.region'),
        ),
        migrations.AddField(
            model_name='loaderservice',
            name='tonnas',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='loaderservice',
            name='type_en',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='loaderservice',
            name='type_ru',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='loaderservice',
            name='type_uz',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]