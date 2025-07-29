from rag_architecture.rag_pipeline import run_query
from rich import print

query = "How is sensitive data protected in Athenian agents?"
result = run_query(query)

print("\n[bold blue]🔍 RAG Result from Ollama:[/bold blue]")
print(result)
