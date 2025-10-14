import requests
import websocket
import json
import base64

elyse_response = None

def on_message(ws, message):
    global elyse_response
    elyse_response = json.loads(message)
    ws.close()
    

while True:
    ws = websocket.WebSocketApp("ws://10.255.255.254:2026/api", on_message=on_message)
    ws.run_forever()

    if elyse_response is not None:
        break

elyse_message = base64.b64encode(bytearray(elyse_response["msg"])).decode('utf-8')

move_azura_response = requests.post("http://10.255.255.254:2009/set_target", json={"target": "Azura Station"})
print("MoveAzura: " + str(move_azura_response.status_code))

arrived_at_station= False
while not arrived_at_station:
    arrived_at_station_response = requests.get("http://10.255.255.254:2011/stations_in_reach")
    print("ArrivedAtStation: " + str(arrived_at_station_response.status_code))
    arrived_at_station= arrived_at_station_response.json()["stations"].get("Azura Station", False)

azura_response = requests.post("http://10.255.255.254:2030/put_message", json={"sending_station": "Elyse Terminal", "base64data": elyse_message})