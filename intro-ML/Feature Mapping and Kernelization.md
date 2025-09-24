Continues [[Dimensionality Reduction and Feature Selection]]

# Feature Mapping
- Consider a feature space in which the points belonging to each class are not linearly separable
- Feature mapping maps the original feature vector $x$ to an expanded verson $\phi(x)$
	- In the $\phi$-space, the data may be linearly separable
	- ![[Pasted image 20241022134912.png]]
- ![[Pasted image 20241022135453.png]]
# Pros and Cons
## Pros
- Can turn non-linear classification problem into linear problem
## Cons:
- Feature explosion creates issues
	- More expensive to train
	- More training examples needed to prevent overfit
For class #intro-ML