import requests

url = "http://10.255.255.254:2009/set_target"
data = {
    "target": {
    "x": -60000, "y": 9000
    }
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())







# import requests

# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -6792, "y": 6032}}) #Zurro Station
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": 666, "y": 666}}) #Illume Colony
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -8000, "y": -8000}}) #Dynamic
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -7863, "y": -7158}}) #Station 39-B
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -20000, "y": 38000}}) #Artemis Station
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -82599, "y": 89973}}) #Elyse Terminal
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -12522, "y": 11561}}) #Station 62-A
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": 49889, "y": 76728}}) #Platin Mountain
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -108503, "y": -108888}}) #Architect Colony
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -60000, "y": 9000}}) #Phantom Station
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -44603, "y": 45588}}) #Chron
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -96486, "y": -80625}}) #Nuku Station
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -11000, "y": -11000}}) #Aurora Station
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -53811, "y": -44487}}) #Fragilon Rock
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -51418, "y": -52559}}) #Magnon Rock
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -29259, "y": -76849}}) #Xyron Vex
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": 150000, "y": 150000}}) #Quest
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -21300, "y": 36300}}) #Uran Stone
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -21500, "y": 36500}}) #On Uran Stone
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -10000, "y": 20500}}) #On Gold Stone
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -95225, "y": -90623}}) #Aetherium Rock
# response = requests.post("http://10.255.255.254:2009/set_target", json={"target": {"x": -95375, "y": -90773}}) #On Aetherium Rock

# print(response.status_code)
# print(response.json())



# Core Station		0/0
# Vesta Station		10000/10000 
# Azura Station		-1000/1000
# Shangris Station	4783/-5664
# Station 12-A 		16600/-11200  
# Zurro Station 		-7907/2619
# Artemis Station 	-20000/38000
# Elyse Terminal 		-62909/-55808
# Relief Station 		150000/150000
# Arak Station 		2175/2990
# Arakrock 		-13665/-15380
# Illume Colony		600/600
# Nuku Station 		"x": -96486, "y": -80625
# Aurora Station 		-11000/-11000
# Station 12-B 		-10271/18765

# Gold Stone 		-10000/20500
# Platin Mountain 	50233/77626
# Chron 			39006/38652
# Fragilon Rock 		45081/-40991
# Magnon Rock 		-55850/-58879

