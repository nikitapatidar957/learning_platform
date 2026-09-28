"""
Generative AI, RAG, LLM, Agentic AI, Deep Learning & MongoDB Topics and Lessons Seed Data
Incorporating concepts from:
- python_interview/gen_ai_theory.md
- python_interview/Rag_notes.md
- python_interview/notes_copy1.md
"""

ADVANCED_TOPICS = [
    # Generative AI Topics
    {
        "subjectSlug": "generative-ai",
        "title": "Generative AI Foundations",
        "slug": "genai-foundations",
        "description": "Generative vs discriminative AI, GANs, VAEs, diffusion models, transformers, and prompt engineering frameworks.",
        "order": 1,
        "isPublished": True,
    },
    {
        "subjectSlug": "generative-ai",
        "title": "Retrieval-Augmented Generation (RAG)",
        "slug": "rag-architecture-pipeline",
        "description": "Parametric vs non-parametric memory, document ingestion, chunking strategies, vector embeddings, similarity search, and synthesis.",
        "order": 2,
        "isPublished": True,
    },
    # LLM Topics
    {
        "subjectSlug": "llm",
        "title": "Transformer & LLM Foundations",
        "slug": "transformer-attention-foundations",
        "description": "Encoder-decoder models, tokenization (BPE), embeddings, self-attention mechanics (Q, K, V), and decoding temperature.",
        "order": 1,
        "isPublished": True,
    },
    # Agentic AI Topics
    {
        "subjectSlug": "agentic-ai",
        "title": "Autonomous Agent Systems",
        "slug": "agentic-architectures",
        "description": "Agent loop dynamics, ReAct reasoning framework, structured tool calling, short/long-term memory, and multi-agent coordination.",
        "order": 1,
        "isPublished": True,
    },
    # Deep Learning Topics
    {
        "subjectSlug": "deep-learning",
        "title": "Neural Network Fundamentals & Backprop",
        "slug": "neural-network-training",
        "description": "Perceptrons, multi-layer networks, activation functions, forward propagation, calculus chain rule backpropagation, and optimizers.",
        "order": 1,
        "isPublished": True,
    },
    # MongoDB Topics
    {
        "subjectSlug": "mongodb",
        "title": "MongoDB Document Modeling & Aggregations",
        "slug": "mongodb-document-modeling",
        "description": "JSON/BSON document paradigms, CRUD query operators ($gt, $in, $regex), indexing strategies, and aggregation pipelines.",
        "order": 1,
        "isPublished": True,
    },
]

ADVANCED_LESSONS = [
    # -------------------------------------------------------------------------
    # Generative AI Lessons
    # -------------------------------------------------------------------------
    {
        "topicSlug": "genai-foundations",
        "subjectSlug": "generative-ai",
        "title": "Generative vs Traditional AI & Model Types",
        "slug": "generative-vs-traditional-ai",
        "description": "Understand generative vs discriminative modeling, GANs, VAEs, Diffusion models, Transformers, and mitigating hallucination.",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "What is Generative AI?",
                    "content": (
                        "Generative AI refers to algorithms capable of generating novel, human-like content (text, code, images, audio, synthetic data) "
                        "by learning the underlying probability distribution of massive training datasets.\n\n"
                        "• Discriminative AI: Models P(Y | X) ➔ Distinguishes between existing categories (e.g., 'Is this image a dog or a cat?').\n"
                        "• Generative AI: Models P(X) or P(X | Y) ➔ Generates new instances from the learned data distribution (e.g., 'Generate a photorealistic picture of a golden retriever in space')."
                    )
                },
                {
                    "type": "explanation",
                    "title": "The 4 Core Generative AI Model Architectures",
                    "content": (
                        "1. Generative Adversarial Networks (GANs):\n"
                        "   A two-player min-max game: A Generator creates fake samples, and a Discriminator tries to catch them. Over iterations, both become exceptionally skilled.\n\n"
                        "2. Variational Autoencoders (VAEs):\n"
                        "   Compresses inputs into a smooth continuous latent distribution, then samples points to reconstruct novel variants.\n\n"
                        "3. Diffusion Models (Midjourney, Stable Diffusion):\n"
                        "   Gradually destroys images by adding Gaussian noise over hundreds of steps, then trains a deep neural net to reverse the process and denoise pure static into crisp art.\n\n"
                        "4. Transformers (GPT, Claude, Gemini, Llama):\n"
                        "   Uses self-attention to model long-range relationships between tokens for autoregressive text and code generation."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Why Do LLMs Hallucinate?",
                    "content": (
                        "LLMs are stochastic next-token prediction engines. They do NOT possess a conscious understanding of truth; they output words with high conditional probability. "
                        "When training data is ambiguous or knowledge is missing from their parametric memory, they fabricate plausible-sounding falsehoods.\n\n"
                        "Mitigations: RAG (grounding with external search/docs), low temperature, strict system prompts, and multi-step verification tools."
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "Hallucination vs Creativity: The same probabilistic mechanism that creates a poetic metaphor also invents a non-existent legal court case if left unconstrained."
                }
            ]
        }
    },
    {
        "topicSlug": "genai-foundations",
        "subjectSlug": "generative-ai",
        "title": "Prompt Engineering Frameworks & Techniques",
        "slug": "prompt-engineering-techniques",
        "description": "Master Zero-shot, Few-shot (in-context learning), Chain-of-Thought (CoT), ReAct prompting, and inference hyper-parameters.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Prompt Engineering Techniques",
                    "content": (
                        "Prompt engineering is the practice of crafting and structuring inputs to guide large language models toward reliable, accurate outputs:\n\n"
                        "• Zero-Shot Prompting: Providing the instruction directly without any examples.\n\n"
                        "• Few-Shot Prompting (In-Context Learning): Providing 2 to 5 high-quality input-output demonstration pairs in the prompt. "
                        "The model observes the pattern and formats its output accordingly without weight fine-tuning!\n\n"
                        "• Chain-of-Thought (CoT): Prompting the model with \"Let's think step by step\". "
                        "By forcing the model to generate intermediate reasoning tokens, accuracy on math, logic, and multi-step coding problems jumps dramatically!"
                    )
                },
                {
                    "type": "code",
                    "title": "Chain-of-Thought Few-Shot Prompt Example",
                    "language": "python",
                    "code": (
                        "prompt = \"\"\"\n"
                        "Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. \n"
                        "Each can has 3 tennis balls. How many tennis balls does he have now?\n"
                        "A: Roger started with 5 balls. 2 cans of 3 tennis balls each is 2 * 3 = 6 balls. \n"
                        "5 + 6 = 11. The answer is 11.\n\n"
                        "Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, \n"
                        "how many apples do they have?\n"
                        "A: Let's think step by step:\n"
                        "\"\"\""
                    )
                },
                {
                    "type": "explanation",
                    "title": "Inference Hyper-Parameters: Temperature, Top-p, Top-k",
                    "content": (
                        "• Temperature (0.0 to 1.5+): Controls randomness. Lower values (0.0 - 0.2) make outputs focused, deterministic, and analytical (best for code/math). "
                        "Higher values (0.7 - 1.0) increase diversity and vocabulary variety (best for storytelling/creative writing).\n\n"
                        "• Top-p (Nucleus Sampling): Dynamically cuts off the candidate token pool to the smallest set whose cumulative probability sums to p (e.g., 0.90).\n\n"
                        "• Top-k: Hard-limits candidate tokens to the top k highest probability candidates."
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "rag-architecture-pipeline",
        "subjectSlug": "generative-ai",
        "title": "What is RAG & Why Do We Need It?",
        "slug": "what-is-rag-deep-dive",
        "description": "Understand parametric vs non-parametric memory, avoiding costly fine-tuning, and grounding LLMs with real-time enterprise knowledge.",
        "estimatedTime": "25 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": "RAGVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The Fundamental Problem with Raw LLMs",
                    "content": (
                        "1. Knowledge Cutoff: An LLM knows nothing that happened after its training dataset was compiled.\n"
                        "2. Private Enterprise Blindness: An LLM does not know your company's proprietary PDF manuals, internal Notion notes, or customer databases.\n"
                        "3. Hallucination: When asked about facts outside its weights, it confidently invents answers.\n\n"
                        "Why not just Fine-Tune? Fine-tuning updates model weights. It is extraordinarily expensive ($10,000s in GPU compute), slow (hours/days to retrain), "
                        "and cannot be updated in real-time when a document changes."
                    )
                },
                {
                    "type": "visualization",
                    "component": "RAGVisualizer",
                    "initialState": {}
                },
                {
                    "type": "explanation",
                    "title": "Parametric vs Non-Parametric Memory",
                    "content": (
                        "• Parametric Memory: The knowledge encoded inside the billions of weights of the neural network (like a human's long-term memory).\n\n"
                        "• Non-Parametric Memory: External storage (like an open textbook or Google Search) where accurate, real-time documents are indexed in a Vector Database.\n\n"
                        "RAG (Retrieval-Augmented Generation) combines both: When a question is asked, RAG searches the external library, finds the 3 most relevant pages, "
                        "pastes them into the prompt, and asks the LLM: \"Using ONLY the text below, answer the question and cite your source!\""
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "RAG vs Fine-Tuning Summary: Use RAG to give the model ACCESS TO KNOWLEDGE. Use Fine-Tuning to teach the model a SPECIFIC STYLE, tone, or domain syntax."
                }
            ]
        }
    },
    {
        "topicSlug": "rag-architecture-pipeline",
        "subjectSlug": "generative-ai",
        "title": "The End-to-End RAG Engineering Pipeline",
        "slug": "rag-end-to-end-pipeline",
        "description": "Step-by-step implementation: Document parsing, chunking strategies, dense embeddings, vector search, and context synthesis.",
        "estimatedTime": "35 mins",
        "difficulty": "Intermediate to Advanced",
        "order": 2,
        "isPublished": True,
        "interactiveType": "RAGVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The 6-Step Production RAG Flow",
                    "content": (
                        "Step 1: Document Ingestion (PDFs, Markdown, HTML, SQL tables)\n"
                        "Step 2: Chunking (Splitting large documents into bite-sized passages)\n"
                        "Step 3: Vector Embeddings (Converting text into 1536-dimensional semantic vectors)\n"
                        "Step 4: Vector Database Indexing (Pinecone, ChromaDB, FAISS, Milvus)\n"
                        "Step 5: Similarity Search (Finding nearest neighbors with Cosine Similarity)\n"
                        "Step 6: Augmented Prompt Generation (Synthesizing answer with citations)"
                    )
                },
                {
                    "type": "code",
                    "title": "Recursive Chunking & Vector Similarity Pipeline in Python",
                    "language": "python",
                    "code": (
                        "# Step 2: Chunking with Overlap to prevent splitting context mid-sentence\n"
                        "def chunk_text(text, chunk_size=500, overlap=50):\n"
                        "    chunks = []\n"
                        "    start = 0\n"
                        "    while start < len(text):\n"
                        "        end = start + chunk_size\n"
                        "        chunks.append(text[start:end])\n"
                        "        start += chunk_size - overlap  # Sliding window\n"
                        "    return chunks\n\n"
                        "# Step 5: Cosine Similarity between query vector and chunk vectors\n"
                        "import numpy as np\n\n"
                        "def cosine_similarity(v1, v2):\n"
                        "    return np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))\n\n"
                        "# RAG Prompt Assembly\n"
                        "def build_rag_prompt(query, retrieved_chunks):\n"
                        "    context = '\\n---\\n'.join(retrieved_chunks)\n"
                        "    return f\"\"\"Answer the question using ONLY the provided context.\n"
                        "If you don't know the answer, say 'I cannot find this in the documents'.\n\n"
                        "CONTEXT:\n{context}\n\n"
                        "QUESTION: {query}\"\"\""
                    )
                },
                {
                    "type": "callout",
                    "variant": "warning",
                    "content": "Why Chunk Overlap is Critical: If an important answer spans across character index 490 to 520, a hard chunk cut at 500 would sever the sentence in half. A 50-character overlap guarantees the full context exists intact in both chunks."
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # LLM Lessons
    # -------------------------------------------------------------------------
    {
        "topicSlug": "transformer-attention-foundations",
        "subjectSlug": "llm",
        "title": "The Transformer Architecture Deep Dive",
        "slug": "transformer-architecture-deep-dive",
        "description": "Understand how the 2017 'Attention Is All You Need' paper replaced RNNs/LSTMs with parallelizable self-attention.",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate to Advanced",
        "order": 1,
        "isPublished": True,
        "interactiveType": "LLMPipelineVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Why Did Transformers Replace RNNs and LSTMs?",
                    "content": (
                        "Prior to 2017, NLP relied on Recurrent Neural Networks (RNNs) and LSTMs. They processed text word by word sequentially:\n"
                        "• Bottleneck 1: Vanishing/Exploding Gradients on long documents (forgetting words from 50 tokens earlier).\n"
                        "• Bottleneck 2: ZERO GPU Parallelization! Word 50 could not be processed until Word 49 was done.\n\n"
                        "The Transformer discarded recurrence entirely: It takes all 4,000 words in a document simultaneously in parallel and uses Self-Attention "
                        "to calculate how every word relates to every other word."
                    )
                },
                {
                    "type": "visualization",
                    "component": "LLMPipelineVisualizer",
                    "initialState": {}
                },
                {
                    "type": "explanation",
                    "title": "Encoder-Only vs Decoder-Only vs Encoder-Decoder",
                    "content": (
                        "• Encoder-Only (e.g., BERT, RoBERTa):\n"
                        "  Bidirectional attention (can look forward and backward). Best for text classification, sentiment analysis, and generating vector embeddings.\n\n"
                        "• Decoder-Only (e.g., GPT-4, Llama 3, Mistral):\n"
                        "  Causal masked attention (tokens can only attend to prior tokens). Best for autoregressive generative text and code completion.\n\n"
                        "• Encoder-Decoder (e.g., T5, BART):\n"
                        "  Encodes input sequence, then decodes output sequence. Best for machine translation and document summarization."
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "transformer-attention-foundations",
        "subjectSlug": "llm",
        "title": "Self-Attention Mechanics: Query, Key & Value",
        "slug": "self-attention-mechanisms",
        "description": "Master the Q, K, V mathematical formula, scaled dot-product attention, and multi-head projection spaces.",
        "estimatedTime": "30 mins",
        "difficulty": "Advanced",
        "order": 2,
        "isPublished": True,
        "interactiveType": "LLMPipelineVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The Retrieval Analogy for Query, Key, and Value",
                    "content": (
                        "Think of YouTube or a library search:\n"
                        "• Query (Q): What you type into the search bar ('What is machine learning?').\n"
                        "• Key (K): The title / tags on all available video clips ('Introduction to ML', 'Baking Cookies', 'Python Basics').\n"
                        "• Value (V): The actual video content you watch.\n\n"
                        "In Self-Attention, each word in the sentence projects into a Query, a Key, and a Value vector via trained weight matrices W_q, W_k, W_v."
                    )
                },
                {
                    "type": "code",
                    "title": "The Famous Scaled Dot-Product Attention Formula",
                    "language": "python",
                    "code": (
                        "# Attention(Q, K, V) = softmax( (Q * K.T) / sqrt(d_k) ) * V\n\n"
                        "import numpy as np\n\n"
                        "def softmax(x):\n"
                        "    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))\n"
                        "    return e_x / np.sum(e_x, axis=-1, keepdims=True)\n\n"
                        "def scaled_dot_product_attention(Q, K, V):\n"
                        "    d_k = Q.shape[-1]  # Dimension of key vectors\n"
                        "    # 1. Compute attention raw scores (dot product)\n"
                        "    scores = np.matmul(Q, K.swapaxes(-2, -1))\n"
                        "    # 2. Scale by sqrt(d_k) to prevent vanishing gradients in softmax\n"
                        "    scaled_scores = scores / np.sqrt(d_k)\n"
                        "    # 3. Softmax to get probability distribution (attention weights)\n"
                        "    weights = softmax(scaled_scores)\n"
                        "    # 4. Weighted sum of values\n"
                        "    output = np.matmul(weights, V)\n"
                        "    return output, weights"
                    )
                },
                {
                    "type": "callout",
                    "variant": "tip",
                    "content": "Why scale by √d_k? For large vector dimensions (e.g., d_k = 128), dot products grow large in magnitude, pushing softmax into flat regions with near-zero gradients. Scaling stabilizes gradient flow during backpropagation."
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Agentic AI Lessons
    # -------------------------------------------------------------------------
    {
        "topicSlug": "agentic-architectures",
        "subjectSlug": "agentic-ai",
        "title": "Autonomous Agent Loops & The ReAct Framework",
        "slug": "autonomous-agent-loops",
        "description": "Understand what differentiates an AI Agent from a plain chatbot, the ReAct loop, tool calling, and self-correction.",
        "estimatedTime": "30 mins",
        "difficulty": "Advanced",
        "order": 1,
        "isPublished": True,
        "interactiveType": "AgentWorkflowVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Chatbot vs AI Agent: The Difference",
                    "content": (
                        "• Chatbot: Passive single-turn responder. Input prompt in ➔ Output response out. Cannot browse the web, execute terminal commands, or verify facts.\n\n"
                        "• AI Agent: An autonomous goal-driven system equipped with:\n"
                        "  1. LLM Brain (Reasoning & Decision making)\n"
                        "  2. Tools (APIs, Python code interpreter, Database connectors, Web search)\n"
                        "  3. Memory (Short-term context window + Long-term vector store)\n"
                        "  4. Feedback Loop: Evaluates results of its actions and retries if an error occurs."
                    )
                },
                {
                    "type": "visualization",
                    "component": "AgentWorkflowVisualizer",
                    "initialState": {}
                },
                {
                    "type": "explanation",
                    "title": "The ReAct Loop: Reason + Act",
                    "content": (
                        "Published by Yao et al. (Princeton/Google), ReAct coordinates reasoning and action in a tight cycle:\n\n"
                        "1. Thought: \"The user asked for the current stock price of Apple. I do not have real-time financial data in my weights. I should call the stock_ticker API for AAPL.\"\n"
                        "2. Action: `call_api(ticker='AAPL')`\n"
                        "3. Observation: `{ 'price': 224.50, 'currency': 'USD' }`\n"
                        "4. Thought: \"I now have the verified live price. I can synthesize the final answer.\"\n"
                        "5. Final Answer: \"Apple (AAPL) is currently trading at $224.50 USD.\""
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "agentic-architectures",
        "subjectSlug": "agentic-ai",
        "title": "Tool Calling, Function Schemas & Agent Memory",
        "slug": "tool-calling-agent-memory",
        "description": "Define tools with JSON Schema, parse structured function calls, manage working memory vs episodic vector memory.",
        "estimatedTime": "30 mins",
        "difficulty": "Advanced",
        "order": 2,
        "isPublished": True,
        "interactiveType": "AgentWorkflowVisualizer",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "How Tool Calling Works Behind the Scenes",
                    "content": (
                        "Modern LLMs (OpenAI, Anthropic, Gemini) are trained to recognize JSON Schema tool definitions. "
                        "When the model determines a tool is needed, it stops generating text and outputs a structured JSON payload "
                        "containing the tool name and validated arguments. Your backend executes the function and feeds the return string back as a 'tool' message."
                    )
                },
                {
                    "type": "code",
                    "title": "Defining JSON Schema Tools for Agents",
                    "language": "python",
                    "code": (
                        "tools = [\n"
                        "    {\n"
                        "        \"type\": \"function\",\n"
                        "        \"function\": {\n"
                        "            \"name\": \"search_database\",\n"
                        "            \"description\": \"Query the company customer database for account balance\",\n"
                        "            \"parameters\": {\n"
                        "                \"type\": \"object\",\n"
                        "                \"properties\": {\n"
                        "                    \"customer_id\": {\"type\": \"string\", \"description\": \"Customer account UUID\"},\n"
                        "                    \"include_history\": {\"type\": \"boolean\", \"default\": False}\n"
                        "                },\n"
                        "                \"required\": [\"customer_id\"]\n"
                        "            }\n"
                        "        }\n"
                        "    }\n"
                        "]"
                    )
                },
                {
                    "type": "explanation",
                    "title": "The 3 Layers of Agent Memory",
                    "content": (
                        "• Sensory / Scratchpad Memory: Short-term context within the current prompt (tool call history, intermediate scratch notes).\n"
                        "• Episodic Memory: Memory of previous user interactions and past conversation trajectories stored in persistent databases.\n"
                        "• Semantic Memory: Facts, world knowledge, and corporate handbooks retrieved on-demand via vector search."
                    )
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # Deep Learning Lessons
    # -------------------------------------------------------------------------
    {
        "topicSlug": "neural-network-training",
        "subjectSlug": "deep-learning",
        "title": "Perceptrons & Multi-Layer Neural Networks",
        "slug": "perceptrons-multi-layer-networks",
        "description": "Understand the artificial neuron, linear combinations (z = Wx + b), and why non-linear activation functions are mandatory.",
        "estimatedTime": "25 mins",
        "difficulty": "Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "The Perceptron: Building Block of Deep Learning",
                    "content": (
                        "Proposed by Frank Rosenblatt in 1958, a perceptron models an individual biological neuron:\n\n"
                        "1. Inputs (x₁, x₂, ..., xₙ) are multiplied by respective Weights (w₁, w₂, ..., wₙ).\n"
                        "2. Weighted inputs are summed with a Bias term (b): z = Σ (wᵢ * xᵢ) + b.\n"
                        "3. The net input z is passed through an Activation Function a = σ(z) to produce the final output."
                    )
                },
                {
                    "type": "explanation",
                    "title": "Why Are Non-Linear Activation Functions Mandatory?",
                    "content": (
                        "Without non-linear activations (like ReLU, Sigmoid, Tanh), a 100-layer neural network is mathematically identical to a single 1-layer linear regression! "
                        "Because the combination of linear functions is always just another linear function: W₂(W₁x) = (W₂W₁)x = W_combined x.\n\n"
                        "Non-linearities allow the network to approximate any continuous function (Universal Approximation Theorem), "
                        "bending decision boundaries around complex non-linear patterns."
                    )
                },
                {
                    "type": "code",
                    "title": "Popular Activation Functions in Python",
                    "language": "python",
                    "code": (
                        "import numpy as np\n\n"
                        "# 1. ReLU (Rectified Linear Unit): Standard in hidden layers (prevents vanishing gradients)\n"
                        "def relu(z):\n"
                        "    return np.maximum(0, z)\n\n"
                        "# 2. Sigmoid: Outputs probability in [0, 1] (binary classification output layer)\n"
                        "def sigmoid(z):\n"
                        "    return 1 / (1 + np.exp(-z))\n\n"
                        "# 3. Softmax: Outputs probability distribution over k classes (sum = 1.0)\n"
                        "def softmax(z):\n"
                        "    exp_z = np.exp(z - np.max(z))\n"
                        "    return exp_z / np.sum(exp_z)"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "neural-network-training",
        "subjectSlug": "deep-learning",
        "title": "Forward Propagation, Loss & Backpropagation",
        "slug": "forward-backpropagation-chain-rule",
        "description": "Master forward activation computation, cross-entropy loss, and computing weight gradients via the calculus chain rule.",
        "estimatedTime": "35 mins",
        "difficulty": "Intermediate to Advanced",
        "order": 2,
        "isPublished": True,
        "interactiveType": None,
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Forward Pass vs Backward Pass",
                    "content": (
                        "• Forward Propagation: Input features flow layer by layer through linear transforms and activation functions to compute predicted probabilities ŷ, "
                        "and compare with actual target y using a Loss Function (e.g., Binary Cross-Entropy).\n\n"
                        "• Backward Propagation: The process of propagating the error backwards from the output layer to early layers using the Calculus Chain Rule, "
                        "calculating the partial derivative of Loss with respect to every single weight: ∂L/∂W."
                    )
                },
                {
                    "type": "explanation",
                    "title": "The Chain Rule in Action",
                    "content": (
                        "For a 2-layer network: Input x ➔ Layer 1 (z₁ = W₁x, a₁ = σ(z₁)) ➔ Layer 2 (z₂ = W₂a₁, ŷ = σ(z₂)) ➔ Loss L(y, ŷ).\n\n"
                        "To compute how changing weight W₁ affects the final Loss L, we chain the gradients:\n\n"
                        "∂L / ∂W₁ = (∂L / ∂ŷ) * (∂ŷ / ∂z₂) * (∂z₂ / ∂a₁) * (∂a₁ / ∂z₁) * (∂z₁ / ∂W₁)\n\n"
                        "Each layer computes its local gradient and passes the incoming error gradient back to the preceding layer."
                    )
                },
                {
                    "type": "callout",
                    "variant": "info",
                    "content": "Modern Optimizers: SGD (basic), Momentum (accelerates in consistent directions), RMSProp (adapts learning rate per parameter), Adam (Adaptive Moment Estimation: combines Momentum + RMSProp, the industry standard)."
                }
            ]
        }
    },

    # -------------------------------------------------------------------------
    # MongoDB Lessons
    # -------------------------------------------------------------------------
    {
        "topicSlug": "mongodb-document-modeling",
        "subjectSlug": "mongodb",
        "title": "Document Foundations & CRUD Query Operators",
        "slug": "mongodb-crud-operations",
        "description": "Learn flexible JSON/BSON document structures, embedding vs referencing, and query operators ($gt, $in, $regex).",
        "estimatedTime": "25 mins",
        "difficulty": "Beginner to Intermediate",
        "order": 1,
        "isPublished": True,
        "interactiveType": "MongoPlayground",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "Relational Tables vs MongoDB BSON Documents",
                    "content": (
                        "In relational databases, data is split across rigid tables linked by foreign keys. In MongoDB, data is stored in flexible, JSON-like BSON (Binary JSON) documents.\n\n"
                        "• RDBMS Concept ➔ MongoDB Equivalent:\n"
                        "  - Database ➔ Database\n"
                        "  - Table ➔ Collection\n"
                        "  - Row ➔ Document\n"
                        "  - Column ➔ Field\n"
                        "  - Primary Key (`id`) ➔ ObjectId (`_id`)\n"
                        "  - Table Join ➔ Embedded Documents or `$lookup`"
                    )
                },
                {
                    "type": "visualization",
                    "component": "MongoPlayground",
                    "initialState": {}
                },
                {
                    "type": "code",
                    "title": "Essential PyMongo CRUD Queries",
                    "language": "python",
                    "code": (
                        "from pymongo import MongoClient\n\n"
                        "client = MongoClient('mongodb://localhost:27017')\n"
                        "db = client['learning_platform']\n\n"
                        "# 1. Create (Insert)\n"
                        "db.lessons.insert_one({\n"
                        "    'title': 'MongoDB Queries',\n"
                        "    'difficulty': 'Beginner',\n"
                        "    'tags': ['nosql', 'database'],\n"
                        "    'views': 1200\n"
                        "})\n\n"
                        "# 2. Read with Operators ($gt, $in)\n"
                        "popular_lessons = list(db.lessons.find({\n"
                        "    'views': {'$gt': 1000},\n"
                        "    'difficulty': {'$in': ['Beginner', 'Intermediate']}\n"
                        "}, {'title': 1, 'views': 1, '_id': 0}))\n\n"
                        "# 3. Update ($set, $inc)\n"
                        "db.lessons.update_many(\n"
                        "    {'difficulty': 'Beginner'},\n"
                        "    {'$inc': {'views': 1}}  # Atomic increment\n"
                        ")"
                    )
                }
            ]
        }
    },
    {
        "topicSlug": "mongodb-document-modeling",
        "subjectSlug": "mongodb",
        "title": "Indexing Strategies & Aggregation Pipelines",
        "slug": "mongodb-indexing-aggregations",
        "description": "Master single/compound/text indexes, index selectivity, and analytical multi-stage aggregation pipelines ($match, $group, $sort).",
        "estimatedTime": "30 mins",
        "difficulty": "Intermediate",
        "order": 2,
        "isPublished": True,
        "interactiveType": "MongoPlayground",
        "content": {
            "sections": [
                {
                    "type": "explanation",
                    "title": "MongoDB Indexing Strategies",
                    "content": (
                        "Without indexes, MongoDB performs a Collection Scan (`COLLSCAN`), inspecting every single document in the collection to satisfy a query.\n\n"
                        "• Single Field Index: `db.users.create_index([('email', 1)], unique=True)`\n"
                        "• Compound Index: `db.progress.create_index([('user_id', 1), ('lesson_id', 1)])` (Rule: Equality, Sort, Range - ESR rule)\n"
                        "• Text Search Index: `db.lessons.create_index([('title', 'text'), ('description', 'text')])`\n"
                        "• Explain Plan: Use `db.collection.find().explain('executionStats')` to verify that `totalDocsExamined` equals `nReturned` (Index Scan `IXSCAN`)."
                    )
                },
                {
                    "type": "code",
                    "title": "Analytical Aggregation Pipeline",
                    "language": "python",
                    "code": (
                        "# Pipeline: Filter completed lessons -> Group by subject -> Calculate stats\n"
                        "pipeline = [\n"
                        "    # Stage 1: Match only completed items\n"
                        "    {'$match': {'status': 'completed'}},\n"
                        "    # Stage 2: Group by subject and count completions\n"
                        "    {'$group': {\n"
                        "        '_id': '$subject_slug',\n"
                        "        'total_completions': {'$sum': 1},\n"
                        "        'avg_score': {'$avg': '$progress_percentage'}\n"
                        "    }},\n"
                        "    # Stage 3: Sort descending by completions\n"
                        "    {'$sort': {'total_completions': -1}},\n"
                        "    # Stage 4: Limit to top 5\n"
                        "    {'$limit': 5}\n"
                        "]\n"
                        "results = list(db.progress.aggregate(pipeline))"
                    )
                }
            ]
        }
    }
]
