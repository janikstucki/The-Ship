import requests

url = "http://10.255.255.254:2011/sell"

data = {"station": "Nuku Station", "what": "Nuclear_Waste", "amount": 112}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())

