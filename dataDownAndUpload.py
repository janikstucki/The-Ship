import time, sys, requests

GAME = "http://10.0.2.15"
COMM = "http://10.255.255.254"
ZURRO, ZURRO_POS, ZURRO_PORT = "Zurro Station", {"x": -6792, "y": 6032}, 2029
AZURA, AZURA_POS, AZURA_PORT = "Azura Station", {"x": -1000, "y": 1000}, 2030

def set_target(t): requests.post(f"{GAME}:2009/set_target", json={"target": t}, timeout=5)
def in_reach(n):
    try: s = requests.get(f"{GAME}:2011/stations_in_reach", timeout=5).json().get("stations",{})
    except: return False
    return n in s
def wait(n, sec=180):
    for _ in range(sec):
        if in_reach(n): return True
        time.sleep(1)
    print("Timeout:", n); return False

# 1) Nachricht holen
set_target(ZURRO_POS); wait(ZURRO)
rec = requests.post(f"{COMM}:{ZURRO_PORT}/receive", json={}, timeout=5).json()
msgs = rec.get("received_messages", [])
b64 = next((m["msg"] for m in msgs if m.get("dest")==AZURA and "msg" in m), None)
if not b64:
    print("Keine Nachricht für Azura bei Zurro gefunden."); sys.exit(1)
print("[OK] Base64 geholt (gekürzt):", b64[:40] + ("..." if len(b64)>40 else ""))

# 2) Nachricht hochladen
set_target(AZURA_POS); wait(AZURA)
payload = {"sending_station": ZURRO, "base64data": b64}
requests.post(f"{COMM}:{AZURA_PORT}/put_message", json=payload, timeout=5).raise_for_status()
print("Fertig: Daten bei Azura hochgeladen.")