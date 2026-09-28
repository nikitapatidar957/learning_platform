# The Transformer Architecture Deep Dive

Understand how the 2017 'Attention Is All You Need' paper replaced RNNs/LSTMs with parallelizable self-attention.

---

## Why Did Transformers Replace RNNs and LSTMs?

Prior to 2017, NLP relied on Recurrent Neural Networks (RNNs) and LSTMs. They processed text word by word sequentially:
• Bottleneck 1: Vanishing/Exploding Gradients on long documents (forgetting words from 50 tokens earlier).
• Bottleneck 2: ZERO GPU Parallelization! Word 50 could not be processed until Word 49 was done.

The Transformer discarded recurrence entirely: It takes all 4,000 words in a document simultaneously in parallel and uses Self-Attention to calculate how every word relates to every other word.

## Encoder-Only vs Decoder-Only vs Encoder-Decoder

• Encoder-Only (e.g., BERT, RoBERTa):
  Bidirectional attention (can look forward and backward). Best for text classification, sentiment analysis, and generating vector embeddings.

• Decoder-Only (e.g., GPT-4, Llama 3, Mistral):
  Causal masked attention (tokens can only attend to prior tokens). Best for autoregressive generative text and code completion.

• Encoder-Decoder (e.g., T5, BART):
  Encodes input sequence, then decodes output sequence. Best for machine translation and document summarization.

