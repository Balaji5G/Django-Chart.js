import pika
import json
parameters=pika.ConnectionParameters('localhost')
connection=pika.BlockingConnection(parameters)
channel=connection.channel()
channel.queue_declare(queue='weather data',durable=True)

def callback(ch,method,properties,body):
    data=json.loads(body)
    print(data)
channel.basic_consume(queue='weather data',on_message_callback=callback, auto_ack=True)
print('waiting for messages')
channel.start_consuming()

