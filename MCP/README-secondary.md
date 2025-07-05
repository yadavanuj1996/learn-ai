
<img width="893" alt="Screenshot 2025-07-05 at 4 47 35 PM" src="https://github.com/user-attachments/assets/6586af2c-33eb-4276-9d21-2f6e71ea9efb" />

MCP defines three core primitives that servers can implement:

- Tools: Model-controlled functions that LLMs can invoke (like API calls, computations)
- Resources: Application-controlled data that provides context (like file contents, database records)
- Prompts: User-controlled templates for LLM interactions  

For Python developers, the most immediately useful primitive is tools, which allow LLMs to perform actions programmatically.

### Transport Mechanisms Deep Dive
MCP supports three main transport mechanisms:

**1. Stdio (Standard IO):**
- Communication occurs over standard input/output streams
- Best for local integrations when the server and client are on the same machine
- Simple setup with no network configuration required
 
**2. SSE (Server-Sent Events):**
- Uses HTTP for client-to-server communication and SSE for server-to-client
- Suitable for remote connections across networks
- Allows for distributed architectures

**3. Streamable HTTP (Introduced March 24, 2025):**

- Modern HTTP-based streaming transport that supersedes SSE
- Uses a unified endpoint for bidirectional communication
- Recommended for production deployments due to better performance and scalability
- Supports both stateful and stateless operation modes

Understanding when to use each transport is crucial for building effective MCP implementations:
- Use Stdio when building single-application integrations or during development
- Use SSE for development or when working with older MCP implementations
- Use Streamable HTTP for production deployments where you need the best performance and scalability

<img width="1097" alt="Screenshot 2025-07-05 at 4 49 25 PM" src="https://github.com/user-attachments/assets/c5304816-e826-4bab-ba75-54017a24100e" />

