
### History and what we know
<img width="1302" alt="Screenshot 2025-07-04 at 11 06 55 PM" src="https://github.com/user-attachments/assets/51f96d46-382a-41a7-81e9-5d4563365f7f" />

The first version of smart LLM solution we saw was a simple chatbot ex:- ChatGPT first edition, nowdays we can have AI assistant in which we can add various tools and in case the LLM does not have the answer it can see which tools are available and use one of them to get the answer for us. ( This tool will provide some type of context to the LLM so that LLM can give an answer)

Note: One example of tool can also be a search that add a tool that enables LLM to get real time web search results from let's say DuckDuck Go.

### Current challenge
If we want to do have 100 such tools attach to our LLM, we need to write custom for each of them and then maintain the code and deal with all the changes with the integrations (like version upgrades of libraries or breaking changes made by tool providers fora particular tool etc)

<img width="930" alt="Screenshot 2025-07-04 at 11 21 10 PM" src="https://github.com/user-attachments/assets/163dec8d-5650-43a3-b92a-a3c3fde358e8" />

MCP acts as a median between the LLM and all the tool providers and for any tool provider that want to make a tool that works on MCP protocol needs to adhere all the rules and guidelines defined in MCP. (even in official the docs of MCP it is mentioned that this is like a USB C port and can connect to any number and type of tools.)
