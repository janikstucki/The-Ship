import socket
import requests

HOST = '0.0.0.0'
PORT = 2103

response = requests.get("http://10.255.255.254:2041/data")
data = response.json()
measurement_hex = data["measurement"]


scanner_bytes = bytes.fromhex(measurement_hex)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Engine Overdrive Server läuft auf {HOST}:{PORT}...")

while True:
    client_socket, addr = server_socket.accept()
    print(f"Verbindung von {addr} akzeptiert.")

    try:
        client_socket.sendall(scanner_bytes)
        print(f"{len(scanner_bytes)} Bytes gesendet an {addr}.")
    except Exception as e:
        print(f"Fehler beim Senden: {e}")
    finally:
        client_socket.close()  
