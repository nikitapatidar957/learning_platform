# Forward Propagation, Loss & Backpropagation

Master forward activation computation, cross-entropy loss, and computing weight gradients via the calculus chain rule.

---

## Forward Pass vs Backward Pass

• Forward Propagation: Input features flow layer by layer through linear transforms and activation functions to compute predicted probabilities ŷ, and compare with actual target y using a Loss Function (e.g., Binary Cross-Entropy).

• Backward Propagation: The process of propagating the error backwards from the output layer to early layers using the Calculus Chain Rule, calculating the partial derivative of Loss with respect to every single weight: ∂L/∂W.

## The Chain Rule in Action

For a 2-layer network: Input x ➔ Layer 1 (z₁ = W₁x, a₁ = σ(z₁)) ➔ Layer 2 (z₂ = W₂a₁, ŷ = σ(z₂)) ➔ Loss L(y, ŷ).

To compute how changing weight W₁ affects the final Loss L, we chain the gradients:

∂L / ∂W₁ = (∂L / ∂ŷ) * (∂ŷ / ∂z₂) * (∂z₂ / ∂a₁) * (∂a₁ / ∂z₁) * (∂z₁ / ∂W₁)

Each layer computes its local gradient and passes the incoming error gradient back to the preceding layer.

Modern Optimizers: SGD (basic), Momentum (accelerates in consistent directions), RMSProp (adapts learning rate per parameter), Adam (Adaptive Moment Estimation: combines Momentum + RMSProp, the industry standard).

