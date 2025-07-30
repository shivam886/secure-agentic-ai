#!/usr/bin/env python3

import json, os

INFILE  = "data/telemetry/telemetry_logs.jsonl"
OUTFILE = "data/telemetry/normalized_logs.jsonl"

os.makedirs(os.path.dirname(OUTFILE), exist_ok=True)

count_in  = 0
count_out = 0

with open(INFILE, "r") as fin, open(OUTFILE, "w") as fout:
    for line in fin:
        count_in += 1
        try:
            ev = json.loads(line)
        except json.JSONDecodeError as e:
            print("Skipping bad JSON:", e, line)
            continue
        # Add your metadata
        ev["tenant_id"]   = "tenant‑alpha"
        ev["source_type"] = "sensor‑process"
        fout.write(json.dumps(ev) + "\n")
        count_out += 1

print(f"Read  {count_in} lines from {INFILE}")
print(f"Wrote {count_out} lines to {OUTFILE}")
