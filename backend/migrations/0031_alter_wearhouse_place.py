# Generated by Django 4.1.5 on 2023-03-14 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0030_rename_latitude_wearhouse_description_kr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wearhouse',
            name='place',
            field=models.CharField(max_length=100, null=True),
        ),
    ]