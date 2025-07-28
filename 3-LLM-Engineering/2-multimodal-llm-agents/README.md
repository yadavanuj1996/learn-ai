## Gradio
- Gradio is an framework provided by HuggingFace to create ready made UIs for our AI applications.

# Chat fn that is passed to gradio:

`chat(message, history)`

Which expects to receive `history` in a particular format, which we need to map to the OpenAI format before we call OpenAI:

```
[
    {"role": "system", "content": "system message here"},
    {"role": "user", "content": "first user prompt here"},
    {"role": "assistant", "content": "the assistant's response"},
    {"role": "user", "content": "the new user prompt"},
]
```

But Gradio has been upgraded! Now it will pass in `history` in the exact OpenAI format, perfect for us to send straight to OpenAI.

**message** is the prompt to use  
**history** is the past conversation, in OpenAI format  

We will combine the system message, history and latest message, then call OpenAI.

## What Are Tools?
Tools are **external functions** (e.g., calculator, API, database) that LLMs can call to:
- Extend knowledge
- Perform actions
- Access live or external data

## How Tools Work
1. **Define** tools: specify their name, inputs, and outputs.
2. **Inform** the LLM about the available tools.
3. **LLM interaction**:
   - May **respond directly**, or
   - **Request a tool call** with specific inputs.
4. **You execute** the tool and return the result.
5. **LLM uses** the output to generate a richer, more informed response.

> This process is like inserting extra context into prompts, but automated and dynamic.

## Common Use Cases for Tools
1. **Fetching Extra Data** – e.g., database lookups to enhance knowledge.
2. **Taking Actions** – e.g., booking tickets or sending emails.
3. **Performing Calculations** – since LLMs aren't good at math natively.
4. **Modifying the UI** – e.g., changing the frontend via tool-triggered actions.


- We have created a multi modal ai assistant of flight chat agent in module 5 here that can talk to you in english and show images of destination city.