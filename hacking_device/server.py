#!/usr/bin/env python3
import logging
import sys
from concurrent import futures
import grpc
import api_pb2
import api_pb2_grpc
from grpc import StatusCode
import datetime
import json

# === Konfiguration ===
BIND_ADDR = "10.255.255.254:2028"
# Keys: 'hackhack-x1337' ist der HackHack-Key, 'foobar' ist dev
VALID_API_KEYS = {"foobar", "hackhack-x1337"}
LOGFILE = "./hacking_device.log"

# === Logging (robust, fallback auf stdout) ===
logger_handlers = [logging.StreamHandler(sys.stdout)]
try:
    fh = logging.FileHandler(LOGFILE)
    logger_handlers.insert(0, fh)
except Exception as e:
    print(f"Could not open logfile {LOGFILE}: {e}", file=sys.stderr)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
    handlers=logger_handlers
)

# === Hilfsfunktionen ===
def _now_iso():
    return datetime.datetime.utcnow().replace(microsecond=0).isoformat() + "Z"

def make_secret_data():
    """
    Simuliert die 'geheimen' Daten einer Phantom Station:
    - NFT clone events
    - suspicious accounts
    - file pointers
    """
    # fiktive Einträge (du kannst das beliebig anpassen)
    entries = [
        {
            "type": "nft_clone_event",
            "nft_id": "PHANTOM-0001",
            "original_owner": "artist_neo",
            "cloned_by": "wallet_0xDECAFBAD",
            "timestamp": _now_iso(),
            "evidence": "ipfs://QmFakeHash1"
        },
        {
            "type": "nft_clone_event",
            "nft_id": "PHANTOM-0099",
            "original_owner": "pixel_witch",
            "cloned_by": "wallet_0xDECAFBAD",
            "timestamp": _now_iso(),
            "evidence": "ipfs://QmFakeHash2"
        },
        {
            "type": "suspicious_account",
            "account": "wallet_0xDECAFBAD",
            "score": 0.92,
            "notes": "Multiple clones + marketplace listings on black market",
            "first_seen": _now_iso()
        },
        {
            "type": "file_dump",
            "path": "/station/data/export_2025-10-28.json",
            "size_bytes": 12345,
            "note": "Contains transfer logs and file manifests"
        },
        {
            "type": "intel",
            "summary": "Suggested next hop: investigate marketplace 'DarkSell' and IPFS hash QmFakeHash2"
        }
    ]
    # Return als strings (proto erwartet repeated string)
    return [json.dumps(e) for e in entries]

# === gRPC Servicer ===
class HackingDeviceServerServicer(api_pb2_grpc.HackingDeviceServerServicer):
    def read_secret_station_data(self, request, context):
        md_list = context.invocation_metadata() or []
        md = {k: v for (k, v) in md_list}
        api_key = md.get("x-api-key") or md.get("x-api-key".encode()) or None

        peer = context.peer()
        if not api_key:
            logging.warning("Rejected request: missing X-API-KEY metadata. caller=%s", peer)
            context.abort(StatusCode.UNAUTHENTICATED, "invalid x-api-key: missing")
        if api_key not in VALID_API_KEYS:
            logging.warning("Rejected request: invalid X-API-KEY '%s' from %s", api_key, peer)
            context.abort(StatusCode.UNAUTHENTICATED, "invalid x-api-key")

        logging.info("Accepted request from %s (key ok=%s)", peer, api_key)
        data_lines = make_secret_data()
        logging.info("Serving %d data items for %s", len(data_lines), peer)
        return api_pb2.SecretStationDataResponse(data=data_lines)

# === Server bootstrap ===
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=8))
    api_pb2_grpc.add_HackingDeviceServerServicer_to_server(HackingDeviceServerServicer(), server)
    server.add_insecure_port(BIND_ADDR)
    server.start()
    logging.info("gRPC server listening on %s", BIND_ADDR)
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        logging.info("Shutting down server...")
        server.stop(0)

if __name__ == "__main__":
    serve()