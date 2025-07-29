from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import TextLoader
from langchain_community.llms import Ollama

from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from pathlib import Path

def load_documents(data_path: str = "data/rag_corpus/"):
    text_files = list(Path(data_path).rglob("*.txt"))
    documents = []
    for file_path in text_files:
        loader = TextLoader(str(file_path))
        documents.extend(loader.load())
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    return text_splitter.split_documents(documents)

def create_vector_store(docs, index_path="faiss_index"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = FAISS.from_documents(docs, embeddings)
    db.save_local(index_path)
    return db

def load_vector_store(index_path="faiss_index"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return FAISS.load_local(index_path, embeddings)

def build_rag_pipeline(vectorstore):
    llm = Ollama(model="llama3")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=vectorstore.as_retriever())
    return qa_chain

def run_query(query: str):
    docs = load_documents()
    vs = create_vector_store(docs)
    qa = build_rag_pipeline(vs)
    result = qa.run(query)
    return result
