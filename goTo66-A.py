import pika
import json
import requests

connection = pika.BlockingConnection(pika.ConnectionParameters(host="10.255.255.254", port=2014))
channel = connection.channel()

channel.exchange_declare(exchange='scanner/detected_objects', exchange_type='fanout')
result = channel.queue_declare(queue='', exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange='scanner/detected_objects', queue=queue_name)

for method_frame, properties, body in channel.consume(queue=queue_name, auto_ack=True):
    print(json.loads(body.decode('utf-8')))


    for station in json.loads(body.decode('utf-8')):
        if station["name"] == "Captain Morris":
            x = station["pos"]["x"]
            y = station["pos"]["y"]
            print(f"Station 66-A -> x: {x}, y: {y}")
            url = "http://10.255.255.254:2009/set_target"
            data = {
                "target": {
                    "x":  x,
                    "y": y
                }
            }

            response = requests.post(url, json=data)

            print(response.status_code)
            print(response.json())