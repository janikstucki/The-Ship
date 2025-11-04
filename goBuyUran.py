import requests 
import time 

def travel_to(x, y):
    url = "http://10.255.255.254:2009/set_target"
    data = {
        "target": {
        "x": x, "y": y
        }
    }
    response = requests.post(url, json=data)
    print(response.status_code)
    print(response.json())

def get_pos():
    posresponse = requests.get("http://10.255.255.254:2010/pos")

    posdata = posresponse.json()

    posx = posdata["pos"]["x"]
    posy = posdata["pos"]["y"]
    return posx, posy

posx = None
posy = None

while True:
    response = requests.get("http://10.255.255.254:2012/hold")

    data = response.json()

    uran = data["hold"]["resources"]["URAN"]
    print(uran)


    if uran == 7:
        if posx is None and posy is None:
            posx, posy = get_pos()
            print(posx, posy)
        travel_to(-108503, -108888)
        time.sleep(10)
        get_near_stations = requests.get("http://10.255.255.254:2011/stations_in_reach")

        while get_near_stations.status_code != 200:
            time.sleep(1)
            get_near_stations = requests.get("http://10.255.255.254:2011/stations_in_reach")
            print(get_near_stations.status_code)
            
        if get_near_stations.status_code == 200:
            requests.post("http://10.255.255.254:2011/buy", json={"station": "Architect Colony", "what": "URAN", "amount": 1})
            travel_to(posx, posy)