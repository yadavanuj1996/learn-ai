# 🤖 OpenAI Integration with MCP

This example demonstrates how to integrate the **Model Context Protocol (MCP)** with OpenAI's API to build a system where OpenAI can access and use tools provided by your MCP server.

---

## 📌 Overview

This project shows how to:

- ✅ Create an MCP server that exposes a knowledge base tool
- ✅ Connect OpenAI to the MCP server using the MCP client
- ✅ Allow OpenAI to dynamically select and use tools when generating responses

---

## 🔌 Connection Method

This example uses **`stdio` transport** for communication between the OpenAI client and the MCP server.

- ⚙️ Client and server run in the **same process**
- ⚡ Client **launches the server** as a subprocess
- 🧩 No separate long-running server is needed

---

## 🧠 How OpenAI Executes Tools via MCP

OpenAI's function calling works seamlessly with MCP tools through the following flow:

1. **Tool Registration**  
   MCP client exposes its tools in OpenAI’s function call format.

2. **Tool Choice**  
   OpenAI automatically chooses the most relevant tool based on the user query.

3. **Tool Execution**  
   The MCP client invokes the selected tool and returns the result.

4. **Context Integration**  
   OpenAI integrates the tool result directly into its final response.

---

## 🛠️ Implementation Details

### `server.py` — MCP Server

- Exposes a tool: `get_knowledge_base`
- Retrieves Q&A pairs from a JSON knowledge base
- Serves tool responses on request from OpenAI

---

### `client.py` — MCP Client

- Launches and connects to the MCP server
- Translates MCP tools into OpenAI-compatible function schema
- Routes queries and tool results between OpenAI and the MCP server
- Returns enriched OpenAI responses using tool outputs

---

### `data/kb.json` — Knowledge Base

- A JSON file containing structured Q&A data
- Used by the `get_knowledge_base` tool
- Can be extended to include any domain-specific policy or FAQ information

---

## ✅ Example Use Case

Ask OpenAI something like:
"What is the company's remote work policy?"


OpenAI will:

1. Select the `get_knowledge_base` tool
2. Query the MCP server
3. Use the result to generate a detailed and accurate answer

---

## 📎 Notes

- This integration serves as a reference architecture for building **RAG-style LLM systems** using MCP and OpenAI.
- You can extend this project by adding more tools, datasets, or even switching transport methods (`stdio` → `http`, `websocket`, etc.).


