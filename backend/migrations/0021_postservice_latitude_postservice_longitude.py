# Generated by Django 4.1.5 on 2023-01-07 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0020_remove_loaderservice_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='postservice',
            name='latitude',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='postservice',
            name='longitude',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
