import streamlit as st
from rag_architecture.rag_pipeline import run_query
from datetime import datetime

st.set_page_config(page_title="Secure Agentic AI - RAG", layout="centered")

st.title("🤖 Secure Agentic AI - RAG Chat (Local Ollama)")

# Input from user
query = st.text_area("Enter your security-related query:", height=100)

if st.button("Run Query"):
    if not query.strip():
        st.warning("Please enter a valid query.")
    else:
        with st.spinner("Running RAG query on local LLM..."):
            try:
                response = run_query(query)
                st.success("✅ Response generated:")
                st.markdown(f"**Answer:** {response}")
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")

st.markdown("---")
st.caption(f"© Athenian Tech | {datetime.now().year}")
