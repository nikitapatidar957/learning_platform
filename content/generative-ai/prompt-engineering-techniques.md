# Prompt Engineering Frameworks & Techniques

Master Zero-shot, Few-shot (in-context learning), Chain-of-Thought (CoT), ReAct prompting, and inference hyper-parameters.

---

## Prompt Engineering Techniques

Prompt engineering is the practice of crafting and structuring inputs to guide large language models toward reliable, accurate outputs:

• Zero-Shot Prompting: Providing the instruction directly without any examples.

• Few-Shot Prompting (In-Context Learning): Providing 2 to 5 high-quality input-output demonstration pairs in the prompt. The model observes the pattern and formats its output accordingly without weight fine-tuning!

• Chain-of-Thought (CoT): Prompting the model with "Let's think step by step". By forcing the model to generate intermediate reasoning tokens, accuracy on math, logic, and multi-step coding problems jumps dramatically!

## Chain-of-Thought Few-Shot Prompt Example

```python
prompt = """
Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. 
Each can has 3 tennis balls. How many tennis balls does he have now?
A: Roger started with 5 balls. 2 cans of 3 tennis balls each is 2 * 3 = 6 balls. 
5 + 6 = 11. The answer is 11.

Q: The cafeteria had 23 apples. If they used 20 to make lunch and bought 6 more, 
how many apples do they have?
A: Let's think step by step:
"""
```

## Inference Hyper-Parameters: Temperature, Top-p, Top-k

• Temperature (0.0 to 1.5+): Controls randomness. Lower values (0.0 - 0.2) make outputs focused, deterministic, and analytical (best for code/math). Higher values (0.7 - 1.0) increase diversity and vocabulary variety (best for storytelling/creative writing).

• Top-p (Nucleus Sampling): Dynamically cuts off the candidate token pool to the smallest set whose cumulative probability sums to p (e.g., 0.90).

• Top-k: Hard-limits candidate tokens to the top k highest probability candidates.

