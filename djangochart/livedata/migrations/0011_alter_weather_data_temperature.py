# Generated by Django 3.2.7 on 2021-10-19 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livedata', '0010_auto_20211019_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather_data',
            name='Temperature',
            field=models.FloatField(max_length=100),
        ),
    ]
