from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import random

last_measurement = []

class MyHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        global last_measurement
        if self.path == "/measure":
            last_measurement = [random.randint(0, 100) for _ in range(5)]
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"measurement": last_measurement}).encode())

    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            if last_measurement:
                # wie Laser-Amplifier erwartet
                data_str = "".join([f"{x:02}" for x in last_measurement])
                self.wfile.write(data_str.encode())
            else:
                self.wfile.write(b"no measurement yet")

def run(server_class=HTTPServer, handler_class=MyHandler):
    server_address = ('', 2104)
    httpd = server_class(server_address, handler_class)
    print("🚀 Server running on port 2104...")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
