#!/usr/bin/env python3
import requests, os

feeds = {
    "apt41_iocs": "https://example.com/apt41_iocs.csv",
    "apt41_ttps": "https://example.com/apt41_ttps.csv"
}

os.makedirs("data/iocs_ttps", exist_ok=True)
for name, url in feeds.items():
    r = requests.get(url)
    with open(f"data/iocs_ttps/{name}.csv", "wb") as f:
        f.write(r.content)
