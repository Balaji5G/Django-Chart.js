from django.db import models
from django.db.models.fields import CharField, IntegerField, UUIDField
import uuid

# Create your models here.
class weather_data(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    city=models.CharField(max_length=50)
    Temperature=models.FloatField(max_length=100)
    Timestamp=models.IntegerField() 

    def __str__(self):
        return self.City

class period(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    name=models.CharField(max_length=100)
    type=models.CharField(max_length=50)
    labels=models.CharField(max_length=100)
    


    