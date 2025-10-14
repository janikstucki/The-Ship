import requests

url = "http://10.255.255.254:2011/sell"

data = {"station": "Core Station", "what": "IRON", "amount": 24}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

