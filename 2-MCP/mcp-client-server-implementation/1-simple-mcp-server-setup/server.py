from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv(".env")

# create an mcp server
mcp = FastMCP(name="Calculator", 
              host="0.0.0.0",  # only used for SSE transport (localhost)
              port="8050",     # only used for SSE transport (set this to any port)
              stateless_http=True)


# Add simple calculator tool
# Note mcp used in decorator is the name of variable defined above
@mcp.tool()
def add(a: int, b:int) -> int:
    """
    Adds two numbers together.
    """
    return a + b

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