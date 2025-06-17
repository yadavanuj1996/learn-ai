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



<img width="723" alt="Screenshot 2025-06-15 at 12 31 56 PM" src="https://github.com/user-attachments/assets/448fa6d8-d794-4787-b856-b95d7a1be6d4" />
<img width="723" alt="Screenshot 2025-06-15 at 12 32 22 PM" src="https://github.com/user-attachments/assets/1b10a775-7bcd-4082-b7b0-85ea5e1224d7" />
<img width="723" alt="Screenshot 2025-06-15 at 12 32 51 PM" src="https://github.com/user-attachments/assets/0ea5b808-5668-4125-974a-436a4cdf3b20" />

## Vector Store and Embeddings

#### What is a embedding
An embedding is a specific kind of vector — it's a list of numbers that represents something (like text) in a way that captures its meaning.

#### What is a "collection" in Chroma?
In this context, collection refers to the internal group of vectors (embeddings) stored in your Chroma vector database.

Think of a collection like a table in a relational database or a collection in MongoDB. It's:

A named logical group of documents (or chunks) + their embeddings. Backed by persistent storage (if you use persist_directory).

The place where your documents' text is stored,their vector embeddings are saved, and associated metadata is kept.


### Failure Modes:
1. Duplicate data in multiple documents
    - Le's say if we input two same documents in input, so after splitting and embedding it gets stored in vector db.
    - Once we retrieve a relevant document by similarity of the vector embeddings between input query and stored document splits
    - If there are duplicate input documents same content will be pulled back, ideally we would want syntactically closer and distinct document splits (so that we can pass it to LLM)
2. Equal weightage to whole sentence
    - Let's say we input a search query (Get me details about regression from lecture 3), this will focus equally on regression and lecture 3 thus this query will return documents containing info related to regression even if they are on documents other than lecture 3.


## Retrieval

### Type of Retrieval:
#### 1. Similarity Search
    - Semantically similar search
#### 2. Maximum marginal relevance
<img width="726" alt="Screenshot 2025-06-15 at 1 00 06 PM" src="https://github.com/user-attachments/assets/b1f9cd77-6927-4e49-bea9-dd8f31ab5b7e" />

 - Maximum marginal relevance strives to achieve both relevance to the query and diversity among the results.
 - This can be used to avoid similar or matching data and provided more broader results.

#### 3. LLL Aided Retrieval
<img width="726" alt="Screenshot 2025-06-15 at 1 01 23 PM" src="https://github.com/user-attachments/assets/b7675e78-816a-43c8-b2ea-4481d59d60b7" />

 - Using something like Self query
 - We can break the input in two parts as a question and filter, and apply a filter and then show result in that filtered docs.

#### 4. Compression Retrieval

<img width="726" alt="Screenshot 2025-06-16 at 3 24 47 AM" src="https://github.com/user-attachments/assets/f186e22e-a11f-40a9-8359-6888dfd7f6a0" />

 - ContextualCompressionRetriever can be used (read below section)
 - Another approach for improving the quality of retrieved docs is compression. Information most relevant to a query may be buried in a document with a lot of irrelevant text. 
 - Passing that full document through your application can lead to more expensive LLM calls and poorer responses.
 - Contextual compression is meant to fix this.   


#### ContextualCompressionRetriever
    - Most retrievers (like Chroma, FAISS, etc.) return entire chunks (e.g., full paragraphs) that match the query vector-wise. 
    - But these chunks can: Be large. Contain lots of irrelevant fluff. Overflow context windows.
    - So, ContextualCompressionRetriever solves this by: Running a compression chain (usually a language model) on retrieved docs. Keeping only the parts that are highly relevant to your query. 


#### TFIDFRetriever (Term Frequency–Inverse Document Frequency)
- What it does:
    - Uses a classic bag-of-words approach. Calculates how important a word is in a document relative to a corpus.
    - Ranks documents based on term overlap with the query.
    - Pros:
        - Fast and easy to use.
        - No need for embeddings or training.
        - Transparent: you can see exactly why a document was chosen.
    - Cons:
        - Purely based on exact text match, so no semantic understanding.
        - Sensitive to vocabulary mismatch (e.g., "car" vs "automobile").
        - Best use case:
            - Simple keyword-based search or Lightweight apps or small datasets


#### What is SVMRetriever?
SVMRetriever is a machine learning-based retriever that uses SVM (Support Vector Machine) to classify which documents are most relevant to your question.

- Think of it like this:
    - You give it a bunch of documents (converted to embeddings = numerical representations of meaning). It treats your query like a "positive example", and tries to classify which documents are "like the query" using an SVM. The most similar ones (based on vector distance and classification confidence) are returned.
- Why is it useful?
    - It learns a decision boundary using your question and the document embeddings.
- More flexible than TF-IDF because it uses semantic meaning (via embeddings).
- Can find relevant documents even if they don’t share exact words with the query.

## Question Answering

<img width="804" alt="Screenshot 2025-06-16 at 11 24 00 AM" src="https://github.com/user-attachments/assets/991c73e1-091c-42e3-a720-90d77f549886" />

#### 📌 What is RetrievalQA?

`RetrievalQA` is a **built-in chain** in LangChain that allows you to ask questions based on external documents (like PDFs, web pages, or transcripts). It connects a **retriever** (that finds relevant information) with a **language model (LLM)** (that generates a coherent answer).

<img width="766" alt="Screenshot 2025-06-16 at 11 25 01 AM" src="https://github.com/user-attachments/assets/0b621f55-3e43-46fc-8fe5-b0d4a69f9501" />

#### Types of Chain Types (Check readme-secondary for details)

The prompt is passed to the LLM model with relevant document splits and context in a prompt.
1. Stuff Documents ( All the documents are fed to LLM model)
2. Map Reduce
3. Refine
4. Map Rerank

<img width="766" alt="Screenshot 2025-06-16 at 8 12 32 PM" src="https://github.com/user-attachments/assets/856f78f7-5cbc-44ed-a177-b66da926782d" />

## Chatbot

<img width="770" alt="Screenshot 2025-06-17 at 2 00 38 AM" src="https://github.com/user-attachments/assets/6a3d5353-5965-41b3-87a9-28e5c9cd549a" />
<img width="770" alt="Screenshot 2025-06-17 at 2 00 23 AM" src="https://github.com/user-attachments/assets/dd25a1c5-03d2-4e78-ba29-fcb799e935dc" />



# setup

1. python3 -m venv backend-ve
2. source ./backend/be/activate
2. pip install -r requirements.txt
