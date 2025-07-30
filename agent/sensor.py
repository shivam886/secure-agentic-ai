import time
import json
from datetime import datetime
import psutil

AGENT_ID = "agent-1"
LOG_FILE = "data/telemetry/telemetry_logs.jsonl"
INTERVAL_SECONDS = 60

def collect_process_events():
    events = []
    for proc in psutil.process_iter(['pid', 'name', 'username']):
        info = proc.info
        events.append({
            "timestamp": datetime.now().isoformat() + "Z",
            "agent_id": AGENT_ID,
            "event_type": "process_start",
            "pid": info['pid'],
            "name": info['name'],
            "username": info.get('username')
        })
    return events

def main():
    # Continuously collect and append events
    with open(LOG_FILE, 'a') as f:
        while True:
            events = collect_process_events()
            for e in events:
                f.write(json.dumps(e) + "\\n")
            time.sleep(INTERVAL_SECONDS)

if __name__ == "__main__":
    main()