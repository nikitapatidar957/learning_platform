# Perceptrons & Multi-Layer Neural Networks

Understand the artificial neuron, linear combinations (z = Wx + b), and why non-linear activation functions are mandatory.

---

## The Perceptron: Building Block of Deep Learning

Proposed by Frank Rosenblatt in 1958, a perceptron models an individual biological neuron:

1. Inputs (x₁, x₂, ..., xₙ) are multiplied by respective Weights (w₁, w₂, ..., wₙ).
2. Weighted inputs are summed with a Bias term (b): z = Σ (wᵢ * xᵢ) + b.
3. The net input z is passed through an Activation Function a = σ(z) to produce the final output.

## Why Are Non-Linear Activation Functions Mandatory?

Without non-linear activations (like ReLU, Sigmoid, Tanh), a 100-layer neural network is mathematically identical to a single 1-layer linear regression! Because the combination of linear functions is always just another linear function: W₂(W₁x) = (W₂W₁)x = W_combined x.

Non-linearities allow the network to approximate any continuous function (Universal Approximation Theorem), bending decision boundaries around complex non-linear patterns.

## Popular Activation Functions in Python

```python
import numpy as np

# 1. ReLU (Rectified Linear Unit): Standard in hidden layers (prevents vanishing gradients)
def relu(z):
    return np.maximum(0, z)

# 2. Sigmoid: Outputs probability in [0, 1] (binary classification output layer)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 3. Softmax: Outputs probability distribution over k classes (sum = 1.0)
def softmax(z):
    exp_z = np.exp(z - np.max(z))
    return exp_z / np.sum(exp_z)
```

