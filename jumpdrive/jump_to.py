from opcua import Client

# 1. Client verbinden
client = Client("opc.tcp://127.0.0.1:2035/")  # oder Server-IP
client.connect()

try:
    # 2. Jumpdrive Node abrufen
    jumpdrive = client.get_node("ns=0;i=20001")  # NodeId von Jumpdrive
    jump_to_method = client.get_node("ns=0;i=20002")  # JumpTo Methode

    # 3. Methode aufrufen: x=10, y=20 z.B.
    result = jumpdrive.call_method(jump_to_method, -20000, 0)

    print("Sprung erfolgreich?", result)

finally:
    client.disconnect()
