# streamlit_app.py

import streamlit as st
from rag_pipeline.pipeline import run_query
from logger import log_query_response
from threat_detection.model import ThreatDetector
from threat_detection.attack_graph import AttackGraph
from adversarial.detector import is_malicious
from datetime import datetime

st.set_page_config(page_title="Secure Agentic AI", layout="wide")
st.title("🔒 Secure Agentic AI Dashboard")

# ── Sidebar: Threat Detection ──────────────────────────────────────────────
st.sidebar.header("Threat Detection")
uploaded = st.sidebar.file_uploader("Telemetry JSONL", type="jsonl")
if uploaded:
    detector = ThreatDetector()
    try:
        results = detector.detect_from_logs(uploaded)
        if results:
            st.sidebar.error(f"⚠️ Detected {len(results)} events")
            st.sidebar.json(results)
        else:
            st.sidebar.success("No threats detected")
    except Exception as e:
        st.sidebar.error(f"Error in threat detection: {e}")

# ── Main: RAG Query ────────────────────────────────────────────────────────
query = st.text_area("Enter security query:", height=100)
if st.button("Run Query"):
    if not query.strip():
        st.warning("Enter a query.")
    elif is_malicious(query):
        st.error("Prompt flagged as potentially malicious. Please revise.")
    else:
        with st.spinner("Running RAG…"):
            try:
                answer = run_query(query)
                log_query_response(query, answer)
                st.subheader("🔍 RAG Answer")
                st.write(answer)
            except Exception as e:
                st.error(f"Error running RAG: {e}")

# ── Attack Path Visualization ─────────────────────────────────────────────┐
st.markdown("---")
st.subheader("🗺️ Attack Path")
ag = AttackGraph()

# Build lists of names
nodes     = ag.graph.nodes(data=True)
intrusion = [(nid, d["name"]) for nid, d in nodes if d.get("type") == "intrusion-set"]
patterns  = [(nid, d["name"]) for nid, d in nodes if d.get("type") == "attack-pattern"]

intrusion_names = [name for _, name in intrusion]
pattern_names   = [name for _, name in patterns]

if intrusion_names and pattern_names:
    src = st.selectbox("APT Group", intrusion_names)
    tgt = st.selectbox("Technique", pattern_names)

    # Map back to IDs
    name_to_id = {name: nid for nid, name in intrusion + patterns}
    src_id = name_to_id.get(src)
    tgt_id = name_to_id.get(tgt)

    if st.button("Compute Path"):
        if not src_id or not tgt_id:
            st.error("Invalid selection. Please pick both a group and a technique.")
        else:
            try:
                path = ag.find_shortest_path(src_id, tgt_id)
                path_names = [ag.get_node_name(n) for n in path]
                st.write(" → ".join(path_names))
            except Exception as e:
                st.error(f"Could not compute path: {e}")
else:
    st.info("No intrusion-sets or attack-patterns loaded. Have you cloned CTI data?")

st.caption(f"© Athenian Tech | {datetime.now().year}")
