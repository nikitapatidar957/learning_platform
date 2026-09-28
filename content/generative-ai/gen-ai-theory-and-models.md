# 🔹 What is Generative AI?

**Generative AI (Gen AI)** is a type of artificial intelligence that can **create new content** like text, images, audio, video, or code by learning patterns from existing data. 

“Generative AI is a class of AI models that learn data patterns and generate new, human-like content instead of just predicting or classifying.” ([NareshIT][2])

### 🔥 Key Idea

* Traditional AI → Predicts (e.g., spam detection)
* Generative AI → Creates (e.g., writes an email, generates images)

---

# 🔹 Types of Generative AI Models

1. **Large Language Models (LLMs)** – ChatGPT, Gemini
2. **GANs (Generative Adversarial Networks)** – Image generation
3. **VAEs (Variational Autoencoders)**
4. **Diffusion Models** – Stable Diffusion
5. **Transformers** – backbone of modern AI

---

# 🔹 Applications of Gen AI

* Chatbots & virtual assistants
* Image generation (Midjourney, DALL·E)
* Code generation (Copilot)
* Content writing
* Drug discovery
* Video & music generation

### 2. Difference: Generative AI vs Traditional AI

* Traditional AI → Classification & prediction
* Generative AI → Creates new data/content 

---

### 3. What are LLMs?

* Models trained on huge text datasets
* Predict next word/token
* Generate human-like text 

---

### 4. What are Tokens?

* Small units of text (word/subword/characters) 

---

### 5. What are Embeddings?

* Numerical vector representation of words
* Helps model understand meaning 

---

### 6. What is Prompt Engineering?

* Designing inputs (prompts) to get best output from AI


### 7. What are Transformers?

* Deep learning architecture using **attention mechanism**
* Handles long-range dependencies better than RNNs 

---

### 8. What is Attention Mechanism?

* Helps model focus on important words in input

---

### 9. What is Self-Attention?

* Model relates words within same sentence

---

### 10. What is GAN?

👉 Two networks:

* Generator → creates fake data
* Discriminator → checks real vs fake 

---

### 11. What is VAE?

* Encoder + Decoder model
* Generates new data using probability distribution 

---

### 12. What are Diffusion Models?

* Start with noise → gradually remove noise → generate image 

---

### 13. What is Fine-tuning?

* Training a pretrained model on specific dataset

---

### 14. What is RAG (Retrieval-Augmented Generation)?

* Combines:

  * Retrieval (search data)
  * Generation (LLM response)

---

---

### 15. Generative vs Discriminative Models

* Generative → learns data distribution (P(x, y))
* Discriminative → predicts label (P(y|x)) 

---

### 16. What is Temperature in LLMs?

* Controls randomness
* High → creative
* Low → deterministic

---

### 17. What is Hallucination in AI?

* Model generates incorrect but confident answers

---

### 18. What is Overfitting in Gen AI?

* Model memorizes training data instead of learning

---

### 19. What is Latent Space?

* Compressed representation of data

---

### 20. What is Beam Search?

* Technique to improve text generation quality

---

## 🧠 4. Practical / Scenario Questions

---

### 21. How would you build a chatbot using Gen AI?

Steps:

1. Choose LLM (GPT, Llama)
2. Add knowledge base (RAG)
3. Fine-tune (optional)
4. Deploy via API

---

### 22. How do you handle hallucinations?

* Use RAG
* Add constraints in prompt
* Use verified data

---

### 23. How to ensure data privacy?

* Mask sensitive data
* Use private deployment
* Encryption & access control 

---

### 24. How do you evaluate Gen AI models?

* BLEU score (text)
* ROUGE score
* Human evaluation

---

## ⚡ 5. Latest / Trending Questions (VERY IMPORTANT)

---

### 25. What is Prompt Engineering vs Fine-Tuning?

* Prompt → no training, just input design
* Fine-tuning → retraining model

---

### 26. What are Foundation Models?

* Large pretrained models usable for multiple tasks

---

### 27. What is Multimodal AI?

* Handles text + image + audio together

---

### 28. What is AI Alignment?

* Ensuring AI behaves ethically

---

### 29. What are Ethical Issues in Gen AI?

* Bias
* Deepfakes
* Copyright issues 

---

## 🧪 6. Coding / Hands-on Questions

---

### 30. Write code to call OpenAI API

### 31. Build a chatbot using LangChain

### 32. Create embeddings using Hugging Face

### 33. Implement RAG pipeline

### 34. Fine-tune a model

---

# 🧠 1. What is Generative AI?

### ✅ Easy Answer:

Generative AI is AI that can **create new things** like text, images, code, or videos by learning from existing data.

👉 Example:

* ChatGPT → writes answers
* DALL·E → creates images

---

### 🔍 Cross Questions + Answers:

**Q: Does it copy data?**
👉 No. It learns patterns and creates new content, not exact copies.

**Q: Can it think like humans?**
👉 No. It predicts based on data, not real understanding.

**Q: Can it generate new ideas?**
👉 Yes, but based on patterns it has already learned.

---

### 🎯 What to say in interview:

> “Generative AI creates new content by learning patterns from data.”

---

# 🧠 2. Generative AI vs Traditional AI

### ✅ Easy Answer:

* Traditional AI → gives answers (like yes/no, classification)
* Generative AI → creates new content

👉 Example:

* Spam filter → Traditional AI
* ChatGPT → Generative AI

---

### 🔍 Cross Questions:

**Q: Can generative AI do prediction also?**
👉 Yes, but its main strength is content creation.

**Q: Which is more powerful?**
👉 Generative AI is more flexible.

---

### 🎯 Tip:

Say:

> “Traditional AI predicts, Generative AI creates.”

---

# 🧠 3. What are LLMs (Large Language Models)?

### ✅ Easy Answer:

LLMs are AI models trained on **huge text data** to understand and generate human-like text.

👉 Example:

* ChatGPT
* Gemini

👉 How they work:
They **predict the next word** in a sentence.

---

### 🔍 Cross Questions:

**Q: Why are they called ‘large’?**
👉 Because they are trained on massive data and have billions of parameters.

**Q: Do they understand meaning?**
👉 They understand patterns, not real meaning.

---

### 🎯 Tip:

> “LLMs predict the next word to generate meaningful text.”

---

# 🧠 4. What are Tokens?

### ✅ Easy Answer:

Tokens are **small pieces of text** that AI reads.

👉 Example:
“ChatGPT is amazing”
→ ["Chat", "GPT", "is", "amazing"]

---

### 🔍 Cross Questions:

**Q: Why not use full words?**
👉 Smaller tokens help model learn better.

**Q: Why are tokens important?**
👉 Cost and speed depend on tokens.

---

### 🎯 Tip:

> “Tokens are the basic units AI uses to process text.”

---

# 🧠 5. What are Embeddings?

### ✅ Easy Answer:

Embeddings are **numbers (vectors) that represent meaning of words or sentences**.

👉 Example:

* “King” and “Queen” → similar embeddings

---

### 🔍 Cross Questions:

**Q: Why needed?**
👉 Computers understand numbers, not words.

**Q: Where used?**
👉 Search, recommendation, chatbots (RAG)

---

### 🎯 Tip:

> “Embeddings convert text into numbers so AI can understand meaning.”

---

# 🧠 6. What is Prompt Engineering?

### ✅ Easy Answer:

It means **writing better input (prompt) to get better output from AI**.

👉 Example:
Bad → “Tell me about AI”
Good → “Explain AI in 5 points for beginners”

---

### 🔍 Cross Questions:

**Q: Why is it important?**
👉 Output depends heavily on input.

**Q: What is few-shot prompting?**
👉 Giving examples in prompt.

---

### 🎯 Tip:

> “Prompt engineering is like giving instructions to AI.”

---

# 🧠 7. What are Transformers?

### ✅ Easy Answer:

Transformers are the **technology behind modern AI like ChatGPT**.

👉 They help AI:

* Understand context
* Process long sentences

---

### 🔍 Cross Questions:

**Q: Why not use old models like RNN?**
👉 Transformers are faster and better with long text.

---

### 🎯 Tip:

> “Transformers made modern AI possible.”

---

# 🧠 8. What is Attention?

### ✅ Easy Answer:

Attention helps AI **focus on important words**.

👉 Example:
“I went to the bank to deposit money”
→ AI focuses on “money” to understand “bank”

---

### 🔍 Cross Questions:

**Q: Why is attention needed?**
👉 Not all words are equally important.

---

### 🎯 Tip:

> “Attention helps AI focus on relevant information.”

---

# 🧠 9. What is GAN?

### ✅ Easy Answer:

GAN has two parts:

* Generator → creates fake data
* Discriminator → checks if real or fake

👉 They compete and improve.

---

### 🔍 Cross Questions:

**Q: Why use GAN?**
👉 To generate realistic images.

**Q: Problem with GAN?**
👉 Hard to train.

---

### 🎯 Tip:

> “GAN is like a forger vs police game.”

---

# 🧠 10. What are Diffusion Models?

### ✅ Easy Answer:

They create images by:

1. Adding noise
2. Removing noise step by step

---

### 🔍 Cross Questions:

**Q: Why better than GAN?**
👉 More stable and realistic results.

---

### 🎯 Tip:

> “Diffusion models slowly refine noise into images.”

---

# 🧠 11. What is Fine-tuning?

### ✅ Easy Answer:

Training a pretrained model on **your specific data**.

👉 Example:

* ChatGPT → trained for medical chatbot

---

### 🔍 Cross Questions:

**Q: Why not train from scratch?**
👉 Too expensive.

**Q: Alternative?**
👉 RAG

---

### 🎯 Tip:

> “Fine-tuning customizes AI for specific tasks.”

---

# 🧠 12. What is RAG?

### ✅ Easy Answer:

RAG = AI + Search

👉 It:

1. Searches data
2. Sends to AI
3. AI answers

---

### 🔍 Cross Questions:

**Q: Why use RAG?**
👉 Reduces wrong answers.

**Q: Tools used?**
👉 Vector DB (Pinecone, FAISS)

---

### 🎯 Tip:

> “RAG makes AI more accurate using real data.”

---

# 🧠 13. What is Temperature?

### ✅ Easy Answer:

Controls how creative AI is.

* Low → safe answers
* High → creative answers

---

### 🔍 Cross Questions:

**Q: When use low temperature?**
👉 Facts, coding.

**Q: When high?**
👉 Story writing.

---

### 🎯 Tip:

> “Temperature controls randomness.”

---

# 🧠 14. What is Hallucination?

### ✅ Easy Answer:

When AI gives **wrong answer confidently**.

---

### 🔍 Cross Questions:

**Q: Why happens?**
👉 AI predicts, not verifies.

**Q: How reduce?**
👉 RAG, better prompts.

---

### 🎯 Tip:

> “AI doesn’t know truth, it predicts probability.”

---

# 🧠 15. Evaluation of Gen AI

### ✅ Easy Answer:

Checking how good AI output is.

👉 Methods:

* BLEU, ROUGE
* Human review

---

### 🔍 Cross Questions:

**Q: Why human needed?**
👉 AI quality is subjective.

---

### 🎯 Tip:

> “Evaluation is still difficult in Gen AI.”

---

# 🧠 16. Multimodal AI

### ✅ Easy Answer:

AI that understands:

* Text + Image + Audio

---

### 🔍 Cross Questions:

**Q: Example?**
👉 Upload image → AI explains it.

---

### 🎯 Tip:

> “Multimodal AI understands multiple data types.”

---

# 🧠 17. Ethical Issues

### ✅ Easy Answer:

Problems like:

* Bias
* Fake content
* Privacy

---

### 🔍 Cross Questions:

**Q: How to solve?**
👉 Filters, policies, human review.

---

### 🎯 Tip:

> “Ethics is very important in AI.”

