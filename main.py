# main.py

from rag_pipeline.pipeline import run_query
from rich import print

if __name__ == "__main__":
    q = "What is the Phishing technique in MITRE ATT&CK?"
    ans = run_query(q)
    print("[bold green]Query:[/bold green]", q)
    print("[bold blue]Answer:[/bold blue]", ans)
