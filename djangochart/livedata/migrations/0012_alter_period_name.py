# Generated by Django 3.2.7 on 2021-10-19 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livedata', '0011_alter_weather_data_temperature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
