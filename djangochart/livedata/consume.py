import pika
import json

def callback(ch,method,properties,body):
        weather_data=json.loads(body)
        print(weather_data)
        return weather_data
def weather():
    weather_data=callback()
    values=weather_data
    return values

def connect():
    parameters=pika.ConnectionParameters('localhost')
    connection=pika.BlockingConnection(parameters)
    channel=connection.channel()
    channel.queue_declare(queue='weather data',durable=True)
    channel.basic_consume(queue='weather data',on_message_callback=callback, auto_ack=True)
    channel.start_consuming()
if __name__=='__main__':
    weather(callback())
