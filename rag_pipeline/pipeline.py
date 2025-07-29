# rag_pipeline/pipeline.py

import config
from rag_pipeline.document_loader import load_corpus_documents
from rag_pipeline.stix_loader   import load_stix_documents
from langchain.text_splitter    import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms    import Ollama
from langchain.chains            import RetrievalQA

def load_documents():
    # load your local docs + MITRE STIX
    docs = load_corpus_documents(config.DATA_PATH)
    docs.extend(load_stix_documents(config.CTI_PATH))
    splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return splitter.split_documents(docs)

def create_vector_store(docs):
    emb = HuggingFaceEmbeddings(model_name=config.EMBED_MODEL)
    db  = FAISS.from_documents(docs, emb)
    db.save_local(config.INDEX_PATH)
    return db

def run_query(query: str) -> str:
    """
    1) Load + chunk all docs
    2) Build (or overwrite) FAISS index
    3) Run RetrievalQA chain on Ollama
    """
    docs = load_documents()
    vs   = create_vector_store(docs)
    qa   = RetrievalQA.from_chain_type(
        llm=Ollama(model=config.LLM_MODEL),
        retriever=vs.as_retriever()
    )
    return qa.run(query)
