from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
import json
from django.http import HttpResponse 
from .models import weather_data,weather_data_hours
import pika
import json
import unittest
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.db.models import Avg
# Create your views here.

# parameters=pika.ConnectionParameters('localhost')
# connection=pika.BlockingConnection(parameters)
# channel=connection.channel()
# channel.queue_declare(queue='weather data',durable=True)

# def callback(ch,method,properties,body):
#     data=json.loads(body)
#     print(data)
#     base1=weather_data(
#         city=data['cityname'],
#         Temperature=data['temperature'],
#         Timestamp=data['timestamp']
#     )
#     base1.save()    
# channel.basic_consume(queue='weather data',on_message_callback=callback, auto_ack=True)
# channel.start_consuming()

def chart_data(request):
    labels=[]
    day1_data=[]
    day1_data_1=[]
    temp_avg=[]
    temp_avg1=[]
    temp_avg2=[]
    temp_avg3=[]
    temp_avg4=[]
    temp_avg5=[]
    temp_avg6=[]
    temp_avg7=[]
    day2_data=[]
    day2_data_1=[]
    temp_day2_avg=[]
    temp_day2_avg1=[]
    temp_day2_avg2=[]
    temp_day2_avg3=[]
    query=weather_data.objects.raw("select * from livedata_weather_data where Timestamp>=1633759081")
    for temp in query:
        if temp.Timestamp>=1633759081 and temp.Timestamp<=1634055370 and temp.city=='Chennai':
            temp_avg.append(temp.Temperature)
        elif temp.Timestamp>=1633759199 and temp.Timestamp<=1634055624 and temp.city=='Toronto':
            temp_avg1.append(temp.Temperature)
        elif temp.Timestamp>=1634055984 and temp.Timestamp<1634100789 and temp.city=='Chennai':
            temp_avg2.append(temp.Temperature)
        elif temp.Timestamp>=1634056017 and temp.Timestamp<1634100727 and temp.city=='Toronto':
            temp_avg3.append(temp.Temperature)
        elif temp.Timestamp>=1634100789 and temp.Timestamp<=1634101183 and temp.city=='Chennai':
            temp_avg4.append(temp.Temperature)
        elif temp.Timestamp>=1634100727 and temp.Timestamp<=1634101479 and temp.city=='Toronto':
            temp_avg5.append(temp.Temperature)
        elif temp.Timestamp>=1634214810 and temp.Timestamp<=1634215447 and temp.city=='Chennai':
            temp_avg6.append(temp.Temperature)
        elif temp.Timestamp>=1634214846 and temp.Timestamp<=1634215525 and temp.city=='Toronto':
            temp_avg7.append(temp.Temperature)
        elif temp.Timestamp>=1634531764 and temp.Timestamp<=1634532121 and temp.city=='Chennai':
            temp_day2_avg.append(temp.Temperature)
        elif temp.Timestamp>=1634531862 and temp.Timestamp<=1634531862 and temp.city=='Toronto':
            temp_day2_avg1.append(temp.Temperature)
        elif temp.Timestamp>=1634532730 and temp.Timestamp<=1634538290 and temp.city=='Chennai':
            temp_day2_avg2.append(temp.Temperature)
        elif temp.Timestamp>=1634532728 and temp.Timestamp<=1634538008 and temp.city=='Toronto':
            temp_day2_avg3.append(temp.Temperature)

    avg_city_1=round(((sum(temp_avg)/len(temp_avg))-273.15),2)
    day1_data.append(avg_city_1)
    avg_city_2=round(((sum(temp_avg1)/len(temp_avg1))-273.15),2)  
    day1_data_1.append(avg_city_2)
    avg_city_3=round(((sum(temp_avg2)/len(temp_avg2))-273.15),2)
    day1_data.append(avg_city_3)
    avg_city_4=round(((sum(temp_avg3)/len(temp_avg3))-273.15),2)
    day1_data_1.append(avg_city_4)
    avg_city_5=round(((sum(temp_avg4)/len(temp_avg4))-273.25),2)
    day1_data.append(avg_city_5)
    avg_city_6=round(((sum(temp_avg5)/len(temp_avg5))-273.25),2)
    day1_data_1.append(avg_city_6)
    avg_city_7=round(((sum(temp_avg6)/len(temp_avg6))-273.15),2)
    day1_data.append(avg_city_7)
    avg_city_8=round(((sum(temp_avg7)/len(temp_avg7))-273.15),2)
    day1_data_1.append(avg_city_8)
    day2_avg=round(((sum(temp_day2_avg)/len(temp_day2_avg))-273.15),2)
    day2_data.append(day2_avg)
    day2_avg1=round(((sum(temp_day2_avg1)/len(temp_day2_avg1))-273.15),2)
    day2_data_1.append(day2_avg1)
    day2_avg2=round(((sum(temp_day2_avg2)/len(temp_day2_avg2))-273.15),2)
    day2_data.append(day2_avg2)
    day2_avg3=round(((sum(temp_day2_avg3)/len(temp_day2_avg3))-273.15),2)
    day2_data_1.append(day2_avg3)
    day_average_chennai=[]
    day_average_toronto=[]
    avg_day1_chennai=round((sum(day1_data)/len(day1_data)),2)
    day_average_chennai.append(avg_day1_chennai)
    avg_day1_toronto=round((sum(day1_data_1)/len(day1_data_1)),2)
    day_average_toronto.append(avg_day1_toronto)
    avg_day2_chennai=round((sum(day2_data)/len(day2_data)),2)
    day_average_chennai.append(avg_day2_chennai)
    avg_day2_toronto=round((sum(day1_data_1)/len(day1_data_1)),2)
    day_average_toronto.append(avg_day2_toronto)
    z=int(datetime.now().strftime('%H'))
    current_day=datetime.now().strftime('%y:%m:%d')
    last_n_time=[]
    for i in range(5):
        if z==00:
            z=12
        last_n_time.append(z-i)
    last_n_time.reverse()
    #import pdb;pdb.set_trace()
    return render(request,'basic.html',{'labels':labels[:10],'data':day1_data,'data_1':day1_data_1,'temp':day_average_chennai,'temp1':day_average_toronto,'current_day_avg':avg_day2_chennai,'current_day_avg1':avg_day2_toronto,'z':z,'last_n_time':last_n_time,'current_day':current_day})

  # QuerySet=weather_data.objects.order_by('Timestamp')
    # for values in QuerySet:
    #     epoch=datetime.fromtimestamp(values.Timestamp).strftime('%y-%m-%d %H:%M:%S')
    #     labels.append(epoch[9:])