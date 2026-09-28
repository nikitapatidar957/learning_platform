# Autonomous Agent Loops & The ReAct Framework

Understand what differentiates an AI Agent from a plain chatbot, the ReAct loop, tool calling, and self-correction.

---

## Chatbot vs AI Agent: The Difference

• Chatbot: Passive single-turn responder. Input prompt in ➔ Output response out. Cannot browse the web, execute terminal commands, or verify facts.

• AI Agent: An autonomous goal-driven system equipped with:
  1. LLM Brain (Reasoning & Decision making)
  2. Tools (APIs, Python code interpreter, Database connectors, Web search)
  3. Memory (Short-term context window + Long-term vector store)
  4. Feedback Loop: Evaluates results of its actions and retries if an error occurs.

## The ReAct Loop: Reason + Act

Published by Yao et al. (Princeton/Google), ReAct coordinates reasoning and action in a tight cycle:

1. Thought: "The user asked for the current stock price of Apple. I do not have real-time financial data in my weights. I should call the stock_ticker API for AAPL."
2. Action: `call_api(ticker='AAPL')`
3. Observation: `{ 'price': 224.50, 'currency': 'USD' }`
4. Thought: "I now have the verified live price. I can synthesize the final answer."
5. Final Answer: "Apple (AAPL) is currently trading at $224.50 USD."

