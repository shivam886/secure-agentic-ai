# rag_pipeline/document_loader.py

from pathlib import Path
from langchain_community.document_loaders import TextLoader, UnstructuredPDFLoader

def load_corpus_documents(data_path: str = "data/rag_corpus/"):
    docs = []
    for fp in Path(data_path).rglob("*"):
        suffix = fp.suffix.lower()
        if suffix in {".txt", ".md", ".markdown"}:
            docs.extend(TextLoader(str(fp)).load())
        elif suffix == ".pdf":
            docs.extend(UnstructuredPDFLoader(str(fp)).load())
    return docs
