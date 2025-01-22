# Cauchy-Schwarz (CR) Inequality
- Consider two $d-$dimensional real number vectors $u,\,v \in \mathbb{R}^{d}$
- Take the inner product of these vectors
	- $u^{T}v=\sum_{i=1}^{d}u_{i}v_{i}$
- This can also be defined as 
	- $u^{T}v=||u||*||v||*\cos(\theta)$
		- $\theta$ is the angle between the vectors
- If this is true, this means
	- $$|u^{T}v| \leq ||u||*||v||$$
- We can normalize the two vectors and derive
	- $-1 \leq u^{T}v \leq 1$

- Intuitively, from the cosine property, if the angle between the two vectors is less than 90, then the inner product of the normalized vectors will be positive
	- If angle is 90, the product will be 0
	- If angle is obtuse, the product is negative
- This means the inner product can measure how closely one vector points in the direction of another vector
  ### Norm Operator Definition
  $$||u||_{p}=\left( \sum_{i=1}^d |u_{i}|^p\right)^{\frac{1}{p}}$$
	- If no p is specified, the convention states p is 2
# Convex Sets
- A set C is convex if
	- $\forall x,\,y \in C$ and $\Theta \in [0,\,1]$,
	- We have $\Theta x+(1-\Theta)y \in C$
	- In other words, if you draw a line between two points in the set, the entirety of the line must be within the set
## Why Is This Useful
- This is important because gradient descent walks between different solutions of the machine learning problem to find the optimal solution
- Every step along the way must also be a valid solution
- So the set of models must be convex
- Additionally, intersections of convex sets are convex
# Projection
- The projection of a point y onto a set C
	- The closest point to y that is within C
- $$P_{c}(y)=arg\min_{x \in C}||x-y||$$
## Why Is This Useful
- Any point will only have one valid projection onto a convex set; just one answer. Why?
	- Imagine a donut set.
	- If the point y is in the center of the donut, the closest point in the donut to y is every single point along the inner circle of the donut
	- In this case, $P_{c}(y)$ has infinite solutions, which is bad
# Convex Functions
- A function $f: \mathbb{R}^{d}\to \mathbb{R}$
	- The domain of the function is a convex set
	- $$\begin{align}
\forall x,\,y \in domf \text{ and } \lambda \in [0,\, 1] \\
f(\lambda x+ (1-\lambda)y) \leq \lambda f(x)+(1-\lambda)f(y)
\end{align}$$
- The second property says that if you draw a line between any two points on the function, the entirety of the line must lie on or above the function
	- These lines are called chords of the function
## Types of functions based on Concavity
- If the chord lies entirely below the function, it is concave
- $y=x^3$ is neither
- $y=x$ is affine, which means both
	- All chords lie on the function
- All norms are convex
- 