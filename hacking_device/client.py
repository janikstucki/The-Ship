#!/usr/bin/env python3
import grpc
import api_pb2
import api_pb2_grpc
import json
from datetime import datetime

SERVER = "10.255.255.254:2028"
API_KEY = "hackhack-x1337"  # benutze HackHack-Key
OUTFILE = "station_dump.json"

def fetch_and_save():
    channel = grpc.insecure_channel(SERVER)
    stub = api_pb2_grpc.HackingDeviceServerStub(channel)
    metadata = (("x-api-key", API_KEY),)
    try:
        resp = stub.read_secret_station_data(api_pb2.Void(), metadata=metadata, timeout=10)
    except grpc.RpcError as e:
        print("RPC failed:", e.code(), e.details())
        return

    data_items = []
    for s in resp.data:
        try:
            data_items.append(json.loads(s))
        except Exception:
            # falls kein JSON -> als raw String speichern
            data_items.append({"raw": s})

    output = {
        "fetched_at": datetime.utcnow().isoformat() + "Z",
        "server": SERVER,
        "items": data_items
    }

    with open(OUTFILE, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"Wrote {len(data_items)} items to {OUTFILE}")

if __name__ == "__main__":
    fetch_and_save()