import pika
import json
import requests
 
connection = pika.BlockingConnection(pika.ConnectionParameters(host="10.255.255.254", port=2014))
channel = connection.channel()
 
channel.exchange_declare(exchange='scanner/detected_objects', exchange_type='fanout')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='scanner/detected_objects', queue=queue_name)
 
target_url = "http://10.255.255.254:2009/set_target"
 
def follow_station(station_data):
    for obj in station_data:
        if obj.get('name') == 'Xyron Vex':  
            position = obj['pos']
            x = position['x']
            y = position['y']
 
            payload = {"target": {"x": x, "y": y}}
            try:
                response = requests.post(target_url, json=payload)
                print(f"Set target to: x={x}, y={y}, response={response.status_code}")
            except Exception as e:
                print(f"Error setting target: {e}")
 
for method_frame, properties, body in channel.consume(queue=queue_name, auto_ack=True):
    station_data = json.loads(body.decode('utf-8'))
    follow_station(station_data)