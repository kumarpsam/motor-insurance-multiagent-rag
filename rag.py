import faiss
import numpy as np
from sentence_transformers import SentenceTransformer

# Load embedding model (lightweight)
model = SentenceTransformer("all-MiniLM-L6-v2")

# Read policy document
with open("data/motor_policy.txt", "r", encoding="utf-8") as f:
    document_text = f.read()

# Split into simple chunks (basic split)
documents = document_text.split("\n\n")

# Generate embeddings
doc_embeddings = model.encode(documents)

# Convert to float32 for FAISS
doc_embeddings = np.array(doc_embeddings).astype("float32")

# Create FAISS index
dimension = doc_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(doc_embeddings)

def retrieve_context(query, top_k=2):
    query_embedding = model.encode([query]).astype("float32")
    distances, indices = index.search(query_embedding, top_k)

    results = [documents[i] for i in indices[0]]
    return "\n".join(results)
