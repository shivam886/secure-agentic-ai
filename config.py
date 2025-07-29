# config.py

# Where your RAG corpus lives
DATA_PATH   = "data/rag_corpus/"

# Where your MITRE STIX data lives
CTI_PATH    = "cti/enterprise-attack"

# Where to write/load your FAISS index
INDEX_PATH  = "faiss_index"

# Ollama model name
LLM_MODEL   = "llama3"

# HuggingFace embedding model name
EMBED_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
