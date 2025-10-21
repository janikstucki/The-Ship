from opcua import ua, Server

# 1. Server erstellen
server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:2035/")


# 2. NodeSet laden
server.import_xml("/home/janik/Documents/Code/jumpdrive/jumpdrive.xml")  # hier dein XML

# 3. Starten
server.start()
print("Server läuft auf opc.tcp://0.0.0.0:2035/")

try:
    while True:
        pass  # Server läuft endlos
finally:
    server.stop()
    print("Server gestoppt")
