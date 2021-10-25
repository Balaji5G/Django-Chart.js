from django.db.models import query
from django.db.models.query import QuerySet
from django.shortcuts import render
import json
from django.http import HttpResponse 
from .models import weather_data,period
import pika
import json
import unittest
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime
from django.db.models import Avg
from livedata.forms import userinput
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
    temp_data_hr=[]
    temp_data_hr1=[]
    temp_data_hr2=[]
    temp_data_hr3=[]
    temp_data_hr4=[]
    temp_data_hr5=[]
    temp_data_hr6=[]
    temp_data_hr7=[]
    temp_day2_data_hr=[]
    temp_day2_data_hr1=[]
    temp_day2_data_hr2=[]
    temp_day2_data_hr3=[]
    query=weather_data.objects.all()
    for temp in query:
        if temp.Timestamp>=1633759081 and temp.Timestamp<=1634055370 and temp.city=='Chennai':
            temp_data_hr.append(temp.Temperature)
        elif temp.Timestamp>=1633759199 and temp.Timestamp<=1634055624 and temp.city=='Toronto':
            temp_data_hr1.append(temp.Temperature)
        elif temp.Timestamp>=1634055984 and temp.Timestamp<1634100789 and temp.city=='Chennai':
            temp_data_hr2.append(temp.Temperature)
        elif temp.Timestamp>=1634056017 and temp.Timestamp<1634100727 and temp.city=='Toronto':
            temp_data_hr3.append(temp.Temperature)
        elif temp.Timestamp>=1634100789 and temp.Timestamp<=1634101183 and temp.city=='Chennai':
            temp_data_hr4.append(temp.Temperature)
        elif temp.Timestamp>=1634100727 and temp.Timestamp<=1634101479 and temp.city=='Toronto':
            temp_data_hr5.append(temp.Temperature)
        elif temp.Timestamp>=1634214810 and temp.Timestamp<=1634215447 and temp.city=='Chennai':
            temp_data_hr6.append(temp.Temperature)
        elif temp.Timestamp>=1634214846 and temp.Timestamp<=1634215525 and temp.city=='Toronto':
            temp_data_hr7.append(temp.Temperature)
        elif temp.Timestamp>=1634531764 and temp.Timestamp<=1634532121 and temp.city=='Chennai':
            temp_day2_data_hr.append(temp.Temperature)
        elif temp.Timestamp>=1634531862 and temp.Timestamp<=1634531862 and temp.city=='Toronto':
            temp_day2_data_hr1.append(temp.Temperature)
        elif temp.Timestamp>=1634532730 and temp.Timestamp<=1634538290 and temp.city=='Chennai':
            temp_day2_data_hr2.append(temp.Temperature)
        elif temp.Timestamp>=1634532728 and temp.Timestamp<=1634538008 and temp.city=='Toronto':
            temp_day2_data_hr3.append(temp.Temperature)
    # import pdb;pdb.set_trace()
    day1_data=[]
    day1_data_1=[]
    avg_city_1=round(((sum(temp_data_hr)/len(temp_data_hr))-273.15),2)
    day1_data.append(avg_city_1)
    avg_city_2=round(((sum(temp_data_hr1)/len(temp_data_hr1))-273.15),2)  
    day1_data_1.append(avg_city_2)
    avg_city_3=round(((sum(temp_data_hr2)/len(temp_data_hr2))-273.15),2)
    day1_data.append(avg_city_3)
    avg_city_4=round(((sum(temp_data_hr3)/len(temp_data_hr3))-273.15),2)
    day1_data_1.append(avg_city_4)  
    avg_city_5=round(((sum(temp_data_hr4)/len(temp_data_hr4))-273.25),2)
    day1_data.append(avg_city_5)
    avg_city_6=round(((sum(temp_data_hr5)/len(temp_data_hr5))-273.25),2)
    day1_data_1.append(avg_city_6)
    avg_city_7=round(((sum(temp_data_hr6)/len(temp_data_hr6))-273.15),2)
    day1_data.append(avg_city_7)
    avg_city_8=round(((sum(temp_data_hr7)/len(temp_data_hr7))-273.15),2)
    day1_data_1.append(avg_city_8)
    # for data in day1_data():
    #     base2=weather_data_periods(
    #     city_name=data['cityname'],
    #     Temperature=data['temperature']
    # )
    # base2.save() 
    day2_data=[]
    day2_data_1=[]
    day2_avg=round(((sum(temp_day2_data_hr)/len(temp_day2_data_hr))-273.15),2)
    day2_data.append(day2_avg)
    day2_avg1=round(((sum(temp_day2_data_hr1)/len(temp_day2_data_hr1))-273.15),2)
    day2_data_1.append(day2_avg1)
    day2_avg2=round(((sum(temp_day2_data_hr2)/len(temp_day2_data_hr2))-273.15),2)
    day2_data.append(day2_avg2)
    day2_avg3=round(((sum(temp_day2_data_hr3)/len(temp_day2_data_hr3))-273.15),2)
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
    current_day=datetime.now().strftime('%d')
    cd=int(datetime.now().strftime('%d'))
    last_n_time=[]
    for i in range(5):
        if z==00:
            z=12
        last_n_time.append(z-i)
    last_n_time.reverse()
    last_n_day=[]
    for i in range(5):
        last_n_day.append(cd-i)
    last_n_day.reverse()
    last_n_hr=[]
    if request.method=='GET':
        form=userinput()
    else:
        form=userinput(request.POST)
        if form.is_valid(): 
            value=form.cleaned_data['entervalue']
        for i in range(value):
            last_n_hr.append(z-i)
        last_n_hr.reverse()
    hour_labels=[]
    day_labels=[]
    month_labels=[]
    query_1=period.objects.all()
    for value in query_1:
        #import pdb;pdb.set_trace()
        if value.name=='hour' and value.type=='xaxis':
            hour_labels.append(str(value.labels))
        elif value.name=='day' and value.type=='xaxis':
            day_labels.append(str(value.labels))
        else:
            month_labels.append(str(value.labels))
    for val in hour_labels:
        hr=val.split(',')
    for val in day_labels:
        day=val.split(',') 
    for val in month_labels:
        mon=val.split(',')
    hr_data=[]
    hr_data1=[]
    for i in range(len(hr)):
        if i==9:
            hr_data.append(day1_data[0])
            hr_data1.append(day1_data_1[0])
        elif i==10:
            hr_data.append(day1_data[1])
            hr_data1.append(day1_data_1[1])
        elif i==11:
            hr_data.append(day1_data[2])
            hr_data1.append(day1_data_1[2])
        elif i==12:
            hr_data.append(day1_data[3])
            hr_data1.append(day1_data_1[3])
        else:
            hr_data.append(0)
            hr_data1.append(0)
    last_n_hr_data=[]
    last_n_hr_data1=[]
    # for i in range(len(hr_data)):
    #     last_n_hr_data.append(0)
    #     last_n_hr_data1.append(0)
    # for i in (range(len(hr_data))):
    #     if last_n_hr[i]==hr_data[i]:
    #         last_n_hr_data.append(hr_data[i])
    #     else:
    #         last_n_hr_data.append(0)
    # for i in range(len(last_n_hr_data1)):
    #     if last_n_hr_data1[i]==hr_data1[i]:
    #         last_n_hr_data1.append(hr_data1[i])
    #     else:
    #         last_n_hr_data1.append(0)
    
    for i in last_n_hr:
        if i==9:
            last_n_hr_data.append(day1_data[0])
            last_n_hr_data1.append(day1_data_1[0])
        elif i==10:
            last_n_hr_data.append(day1_data[1])
            last_n_hr_data1.append(day1_data_1[1])
        elif i==11:
            last_n_hr_data.append(day1_data[2])
            last_n_hr_data1.append(day1_data_1[2])
        elif i==12:
            last_n_hr_data.append(day1_data[3])
            last_n_hr_data1.append(day1_data_1[3])
        else:
            last_n_hr_data.append(0)
            last_n_hr_data1.append(0)
    day_val=[]
    day_val1=[]
    for i in range(1,len(day)):
        if i==11:
            day_val.append(day_average_chennai[0])
            day_val1.append(day_average_toronto[0])
        elif i==12:
            day_val.append(day_average_chennai[1])
            day_val1.append(day_average_toronto[1])
        else:
            day_val.append(0)
            day_val1.append(0)

    #import pdb;pdb.set_trace()
    return render(request,'basic.html',{'hour_labels':hr,'month_labels':mon,'day_labels':day,'data':hr_data,'data_1':hr_data1,'temp':day_val,'temp1':day_val1,'current_day_avg':avg_day2_chennai,'current_day_avg1':avg_day2_toronto,'z':z,'last_n_time':last_n_hr,'current_day':current_day,'last_n_day':last_n_day,'form':form,'last_n_hour_data':last_n_hr_data,'last_n_hour_data1':last_n_hr_data1})
