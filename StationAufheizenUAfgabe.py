import requests
import time

while True:
    url = "http://10.255.255.254:2018/activate"

    response = requests.post(url)

    print(response.status_code)
    print(response.json())
    time.sleep(9)

