from pymongo import MongoClient
import requests
import uuid

client = MongoClient("mongodb://theship:theship1234@127.0.0.1:2021/theshipdb")
db = client.theshipdb
collection = db["vacuum-energy"]
id = str(uuid.uuid4())

while True:
    create_response = requests.post("http://10.255.255.254:2037/trigger_measurement", json={"request_id": id})
    print(create_response.status_code)
    
    while True: 
        state_response = requests.get(f"http://10.255.255.254:2037/measurements/{id}")

        if (state_response.json()["state"] == "measured"):
            collection.delete_many({})
            collection.insert_one({"data": state_response.json()["result"]})
            print(state_response.json())

            delete_response = requests.delete(f"http://10.255.255.254:2037/measurements/{id}")
            print(delete_response.status_code)

            id = str(uuid.uuid4())
            break