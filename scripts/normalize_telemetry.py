#!/usr/bin/env python3
import json, os
from datetime import datetime

INFILE  = "data/telemetry/telemetry_logs.jsonl"
OUTFILE = "data/telemetry/normalized_logs.jsonl"

os.makedirs(os.path.dirname(OUTFILE), exist_ok=True)

with open(INFILE) as fin, open(OUTFILE, "w") as fout:
    for line in fin:
        try:
            ev = json.loads(line)
        except json.JSONDecodeError:
            continue
        # Add normalization fields
        ev["tenant_id"]   = "tenant‑alpha"
        ev["source_type"] = "sensor‑process"
        # Ensure timestamp is ISO
        # ev["timestamp"] = datetime.fromisoformat(ev["timestamp"].rstrip("Z")).isoformat() + "Z"
        fout.write(json.dumps(ev) + "\n")
print(f"Wrote normalized telemetry to {OUTFILE}")


