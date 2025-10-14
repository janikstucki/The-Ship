import requests

url = "http://10.255.255.254:2009/set_target"
data = {
    "target": {
        "x":  -21500.0 ,
        "y": 36500.0
    }
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())




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
# Nuku Station 		-85936/-83194 
# Aurora Station 		-11000/-11000
# Station 12-B 		-10271/18765

# Gold Stone 		-10000/20500
# Platin Mountain 	50233/77626
# Chron 			39006/38652
# Fragilon Rock 		45081/-40991
# Magnon Rock 		-55850/-58879

