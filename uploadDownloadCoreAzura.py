import requests

url = "http://10.255.255.254:2027/receive"

upload = requests.post(url)

print(upload.status_code)
data = upload.json()

if data.get("kind") == "success" and data.get("received_messages"):
    msg_info = data["received_messages"][0]  
    msg = msg_info.get("data")    

StationX, StationY = 0, 0
x, y = 0, 0

while x != StationX and y != StationY:
    getPos = "http://10.255.255.254:2011/pos"
    pos = requests.get(getPos)

    data = pos.json()

    if data.get("kind") == "success" and "pos" in data:
        StationX = data["pos"]["x"]
        StationY = data["pos"]["y"]

    url = "http://10.255.255.254:2009/set_target"
    data = {
            "target": {
                "x":  x,
                "y": y
            }
        }
    response = requests.post(url, json=data)


import requests, base64, json

COMM = "http://10.255.255.254"
AZURA_PORT = 2030

payload = {
    "sending_station": "Core Station",  
    "base64data": msg
}

r = requests.post(f"{COMM}:{AZURA_PORT}/put_message",
                  data=json.dumps(payload),
                  headers={"Content-Type": "application/json"})

print(r.status_code, r.text)

