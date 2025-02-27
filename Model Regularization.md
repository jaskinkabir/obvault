# Regularization
- Defined as any modification to a learning algorithm that is intended to reduce its generalization error but not its training error
	- Minimizing training error is to solve underfit
	- Minimizing the gap between validation and training error is to solve overfit. **This** is the goal of regularization
## Model Capacity
- Capacity is the ability of a model to fit many different functions
- We can reduce overfitting by reducing the *Hypothesis Space*
	- **Hypothesis Space:** The set of all functions the model can fit
## Norm Penalties
- MAP esitmation:  Guess most likely wieghts given training data and some prior knowledge about weights
- Squared L2: Encourages small weights, equivalent to MAP Bayesian estimation with Gaussian prior
- $$\Omega_{L_{2}}=\|w\|^{2}$$
- L1: Penalize on absolute value of weights
- $$\Omega_{L_{1}}(\theta)=|w|=\sum_{w \in\theta}|w|$$
- Encourages sparsity, equivalent to MAP Bayesian estimation with Laplace prior
	- Laplace distribution has infinite density at mean
- 
## Sparsification Tendency of L1
- For L1 penalty, the component of the gradient that depends on $\Omega$ is constant with respect to $|w|$, except for at $w=0$
- However the gradient for L2 penalty decreases as |w| decreases, and eventually reaches equilibrium with $w \neq 0$
- In theory, L2 shouldn't reduce any weights to 0, but L1 will
	- In practice, they both reduce weights to 0
- 
For class #IoT-ML 