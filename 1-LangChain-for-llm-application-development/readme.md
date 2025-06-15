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



### Failure Modes:
1. Duplicate data in multiple documents
    - Le's say if we input two same documents in input, so after splitting and embedding it gets stored in vector db.
    - Once we retrieve a relevant document by similarity of the vector embeddings between input query and stored document splits
    - If there are duplicate input documents same content will be pulled back, ideally we would want syntactically closer and distinct document splits (so that we can pass it to LLM)
2. Equal weightage to whole sentence
    - Let's say we input a search query (Get me details about regression from document 3), this will focus equally on regression and document 3 thus this query will return documents containing info related to regression even if they are on documents other than document 3.
    


# setup

1. python3 -m venv backend-ve
2. source ./backend/be/activate
2. pip install -r requirements.txt
