# Generated by Django 3.2.7 on 2021-10-09 05:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('livedata', '0007_auto_20211001_2301'),
    ]

    operations = [
        migrations.CreateModel(
            name='weather_data_chart',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='Timestamp',
            field=models.IntegerField(max_length=50),
        ),
    ]