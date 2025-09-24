Continues [[ML Optimization Fundamentals]]
Continued by [[Strong Convexity and Smoothness]]
Expanded by [[Matrix Positivity]]
# Norm
- Defined as $$\|u\|_{p}=\left( \sum_{i=1}^d |u_{i}|^p\right)^{\frac{1}{p}}$$
	- If no p is specified, the convention states p is 2
## Properties
1. $$\|x\|=0 \iff x=0$$
2. Homogeneity $$\|\alpha x\|=|\alpha|*\|x\|,\, \alpha \in \mathbb{R}$$
3. **Triangle Inequality**
	1. $$\|x+y\| \leq \|x\| + \|y\|$$
	2. Proven through this diagram
		1. ![[Pasted image 20250122145207.png]]
		2. The distance from origin to x+y must be leq the distance to x plus the distance to y
		3. Because the direct path to x+y must be shorter or the same

# Jensen's Inequality
- Consider a convex function $f$. It holds that
-  $$f\left( \sum _{i=1}^{n}\lambda_{i}x_{i} \right) \leq \sum_{i=1}^{n}\lambda_{i}f(x_{i})$$
	- $\lambda_{i} \geq 0,\, \text{and} \sum_{i}\lambda_{i}=1$
		- The summation on the left is called a convex combination
- Intuitively, this follows from properties 2 and 3 of norms, since the norm is a convex function
# First Order Definiton of Convexity
- A function is convex if it is differentiable and: 
- $$f(y) \geq f(x) + \nabla f(x)^{T}(y-x)$$
# Second Order Definition
### Hessian Matrix
- The Hessian matrix is the second order gradient of a function. It is defined as the following symmetric matrix
- $$\nabla ^{2}f(x) := \begin{pmatrix}
\frac{d^{2}f(x)}{dx_{1}^{2}} & \frac{d^{2}f(x)}{dx_{1}dx_{2}} & \dots & \frac{d^{2}f(x)}{dx_{1}dx_{n}} \\
\frac{d^{2}f(x)}{dx_{2}dx_{1}} & \frac{d^{2}f(x)}{dx_{2}^{2}} & \dots & \frac{d^{2}f(x)}{dx_{2}dx_{n}} \\
\vdots & \vdots &\ddots& \vdots \\
\frac{d^{2}f(x)}{dx_{n}dx_{1}} & \frac{d^{2}f(x)}{dx_{n}dx_{2}} & \dots &\frac{d^{2}f(x)}{dx_{n}dx_{n}}
\end{pmatrix}$$
- If each element of this matrix can be referred to with $H_{a,\,b}$ then
- $$H_{a,\, b}=\frac{d^{2}f(x)}{dx_{a}dx_{b}}$$
	- This is the partial second order derivative of f with respect to $x_{a}$  multiplied by the partial $x_{b}$
## Definition
- The **Second Order Definition of Convexity** states that $f$ is convex if
	- $$\nabla f^{2}(x) \succeq 0$$
	- Notice that the Hessian matrix is symmetric. This means that finding if the Hessian is positive semidefinite is trivial
	- See [[Matrix Positivity]] for expansion on positive semidefinite matrices
- This means that $$y^{T}\nabla^{2}f(x)y \geq 0,\, \forall y \in dom(f)$$
	- Why does this mean $f$ is convex?
# Convex Optimization Problems
## Definition
- A problem is convex if
1. The objective function is convex
	1. This is the function we are trying to minimize
	2. Typically the loss function in ML
		1. $\min_{x} f(x)$, $f(x)$ is the objective function
2. The constraint set is also convex
	1. If $x$ is the parameter of the objective function $f(x)$, the constraint set $\Omega$ is the set of all valid values of $x$
## Local and Global Optima
- For any optimization function we can define local and global optima
### Local Optima
- Intuition
	- Draw a circle of radius $\epsilon$ around $x$
	- If we can find a point $y$ within this circle, ie whose distance from x < $\epsilon$, then we know that y beats $x$
	- $f(x) \leq f(y)$
- $x \in \Omega$ is a local optimum if 
	- $\exists \epsilon > 0 \text{ s.t } f(x) \leq f(y),\, \forall y \in \Omega : \|x-y\| \leq \epsilon$
		- $\Omega$ is the constraint set, the set of all possible solutions
- In other words, can you draw a circle around x where every other point on the function is greater than $f(x)$
- The point x beats all other points within that circle of radius $\epsilon$
### Global Optimum
- $x \in \Omega$ is g.o. if
	- $f(x) \leq f(y),\, \forall y \in \Omega$
- g.o $\implies$ l.o
	- A global optimum is always local but not vice versa
- **Theorem**
	- For convex problems, every l.o. is g.o.
	- Once you stumble upon a local optimum, you don't have to keep searching. You've already found the best possible solution, the global optimum.
- Our goal is to study rates of convergence

### Theorem: For Convex Problems, Every L.O. is also G.O.
#### Proof:
- Assume $x$ is l.o. but not g.o.
- This means $\exists \epsilon > 0 \text{ s.t } f(x) \leq f(y),\, \forall y \in \Omega : \|x-y\| \leq \epsilon$
- However, because $x$ is not g.o. $\exists z \text{ s.t. } f(z) < f(x)$
- Now let $y=\Theta x+(1-\Theta)z,\, \text{ s.t } \|y-x\| < \epsilon$
	- $y$ is some point along the line between $x$ and $z$ that lies within the $\epsilon-$neighborhood of $x$
- Because $f$ is convex, $f(\Theta x+ (1-\Theta)z) \leq \Theta f(x)+(1-\Theta)f(z),\, \forall x,\,z \in \Omega$
	- $f(y) \leq \Theta f(x) + (1-\Theta)f(z)$
		- $f(y)$ is lower than some point on the line between $f(x)$ and $f(z)$
		- Because $f(z) < f(x),\,f(y) < f(x)$
	- 
	- 
## Constrained Optimization
- Define $x^{*}$ is the optimum solution
- For unconstrained optimization, $\nabla f(x^{*})=0$
	- From high school
- But what if the constraints on $x$ defined by $\Omega$ don't include $x^{*})$
- The condition is now as follows
	- $$\nabla f(x^{*})^{T}(y-x^{*}) \geq 0,\,  \forall y \in \Omega$$
- Why does this condition work?
	- ![[Pasted image 20250122154111.png]]
	- The gradient of $f$ at $x^{*}$ points in the direction in which the function increases
		- This pulls from the CZ inequality
		- 
	- If you choose a point $y$ in the constraint set that points from $x^{*}$ in the direction of the gradient, that means that the function increases as it moves from $x^{*}$ to $y$
	- If this is true $\forall y \in \Omega$, **that means $x^{*}$ is the global optimum**


- Reread notes in detail
- Read ahead
	- on monday we will finish fundamentals pdf
	- Read gaps ahead and search/ask chatgpt
	- Be more prepared before lectures
- Come to office hours

For class #optimization-ml