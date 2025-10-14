import requests
import time
url = "http://10.255.255.254:2029/receive"

message = requests.post(url)

print(message.status_code)
print(message.json())

goto = "http://10.255.255.254:2009/set_target"
data = {
    "target": {
        "x":  -1000.0,
        "y": 1000.0
    }
}

response = requests.post(goto, json=data)

print(response.status_code)
print(response.json())

time.sleep(50)

#upload

uploadUrl = "http://10.255.255.254:2030/put_message" 

msg = {"src": "Shangris Station", "msg": message}


upload = requests.post(uploadUrl, json=msg)

print(upload.status_code)
print(upload.json())