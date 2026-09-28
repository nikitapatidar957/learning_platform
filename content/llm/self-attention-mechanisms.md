# Self-Attention Mechanics: Query, Key & Value

Master the Q, K, V mathematical formula, scaled dot-product attention, and multi-head projection spaces.

---

## The Retrieval Analogy for Query, Key, and Value

Think of YouTube or a library search:
• Query (Q): What you type into the search bar ('What is machine learning?').
• Key (K): The title / tags on all available video clips ('Introduction to ML', 'Baking Cookies', 'Python Basics').
• Value (V): The actual video content you watch.

In Self-Attention, each word in the sentence projects into a Query, a Key, and a Value vector via trained weight matrices W_q, W_k, W_v.

## The Famous Scaled Dot-Product Attention Formula

```python
# Attention(Q, K, V) = softmax( (Q * K.T) / sqrt(d_k) ) * V

import numpy as np

def softmax(x):
    e_x = np.exp(x - np.max(x, axis=-1, keepdims=True))
    return e_x / np.sum(e_x, axis=-1, keepdims=True)

def scaled_dot_product_attention(Q, K, V):
    d_k = Q.shape[-1]  # Dimension of key vectors
    # 1. Compute attention raw scores (dot product)
    scores = np.matmul(Q, K.swapaxes(-2, -1))
    # 2. Scale by sqrt(d_k) to prevent vanishing gradients in softmax
    scaled_scores = scores / np.sqrt(d_k)
    # 3. Softmax to get probability distribution (attention weights)
    weights = softmax(scaled_scores)
    # 4. Weighted sum of values
    output = np.matmul(weights, V)
    return output, weights
```

Why scale by √d_k? For large vector dimensions (e.g., d_k = 128), dot products grow large in magnitude, pushing softmax into flat regions with near-zero gradients. Scaling stabilizes gradient flow during backpropagation.

