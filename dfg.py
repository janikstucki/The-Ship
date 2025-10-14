import requests

def set_thrust(url, thrust_percent):
    data = {"thrust_percent": thrust_percent}
    requests.put(url, json=data)


set_thrust("http://10.255.255.254:2003/thruster", 100)  

