import asyncio
import json
import os

from datetime import date
from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from openai import OpenAI

load_dotenv()

def mcp_tools_to_openai_format(tools):
    # MCP and OpenAI use different schemas to describe tools.
    # This function translates MCP's format into what OpenAI expects.
    # GPT-4o reads "description" to decide when to call a tool,
    # and "parameters" to know what arguments to pass.
    return [
        {
            "type": "function",           # OpenAI requires this wrapper on every tool
            "function": {
                "name": t.name,           # e.g. "list_emails", "accept_event"
                "description": t.description,
                "parameters": t.inputSchema,
            },
        }
        for t in tools
    ]
 
async def call_mcp_tool(session, tool_name, tool_input):
    # MCP tools are called via the ClientSession's call_tool method.
    # This function wraps that call and returns the result in a way
    # that GPT-4o can understand.
    result = await session.call_tool(tool_name, tool_input)
    return result.content[0].text if result.content else ""

async def run_agent():
    today = date.today().isoformat()

    workspace_server = StdioServerParameters(
        command="uvx",
        args=["mcp-google-workspace@latest"],
        env={},  # reads .gauth.json and .accounts.json automatically from current dir
    )

    print(f"\n📬 Mail agent starting for {today}\n")

    async with stdio_client(workspace_server) as (read, write):
        async with ClientSession(read, write) as workspace:
            await workspace.initialize()
            # Always call this before list_tools() or call_tool().
            
            all_tools_raw = (await workspace.list_tools()).tools
            all_tools = mcp_tools_to_openai_format(all_tools_raw)
            all_tool_names = {t.name for t in all_tools_raw}

            print(f"✅ Workspace tools: {[t.name for t in all_tools_raw]}\n")


            client= OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

            messages = [
                {
                    "role": "system",
                    # OpenAI takes the system prompt as the first message
                    # with role "system" — not as a separate parameter.
                    "content": f"""You are a personal email and calendar assistant. Today is {today}.

                Your tasks:
                1. Read all emails that arrived today using the Gmail tools.
                2. Summarise them in three groups: URGENT, FYI, NEWSLETTERS/PROMOS.
                3. Find all meeting invites in email and calendar events for today.
                4. For each invite decide ACCEPT or DECLINE:
                - ACCEPT: from manager/stakeholder, or subject has 1:1 / standup /
                    review / demo / client / interview / sync / urgent
                - DECLINE: optional, mass invite, social/fun, or clashes with
                    a more important meeting
                5. Use the calendar tools to actually accept or decline — do not just describe it.
                6. End with a clean summary of what you read and what actions you took.
                7. Please note even if calendar meets are from unknown people if they are important they should not be removed.
                8. Do not reject because of unknown people think that only office people will mail me but all of their invites may not be important use your intelligence but do not reject because of unknown sender.
                
                Always be decisive. Always use the tools."""
                                        },
                                        {
                                            "role": "user",
                                            "content": "Process my emails and calendar for today please."
                                            # This kicks off the agent. GPT-4o will start
                                            # calling tools in response to this message.
                                        }
            ]

            # main agentic loop (that is part of overall agentic workflow refer diagram)
            
            while True:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    tools=all_tools,
                    messages=messages,
                )

                calendar_assistant_message = response.choices[0].message

                if calendar_assistant_message.content:
                    print(f"\n\n\n\n\n\n\n\n\n\n Calendar Agent: {calendar_assistant_message.content}\n")
                    
                # main condition that if no more tool call needed and the final message is
                # is printed that needs to be shown as log
                if not calendar_assistant_message.tool_calls:
                    break

                # LLM does not have history of our chat so we send the entire conversation
                # with even their own response back to them for next tool call/ chat response.
                messages.append(calendar_assistant_message)

                for tool_call in calendar_assistant_message.tool_calls:
                    tool_name = tool_call.function.name
                    tool_input = json.loads(tool_call.function.arguments)
                    
                    print(f"  🔧 {tool_name}({tool_input})")
                    
                    tool_result = await call_mcp_tool(workspace, tool_name, tool_input)


                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_result,
                    })
            
            print("\n✅ Done.\n")


if __name__ == "__main__":
    asyncio.run(run_agent())