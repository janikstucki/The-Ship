import pika
import json
import requests

# Reuse HTTP session for speed
session = requests.Session()

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host="10.255.255.254", port=2014)
)
channel = connection.channel()

channel.exchange_declare(exchange="scanner/detected_objects", exchange_type="fanout")
result = channel.queue_declare(queue="", exclusive=True)
queue_name = result.method.queue
channel.queue_bind(exchange="scanner/detected_objects", queue=queue_name)

url = "http://10.255.255.254:2009/set_target"

def callback(ch, method, properties, body):
    try:
        data = json.loads(body.decode("utf-8"))
    except Exception as e:
        print("JSON error:", e)
        return

    for station in data:
        if station.get("name") == "Captain Morris":
            x = station["pos"]["x"]
            y = station["pos"]["y"]
            print(f"🎯 -> x: {x}, y: {y}")

            try:
                resp = session.post(url, json={"target": {"x": x, "y": y}}, timeout=0.2)
                print(resp.status_code)
            except requests.RequestException as e:
                print("Post error:", e)

# use basic_consume instead of blocking consume loop
channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)

print("⚡ Listening...")
channel.start_consuming()
