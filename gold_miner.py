import requests
import time

mining_coordinates = {"x": 50000, "y": 76540}  # Uran Stone
station_name = "Core Station"
station_coordinates = {"x": 0, "y": 0}

def get_storage():
    storage_response = requests.get("http://10.255.255.254:2012/hold")
    return storage_response.json()["hold"]

while True:
    # 1️⃣ Zum Mining-Spot fliegen
    move_gold_response = requests.post("http://10.255.255.254:2009/set_target", json={"target": mining_coordinates})
    print("MoveUran:", move_gold_response.status_code)

    arrived_at_gold = False
    while not arrived_at_gold:
        pos_resp = requests.get("http://10.255.255.254:2010/pos")
        vel = pos_resp.json()["velocity"]
        arrived_at_gold = abs(vel["x"]) < 0.1 and abs(vel["y"]) < 0.1
        time.sleep(1)

    # 2️⃣ Mining starten
    free_storage = get_storage()["hold_free"]
    mining_angle = 350
    last_activation = 0

    while free_storage > 0:
        # Laser ausrichten & aktivieren
        requests.put("http://10.255.255.254:2018/angle", json={"angle": mining_angle})
        if time.time() - last_activation >= 10:
            laser_response = requests.post("http://10.255.255.254:2018/activate")
            print("Laser aktiviert:", laser_response.status_code)
            last_activation = time.time()

        # Mining-Status prüfen
        state_resp = requests.get("http://10.255.255.254:2018/state").json()
        if not state_resp["is_mining"]:
            mining_angle += 10
            if mining_angle == 360:
                mining_angle = 0
            print("Kein Mining – Winkel geändert auf", mining_angle)

        free_storage = get_storage()["hold_free"]

    # 3️⃣ Zur Station fliegen
    move_core_response = requests.post("http://10.255.255.254:2009/set_target", json={"target": station_coordinates})
    print("MoveCore:", move_core_response.status_code)

    arrived_at_core = False
    while not arrived_at_core:
        resp = requests.get("http://10.255.255.254:2011/stations_in_reach")
        arrived_at_core = resp.json()["stations"].get(station_name, False)

    # 4️⃣ Verkaufen
    storage = get_storage()
    while storage["hold_free"] != 120:
        resources = storage["resources"]
        gold = resources.get("GOLD", 0)
        if gold > 0:
            requests.post("http://10.255.255.254:2011/sell", json={"station": station_name, "what": "GOLD", "amount": gold})
            print("Sell Gold:", gold)

        for res in ["STONE", "IRON", "PLATIN"]:
            requests.post("http://10.255.255.254:2011/sell", json={"station": station_name, "what": res, "amount": 120})
            print("Sell", res)

        storage = get_storage()

