import requests
import time
import datetime
import config
import pika
import json

def weather_data():
        #import pdb;pdb.set_trace()
    while True:
        list_of_cities=["chennai","toronto"]
        for city in list_of_cities:
            #import pdb;pdb.set_trace()
            req=requests.get(config.weather_website_url.format(city)).json()
            #list_of_weather_data=[]
            city_weather={
                'cityname':req["name"],
                'temperature':req["main"]["temp"],
                'timestamp':req["dt"],
                }
            local_time=datetime.datetime.now().strftime('%H:%M:%S')
            local_timestamp=datetime.datetime.now().timestamp()
            time.sleep(1)
            send_data_to_weather_app(city_weather)

def send_data_to_weather_app(weather_data):        
    parameters=pika.ConnectionParameters('localhost')
    connection=pika.BlockingConnection(parameters)
    channel=connection.channel()
    channel.queue_declare(queue='weather data',durable=True)
    data=weather_data
    message=json.dumps(data)
    channel.basic_publish(exchange='',routing_key='weather data',body=message)
    print(message)
    connection.close()

if __name__=='__main__':
    #print(weather_data())
    print(send_data_to_weather_app(weather_data()))

