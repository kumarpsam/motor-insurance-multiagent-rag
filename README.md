# 🚗 Motor Insurance Multi-Agent + RAG System

This project demonstrates a **planner-driven multi-agent architecture** integrated with **Retrieval-Augmented Generation (RAG)** using a fully local LLM setup.

The system simulates a UK Motor Insurance claim triage system with modular AI agents.

---

## 🧠 Architecture Overview

The system follows a planner-based orchestration model:

                  ┌─────────────┐
                  │    User     │
                  └──────┬──────┘
                         │
                         ▼
                  ┌─────────────┐
                  │   Planner   │
                  │    Agent    │
                  └──────┬──────┘
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼
   ┌─────────────┐              ┌─────────────┐
   │ Policy Agent│              │ Risk Agent  │
   │    (RAG)    │              │             │
   └──────┬──────┘              └──────┬──────┘
          │                             │
          └──────────────┬──────────────┘
                         │
                         ▼
                  ┌─────────────┐
                  │  Decision   │
                  │    Agent    │
                  └─────────────┘


---

## 🔎 How RAG Works

1. Policy documents are embedded using `SentenceTransformers`
2. Embeddings are stored in a FAISS vector index
3. User claim query retrieves relevant policy clauses
4. Retrieved context is injected into the Policy Agent prompt
5. LLM generates a context-aware validation decision

---

## ⚙️ Tech Stack (POC Version)

- Python 3.12
- Ollama (Local LLM runtime)
- Phi-3 Mini model
- FAISS (Vector Search)
- Sentence Transformers (Embeddings)
- Modular Multi-Agent Architecture
- Planner-driven routing logic

All running locally on an 8GB laptop.

---

## 🚀 Features

- Planner-based conditional agent routing
- Policy validation using RAG
- Fraud risk assessment agent
- Deterministic decision output (APPROVE / REJECT / ESCALATE)
- Token control and response constraints
- Fully open-source stack

---

## ▶️ How to Run

### 1️⃣ Install Ollama
Download and install from:
https://ollama.com

Pull model:
ollama pull phi3:mini
---

### 2️⃣ Create Virtual Environment
python -m venv venv
.\venv\Scripts\Activate

---

### 3️⃣ Install Dependencies
pip install -r requirements.txt

---

### 4️⃣ Run Application
python main.py


Example input:
Policy started 5 days ago.
Accident today.
Claim amount £15000.


---

## 🏗 Enterprise Upgrade Path

To productionize this system:

- Replace local LLM with Azure OpenAI / AWS Bedrock
- Add API layer using FastAPI
- Add PostgreSQL for persistent storage
- Add Redis for caching
- Deploy via Docker + Kubernetes
- Add authentication (OAuth / OIDC)
- Add monitoring (Prometheus / CloudWatch)

---

## 📌 Purpose

This project demonstrates how:

- Multi-agent orchestration
- Retrieval-Augmented Generation
- Deterministic LLM control
- Modular architecture

can form the foundation of enterprise-grade AI systems in regulated industries like insurance.

---

## 📂 Repository Structure

motor-insurance-multiagent-rag/
│
├── agents/
├── data/
├── rag.py
├── llm.py
├── main.py
├── requirements.txt
└── README.md


---

## 📜 License

Open-source project for learning and demonstration purposes.

