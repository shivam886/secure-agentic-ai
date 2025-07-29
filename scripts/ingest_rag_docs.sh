#!/usr/bin/env bash
# Copy your local .md/.pdf files into the RAG corpus
mkdir -p data/rag_corpus
cp ~/Documents/*.md data/rag_corpus/ 2>/dev/null || true
cp ~/Documents/*.pdf data/rag_corpus/ 2>/dev/null || true
