import random
import string
from http.server import BaseHTTPRequestHandler, HTTPServer
import requests
import threading
import time

PORT = 2104
cached_data = "000000"  # hex-only

MAX_LEN = 40  # je nach Laser

def update_sensor_data():
    global cached_data
    while True:
        try:
            resp = requests.post("http://10.255.255.254:2104/measure", timeout=5)
            sensor_raw = resp.text.strip() or "000000"
            
            # Nur Ziffern behalten
            filtered = ''.join(c for c in sensor_raw if c in '0123456789')
            
            # Feste Länge, Fallback mit Nullen
            if len(filtered) < MAX_LEN:
                filtered = filtered.ljust(MAX_LEN, '0')
            else:
                filtered = filtered[:MAX_LEN]

            cached_data = filtered
            print(f"[AMPLIFIER] Sensor gefiltert: {cached_data}")
        except Exception as e:
            print("[AMPLIFIER] Sensorfehler:", e)
            cached_data = '0' * MAX_LEN

        time.sleep(5)


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(cached_data.encode())

if __name__ == "__main__":
    threading.Thread(target=update_sensor_data, daemon=True).start()
    server = HTTPServer(('0.0.0.0', PORT), Handler)
    print(f"🚀 Laser-Amplifier-Server läuft auf Port {PORT}")
    server.serve_forever()
