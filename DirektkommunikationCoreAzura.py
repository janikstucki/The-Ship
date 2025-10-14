import requests, json, time

COMM = "http://10.255.255.254"
CORE_SEND_URL = f"{COMM}:2027/send"
CORE_RECEIVE_URL = f"{COMM}:2027/receive"
AZURA_PUT_URL = f"{COMM}:2030/put_message"
AZURA_GET_URL = f"{COMM}:2030/messages_for_other_stations"

sent_core_msgs = set()
sent_azura_msgs = set()

while True:
    downloadCore = requests.post(CORE_RECEIVE_URL)
    dataCore = downloadCore.json()
    if dataCore.get("kind") == "success":
        for msg_info in dataCore.get("received_messages", []):
            msg = msg_info.get("data")
            if msg and msg not in sent_core_msgs:
                print("Core → Azura:", msg)
                payload = {"sending_station": "Core Station", "base64data": msg}
                r = requests.post(AZURA_PUT_URL, json=payload)
                print("Upload zu Azura:", r.status_code)
                sent_core_msgs.add(msg)

    downloadAzura = requests.get(AZURA_GET_URL)
    dataAzura = downloadAzura.json()
    if dataAzura.get("kind") == "success":
        for msg_info in dataAzura.get("received_messages", []):
            msg = msg_info.get("base64data")
            if msg and msg not in sent_azura_msgs:
                print("Azura → Core:", msg)
                payload = {"source": "Azura Station", "message": msg}
                r = requests.post(CORE_SEND_URL, json=payload)
                print("Upload zu Core:", r.status_code)
                sent_azura_msgs.add(msg)

    time.sleep(0.5)
