from django.db import models
from django.db.models.fields import CharField, IntegerField, UUIDField
import uuid

# Create your models here.
class weather_data(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    city=models.CharField(max_length=50)
    Temperature=models.FloatField(max_length=150)
    Timestamp=models.IntegerField() 

    def __str__(self):
        return self.City

class weather_data_hours(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    city_name=models.CharField(max_length=100)
    Temperature=models.FloatField(max_length=100)
    Hours=models.IntegerField()

    
    


    