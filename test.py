# python3 - << 'EOF'
import io, sys

path = "data/telemetry/telemetry_logs.jsonl"
print("=== Raw file bytes ===")
with open(path, "rb") as f:
    b = f.read()
    print(repr(b[:200]), "…")           # show first 200 bytes
print("\n=== Line‑by‑line repr() ===")
with open(path, "r", encoding="utf-8", errors="replace") as f:
    for i, line in enumerate(f, 1):
        print(f"{i}: {repr(line)}")
        if i >= 5: break

