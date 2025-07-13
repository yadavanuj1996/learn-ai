Important links for the project:
1. https://github.com/modelcontextprotocol/python-sdk
2. https://github.com/daveebbelaar/ai-cookbook/tree/main/mcp/crash-course/ (Follow README very important)


- Development Mode with MCP Inspector
    - The easiest way to test your server is using the MCP Inspector: mcp dev server.py

You can also run the server directly:

Method 1: Running as a Python script
- python server.py

Method 2: Using UV (recommended)
- uv run server.py

### What Happens When You Run an MCP Server?
When you run an MCP server:

- The server initializes with the capabilities you've defined (tools, resources, etc.)
It starts listening for connections on a specific transport
By default, MCP servers don't use a traditional web server port. Instead, they use either:

    - stdio transport: The server communicates through standard input and output (the default for mcp run and integration with Claude Desktop)
    - SSE transport: For HTTP-based communication (used when explicitly configured)
If you want to expose your server over HTTP with a specific port, you need to modify your server to use the SSE transport