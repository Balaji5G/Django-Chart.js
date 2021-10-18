import pika
import json 
from weather import weather_data
parameters=pika.ConnectionParameters('localhost')
connection=pika.BlockingConnection(parameters)
channel=connection.channel()
channel.queue_declare(queue='weather data',durable=True)
data=weather_data
message=json.dumps(data)
#message='Hello'
channel.basic_publish(exchange='',routing_key='weather data',body=message)
print(message)
connection.close()