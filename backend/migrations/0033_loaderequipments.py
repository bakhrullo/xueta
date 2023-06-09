# Generated by Django 4.1.5 on 2023-03-30 05:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0032_remove_loaderequipment_description_en_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoaderEquipments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_uz', models.CharField(blank=True, max_length=500, null=True)),
                ('name_en', models.CharField(blank=True, max_length=500, null=True)),
                ('name_ru', models.CharField(blank=True, max_length=500, null=True)),
                ('type', models.CharField(max_length=100, null=True)),
                ('number', models.CharField(blank=True, max_length=15, null=True)),
                ('tonn', models.CharField(blank=True, max_length=100, null=True)),
                ('region', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='backend.region')),
            ],
        ),
    ]
