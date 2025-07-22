import asyncio
import json
from contextlib import AsyncExitStack
from typing import Any, Dict, List, Optional

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from dotenv import load_dotenv
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from openai import AsyncOpenAI

# Configuration
LLAMA_SERVER_URL = "http://localhost:11434/v1"
LLAMA_API_KEY = "ollama"
MCP_SERVER_URL = "http://localhost:8050"
MODEL = "llama3.2"


# FastAPI App
app = FastAPI()

class QueryRequest(BaseModel):
    query: str

class MCPOpenAIClient:
    def __init__(self):
        self.session: Optional[ClientSession] = None
        self.exit_stack = AsyncExitStack()
        self.openai_local_llama_client = AsyncOpenAI(base_url=LLAMA_SERVER_URL, api_key=LLAMA_API_KEY)

    async def connect_to_server(self, mcp_url: str = MCP_SERVER_URL):
        # Connect using streamable-http client the right way
        read, write, _ = await self.exit_stack.enter_async_context(
            streamablehttp_client(f"{mcp_url}/mcp")
        )
        self.session = await self.exit_stack.enter_async_context(
            ClientSession(read, write)
        )
        await self.session.initialize()
    async def get_mcp_tools(self) -> List[Dict[str, Any]]:
        tools_result = await self.session.list_tools()
        return [
            {
                "type": "function",
                "function": {
                    "name": tool.name,
                    "description": tool.description,
                    "parameters": tool.inputSchema,
                },
            }
            for tool in tools_result.tools
        ]

    async def process_query(self, query: str) -> str:
        tools = await self.get_mcp_tools()
        response = await self.openai_local_llama_client.chat.completions.create(
            model=MODEL,
            messages=[{"role": "user", "content": query}],
            tools=tools,
            tool_choice="auto",
        )
        assistant_message = response.choices[0].message
        messages = [{"role": "user", "content": query}, assistant_message]

        if assistant_message.tool_calls:
            for tool_call in assistant_message.tool_calls:
                result = await self.session.call_tool(
                    tool_call.function.name,
                    arguments=json.loads(tool_call.function.arguments),
                )
                messages.append(
                    {
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": result.content[0].text,
                    }
                )
            final_response = await self.openai_local_llama_client.chat.completions.create(
                model=response.model,
                messages=messages,
                tools=tools,
                tool_choice="none",
                stream=False,
            )
            return final_response.choices[0].message.content
        return assistant_message.content

    async def cleanup(self):
        await self.exit_stack.aclose()

# Global MCP+OpenAI client instance
mcp_client = MCPOpenAIClient()

@app.on_event("startup")
async def startup_event():
    await mcp_client.connect_to_server()

@app.on_event("shutdown")
async def shutdown_event():
    await mcp_client.cleanup()

@app.post("/query")
async def query_endpoint(request: QueryRequest):
    response = await mcp_client.process_query(request.query)
    return JSONResponse(content={"response": response})
