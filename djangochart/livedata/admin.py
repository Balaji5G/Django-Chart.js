from django.contrib import admin
from . models import period, weather_data
# Register your models here.
admin.site.register(weather_data)
admin.site.register(period)