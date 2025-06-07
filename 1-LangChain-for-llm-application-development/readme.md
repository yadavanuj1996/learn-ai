# Theory 
## RAG, or Retrieval-Augmented Generation

<img width="726" alt="Screenshot 2025-06-07 at 7 20 13 PM" src="https://github.com/user-attachments/assets/4a92d0e6-4ad4-46f0-8331-1b8c3d859aa0" />

RAG stands for Retrieval-Augmented Generation.

It's an approach used in AI systems—especially with LLMs (Large Language Models)—to improve their accuracy and relevance by combining retrieval of external documents with text generation.

#### Components in RAG System
| Component               | Description                                                                     |
| ----------------------- | ------------------------------------------------------------------------------- |
| **LLM**                 | Generates answers (e.g., GPT-4, LLaMA, Mistral).                                |
| **Retriever**           | Finds relevant documents from a data source (often using vector embeddings).    |
| **Vector DB**           | Stores pre-processed documents as embeddings (e.g., Pinecone, Weaviate, FAISS). |
| **Embedding Model**     | Converts text into numerical vectors for semantic search.                       |
| **Reranker (optional)** | Ranks retrieved docs for higher relevance before passing to LLM.                |




# setup

1. python3 -m venv backend-ve
2. source ./backend/be/activate
2. pip install -r requirements.txt
