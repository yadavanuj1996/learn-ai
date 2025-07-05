### Definition
Model Context Protocol (MCP), a new standard for connecting AI assistants to the systems where data lives, including content repositories, business tools, and development environments. Its aim is to help frontier models produce better, more relevant responses.

### History and what we know
<img width="1302" alt="Screenshot 2025-07-04 at 11 06 55 PM" src="https://github.com/user-attachments/assets/51f96d46-382a-41a7-81e9-5d4563365f7f" />

The first version of smart LLM solution we saw was a simple chatbot ex:- ChatGPT first edition, nowdays we can have AI assistant in which we can add various tools and in case the LLM does not have the answer it can see which tools are available and use one of them to get the answer for us. ( This tool will provide some type of context to the LLM so that LLM can give an answer)

Note: One example of tool can also be a search that add a tool that enables LLM to get real time web search results from let's say DuckDuck Go.

### Current challenge
If we want to do have 100 such tools attach to our LLM, we need to write custom for each of them and then maintain the code and deal with all the changes with the integrations (like version upgrades of libraries or breaking changes made by tool providers fora particular tool etc)

### How MCP solves it
<img width="930" alt="Screenshot 2025-07-04 at 11 21 10 PM" src="https://github.com/user-attachments/assets/163dec8d-5650-43a3-b92a-a3c3fde358e8" />

MCP acts as a median between the LLM and all the tool providers and for any tool provider that want to make a tool that works on MCP protocol needs to adhere all the rules and guidelines defined in MCP. (even in official docs of MCP it is mentioned that this is like a USB C port and can connect to any number and type of tools.)


### MCP Components

<img width="1285" alt="Screenshot 2025-07-05 at 1 24 18 AM" src="https://github.com/user-attachments/assets/80deb862-b459-43f7-8f99-e837d4a44177" />

3 Major components
- MCP Host
- MCP Client
- MCP Server

Internally in MCP host can create MCP clients to interact with different different tools or service providers. 
**This MCP client will be interacting with MCP server (using MCP protocol).**

- MCP host can be a vscode ide or claude desktop. Also it can be a application created using streamlit or fast api.
  - Streamlit can act as the MCP Host App where both the interface and the MCP logic run (Stremlit provides a frontend interactive chat UI.)
  - FastAPI is best when you want to decouple the frontend (e.g., React) and expose your MCP loop as an API

- We can connect MCP client with multiple MCP servers and these MCP server can be connected to different tools & services. In the diagram above if you see one MCP server is connected to Code repo, another is connected to db while one is connect to some APIs.
  - In the above example each MCP server is connected to only one service/ tool but there is no constraint **each MCP server can be connected to multiple services/tools.**

Note: If any changes in tool providers will be done we don't have to make any changes (no extra code change need on our side as we are manageing mcp host on out side that does not need any code change) it's tool providers responsibility to keep thier tool or service providers adhered to MCP protocol.


- **The MCP server will also be provided by service providers**, ex:- if zerodha exposes it's MCP server and we connect zerodha MCP server using our MCP client, the responsibility of manageing MCP server in this case will lie with zerodha and any udpate that needs to be made will be made by zerodha and we don't have to make any change in our code.


## Communication between these components

<img width="1281" alt="Screenshot 2025-07-05 at 2 02 14 AM" src="https://github.com/user-attachments/assets/87f68a0b-f264-4199-b86c-7cd547abbee7" />

1. MCP host will first find out on the basis of input provided and go and hit MCP servers and MCP server will return all the toold and service providers available with it.
2. MCP host will hit the LLM with input question and all tools available in MCP server.
3. LLM will provide response which tool to use (of all the list of tools provided). Let's say LLM responds to MCP hostto use a particular DB tool.
4. The MCP Host will along with input question and the tool it will hit the specific tool through the MCP server. (In this case after hitting the particular db tool the reponse will be sent back to MCP Host)
5. The **Context** will be sent to the LLM and we get the final output.

