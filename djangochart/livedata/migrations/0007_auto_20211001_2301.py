# Generated by Django 3.2.7 on 2021-10-01 17:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('livedata', '0006_alter_base_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='weather_data',
            options={},
        ),
        migrations.AlterField(
            model_name='weather_data',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
