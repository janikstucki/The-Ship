from opcua import Client

client = Client("opc.tcp://127.0.0.1:2035/")  
client.connect()

try:
    jumpdrive = client.get_node("ns=0;i=20001")  
    jump_to_method = client.get_node("ns=0;i=20002")  

    result = jumpdrive.call_method(jump_to_method, -20000, 0)

    print("Sprung erfolgreich?", result)

finally:
    client.disconnect()
