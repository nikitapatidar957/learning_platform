# Tool Calling, Function Schemas & Agent Memory

Define tools with JSON Schema, parse structured function calls, manage working memory vs episodic vector memory.

---

## How Tool Calling Works Behind the Scenes

Modern LLMs (OpenAI, Anthropic, Gemini) are trained to recognize JSON Schema tool definitions. When the model determines a tool is needed, it stops generating text and outputs a structured JSON payload containing the tool name and validated arguments. Your backend executes the function and feeds the return string back as a 'tool' message.

## Defining JSON Schema Tools for Agents

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_database",
            "description": "Query the company customer database for account balance",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {"type": "string", "description": "Customer account UUID"},
                    "include_history": {"type": "boolean", "default": False}
                },
                "required": ["customer_id"]
            }
        }
    }
]
```

## The 3 Layers of Agent Memory

• Sensory / Scratchpad Memory: Short-term context within the current prompt (tool call history, intermediate scratch notes).
• Episodic Memory: Memory of previous user interactions and past conversation trajectories stored in persistent databases.
• Semantic Memory: Facts, world knowledge, and corporate handbooks retrieved on-demand via vector search.

