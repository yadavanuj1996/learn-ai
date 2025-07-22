## GPT Tokenization Summary

- Tokens are the core input units for LLMs.
- Character-level models had small vocabularies but poor semantic understanding.
- Word-level tokenization improved meaning capture but led to huge vocabularies and issues with rare/unknown words.
- Subword tokenization (used by GPT) is a balance — breaks text into common chunks, handling both full words and fragments.
- Spaces are part of tokens and matter semantically.
- Rare/compound words and numbers are split into multiple tokens.
- General rule: 1 token ≈ 4 characters ≈ 0.75 words.
- Tokenizer types vary by model (e.g., GPT vs. LLaMA), with different trade-offs.

---

## Context Windows in LLMs (Token Limits)

- Context window = total number of tokens a model can "see" at once to generate the next token.
- Core task: LLMs predict the next token based on all visible tokens in the context window.
- Includes system prompt, user messages, and model responses — all fed in together each time.
- In chat apps (e.g. ChatGPT), the model doesn’t truly "remember" — it reprocesses the entire conversation each time.
- Window size limits how much history can be used. If a convo or input exceeds this, older tokens are dropped.
- Larger windows are crucial for tasks like multi-shot prompting or processing long documents (e.g., Shakespeare).
- Context window size is defined by the model’s architecture and parameter count.

**Key takeaway**:  
The context window controls how much input history an LLM can consider for output — a vital factor for maintaining coherent, long conversations or handling large texts.
