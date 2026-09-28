# Generative vs Traditional AI & Model Types

Understand generative vs discriminative modeling, GANs, VAEs, Diffusion models, Transformers, and mitigating hallucination.

---

## What is Generative AI?

Generative AI refers to algorithms capable of generating novel, human-like content (text, code, images, audio, synthetic data) by learning the underlying probability distribution of massive training datasets.

• Discriminative AI: Models P(Y | X) ➔ Distinguishes between existing categories (e.g., 'Is this image a dog or a cat?').
• Generative AI: Models P(X) or P(X | Y) ➔ Generates new instances from the learned data distribution (e.g., 'Generate a photorealistic picture of a golden retriever in space').

## The 4 Core Generative AI Model Architectures

1. Generative Adversarial Networks (GANs):
   A two-player min-max game: A Generator creates fake samples, and a Discriminator tries to catch them. Over iterations, both become exceptionally skilled.

2. Variational Autoencoders (VAEs):
   Compresses inputs into a smooth continuous latent distribution, then samples points to reconstruct novel variants.

3. Diffusion Models (Midjourney, Stable Diffusion):
   Gradually destroys images by adding Gaussian noise over hundreds of steps, then trains a deep neural net to reverse the process and denoise pure static into crisp art.

4. Transformers (GPT, Claude, Gemini, Llama):
   Uses self-attention to model long-range relationships between tokens for autoregressive text and code generation.

## Why Do LLMs Hallucinate?

LLMs are stochastic next-token prediction engines. They do NOT possess a conscious understanding of truth; they output words with high conditional probability. When training data is ambiguous or knowledge is missing from their parametric memory, they fabricate plausible-sounding falsehoods.

Mitigations: RAG (grounding with external search/docs), low temperature, strict system prompts, and multi-step verification tools.

Hallucination vs Creativity: The same probabilistic mechanism that creates a poetic metaphor also invents a non-existent legal court case if left unconstrained.

