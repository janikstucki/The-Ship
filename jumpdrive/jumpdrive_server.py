from opcua import ua, Server

server = Server()
server.set_endpoint("opc.tcp://0.0.0.0:2035/")


server.import_xml("/home/janik/Documents/Code/jumpdrive/jumpdrive.xml")  

server.start()
print("Server läuft auf opc.tcp://0.0.0.0:2035/")

try:
    while True:
        pass  
finally:
    server.stop()
    print("Server gestoppt")
