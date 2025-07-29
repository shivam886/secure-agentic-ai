# rag_pipeline/stix_loader.py

from stix2 import FileSystemSource, Filter
from langchain.schema import Document

def load_stix_documents(cti_path: str = "cti/enterprise-attack"):
    """
    Load MITRE ATT&CK attack‑pattern objects from the STIX JSON folder
    and return them as LangChain Document instances.
    """
    fs = FileSystemSource(cti_path)
    patterns = fs.query([Filter("type", "=", "attack-pattern")])
    docs = []
    for pat in patterns:
        name = pat.get("name", "")
        desc = pat.get("description", "") or ""
        content = f"{name}\n\n{desc}"
        docs.append(Document(
            page_content=content,
            metadata={"id": pat.id, "name": name, "source": "mitre_attack"}
        ))
    return docs
