import os
import requests
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
from openai import OpenAI
from duckduckgo_search import DDGS


# crete mcp server

mcp = FastMCP(
    name="LLM + Search",
    host="0.0.0.0",
    port=8050,  
)

@mcp.tool()
def search(query: str) -> str:
    """Search the DuckDuckGo knowledge base for the given query.
    Args:
        query: The search query.
    Returns:
        A list of search results (top 3).
    """
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)
        return [{"title": r['title'], "url": r['href']} for r in results]
    
# Run the server
if __name__ == "__main__":
    transport = "streamable-http"
    
    if transport == "stdio":
        print("Running server with stdio transport")
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running server with SSE transport")
        mcp.run(transport="sse")
    elif transport == "streamable-http":
        print("Running server with Streamable HTTP transport")
        mcp.run(transport="streamable-http")
    else:
        raise ValueError(f"Unknown transport: {transport}")