# What is RAG & Why Do We Need It?

Understand parametric vs non-parametric memory, avoiding costly fine-tuning, and grounding LLMs with real-time enterprise knowledge.

---

## The Fundamental Problem with Raw LLMs

1. Knowledge Cutoff: An LLM knows nothing that happened after its training dataset was compiled.
2. Private Enterprise Blindness: An LLM does not know your company's proprietary PDF manuals, internal Notion notes, or customer databases.
3. Hallucination: When asked about facts outside its weights, it confidently invents answers.

Why not just Fine-Tune? Fine-tuning updates model weights. It is extraordinarily expensive ($10,000s in GPU compute), slow (hours/days to retrain), and cannot be updated in real-time when a document changes.

## Parametric vs Non-Parametric Memory

• Parametric Memory: The knowledge encoded inside the billions of weights of the neural network (like a human's long-term memory).

• Non-Parametric Memory: External storage (like an open textbook or Google Search) where accurate, real-time documents are indexed in a Vector Database.

RAG (Retrieval-Augmented Generation) combines both: When a question is asked, RAG searches the external library, finds the 3 most relevant pages, pastes them into the prompt, and asks the LLM: "Using ONLY the text below, answer the question and cite your source!"

RAG vs Fine-Tuning Summary: Use RAG to give the model ACCESS TO KNOWLEDGE. Use Fine-Tuning to teach the model a SPECIFIC STYLE, tone, or domain syntax.

