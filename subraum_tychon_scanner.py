import requests
import re
import time
import json

LOG_URL = "http://10.255.255.254:2041/status"
SOLUTION_URL = "http://10.255.255.254:2041/solution"

def fetch_logs():
    resp = requests.get(LOG_URL)
    resp.raise_for_status()
    data = resp.json()
    # Robust auf Logs prüfen
    if 'log' in data:
        return data['log']
    elif 'tip_for_next_try' in data and 'log' in data['tip_for_next_try']:
        return data['tip_for_next_try']['log']
    return []

def parse_times(line):
    # Gibt Liste von ints zurück, nur die Werte
    matches = re.findall(r'\d+:\s*(\d+)', line)
    return list(map(int, matches))

def find_bug_line(logs):
    for line in logs:
        if '---DETECTED BUG---' in line:
            return line
    return None

def is_candidate(bug_times, line_times):
    if len(bug_times) != len(line_times):
        return False
    smaller_found = False
    for b, l in zip(bug_times, line_times):
        if l < b:
            smaller_found = True
        elif l > b:
            return False
    return smaller_found

def main():
    while True:
        try:
            logs = fetch_logs()
            bug_line = find_bug_line(logs)
            if not bug_line:
                print("Keine Bug-Zeile gefunden.")
                time.sleep(1)
                continue
            
            bug_times = parse_times(bug_line)
            N = len(bug_times)

            solution = []
            for line in logs:
                line_times = parse_times(line)
                if len(line_times) == N and is_candidate(bug_times, line_times):
                    solution.append(line)

            if solution:
                payload = json.dumps(solution)
                resp = requests.post(SOLUTION_URL, data=payload)
                print(resp.text)
                
            if not solution:
                solution = ["NO_CANDIDATE_FOUND"]
            payload = json.dumps(solution)
            requests.post(SOLUTION_URL, data=payload)


        except Exception as e:
            print("Fehler:", e)
        time.sleep(1)

if __name__ == "__main__":
    main()