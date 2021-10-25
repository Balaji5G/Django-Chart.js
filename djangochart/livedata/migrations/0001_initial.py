# Generated by Django 3.2.7 on 2021-09-27 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='weather_data',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('Temperature', models.FloatField(max_length=150)),
                ('Timestamp', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='period',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('labels',models.IntegerField()),
            ],
        ),
    ]
