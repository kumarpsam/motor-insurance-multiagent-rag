# motor-insurance-multiagent-rag
=======
# Motor Insurance Multi-Agent + RAG System

This project demonstrates a planner-driven multi-agent architecture combined with FAISS-based Retrieval Augmented Generation (RAG) using a local LLM.

## Features
- Planner-based agent routing
- Policy validation using RAG
- Fraud risk assessment
- Deterministic decision output
- Local LLM via Ollama
- FAISS vector search

## Tech Stack
- Python 3.12
- Ollama (Phi-3 Mini)
- FAISS
- Sentence Transformers
- Modular multi-agent design

## Architecture
User → Planner → Policy (RAG) → Risk → Decision
