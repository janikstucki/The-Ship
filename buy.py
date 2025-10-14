import requests

url = "http://10.255.255.254:2011/buy"

data = {"station": "Vesta Station", "what": "IRON", "amount": 24}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

