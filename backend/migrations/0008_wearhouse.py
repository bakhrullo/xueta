# Generated by Django 4.1.4 on 2022-12-23 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_region'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wearhouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=500, null=True)),
                ('name_en', models.CharField(blank=True, max_length=500, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=500, null=True)),
                ('description_uz', models.TextField(blank=True, max_length=5000, null=True)),
                ('description_en', models.TextField(blank=True, max_length=5000, null=True)),
                ('description_ru', models.TextField(blank=True, max_length=5000, null=True)),
                ('longitude', models.CharField(blank=True, max_length=500, null=True)),
                ('latitude', models.CharField(blank=True, max_length=500, null=True)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.region')),
            ],
        ),
    ]