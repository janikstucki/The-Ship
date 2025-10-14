import requests
import xmlrpc.client
import base64

artemis_xmlrpc = xmlrpc.client.ServerProxy("http://10.255.255.254:2024/RPC2")
[artemis_response] = artemis_xmlrpc.receive()
artemis_response[1] = base64.b64encode(artemis_response[1].data).decode('utf-8')
print("Artemis Messages: " + str(artemis_response))

# move_azura_response = requests.post("http://10.255.255.254:2009/set_target", json={"target": "Azura Station"})
# print("MoveAzura: " + str(move_azura_response.status_code))

# arrived_at_station= False
# while not arrived_at_station:
#     arrived_at_station_response = requests.get("http://10.255.255.254:2011/stations_in_reach")
#     print("ArrivedAtCore: " + str(arrived_at_station_response.status_code))
#     arrived_at_station= arrived_at_station_response.json()["stations"].get("Azura Station", False)

# azura_response = requests.post("http://10.255.255.254:2030/put_message", json={"sending_station": "Artemis Station", "base64data": artemis_response[1]})