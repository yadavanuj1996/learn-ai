Absolutely! Here's the **complete `README.md`** content in a single copy-pasteable block, written cleanly and simply with useful icons and steps:

---

````markdown
# 🚀 MCP Server with Docker

This project demonstrates how to run an **MCP (Model Context Protocol)** server using Docker. The server includes a simple calculator tool accessible by a client.

---

## ✅ Prerequisites

- 🐳 Docker installed
- 🧱 Git to clone the repository
- 🐍 Python (for running the client outside Docker)

---

## 📁 Project Structure

| File               | Description                                      |
|--------------------|--------------------------------------------------|
| `server.py`        | MCP server exposing a calculator tool            |
| `client.py`        | Client that connects to the server and uses tool |
| `Dockerfile`       | Builds the Docker image for the server           |
| `requirements.txt` | Python dependencies                              |

---

## 🛠️ Running the Server with Docker

### 🔧 Step 1: Build the Docker image

```bash
docker build -t mcp-server .
````

### ▶️ Step 2: Run the Docker container

```bash
docker run -p 8050:8050 mcp-server
```

✅ This starts the MCP server inside Docker, accessible at:
`http://localhost:8050`

---

## 🧪 Running the Client

In a **separate terminal**, make sure your Python environment is ready, then run:

```bash
python client.py
```

📌 The client will:

* Connect to the running MCP server
* List all available tools
* Call the `add` tool with inputs `a = 2`, `b = 3`
* Print the result:

  ```
  2 + 3 = 5
  ```

---

## 📎 Notes

* The server uses **HTTP streamable transport** (`/mcp` endpoint).
* You can extend this by adding more tools (e.g., knowledge base, RAG, etc.).
* OpenAI can be connected to this server using MCP’s `ClientSession`.
