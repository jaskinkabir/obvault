Continues [[Properties of Convexity]]
Continued by [[Gradient Descent]]

# Lipschitz Continuity
- A function is **Lipschitz Continuous** with parameter $L \geq 0$ if $$\|f(x)-f(y)\| \leq L\|x-y\|\ \forall x,\, y \in domf$$
	- The distance between $f(x)$ and $f(y)$ is at most some constant $L$ times the distance between $x$ and $y$
	- You can define some cone with slope $L$ that the entire function lies within
	- This definition can be rewritten as $$\frac{\|f(x)-f((y)\|}{\|x-y\|} \leq L$$
		- The expression on the left is the magnitude of the function's average slope
		- Thus, Lipschitz continuity enforces that the function does not grow too quickly, it has a maximum average slope $L$
- For example, $f(x)=x^{2}$ is not Lipschitz continuous because you cannot define a maximum average slope, $f'(x)$ is always increasing.
	- Proof:
	-  $|x^{2}-y^{2}| \leq L|x-y|$
	- $|(x+y)(x-y)| \leq L|x-y|$
	- $|x+y\|x-y| \leq L|x-y|$
	- $|x+y| \leq L$
	- $\nexists L>0\ \text{s.t.} |x+y| \leq L$
- 

# Strictly Convex Functions
- A function is strictly convex if it is convex and $f(\lambda x+(1-\lambda)y) < f(\lambda x) + (1-\lambda)f(y)$
- Strictly convex functions have unique minima
# Strongly Convex Functions
- A function is **m-Strongly Convex** if $\exists\ m>0$ such that
	- $$f(y) \geq f(x) + \nabla f(x)^{T}(y-x) + \frac{m}{2}\|x-y\|^{2}$$
	- This enforces that the function grows faster than some quadratic function
	- A strictly convex function is "not too flat"
- An equivalent definition is that $f$ is m-strongly convex if $f(x) - \frac{m}{2}\|x\|^{2}$ is convex
	- This says that even if you subtract a quadratic, the function is still convex
# Taylor's Theorem
- The theorem says that there exists some point $x+\gamma p$ in between $x$ and $x+p$ such that the gradient at that inner point $\nabla f(x+\gamma p)$ is equal to the average slope of the line between $f(x)$ and $f(x+p)$
- This holds for all real-valued functions 
- This theorem is numerically defined in two ways
## Mean Value Version (Taylor A)
- $\exists \gamma \in (0,\, 1) \text{ s.t}$ $$f(x+p) = f(x) + \nabla f(x+\gamma p)^{T}p$$
	- To better accentuate the fact that this relates to the average slope, it can be rewritten as:$$\frac{f(x+p)-f(x)}{p}=\|\nabla f(x+\gamma p)\|$$
## Integral Version (Taylor B)
- $$f(x+p)=f(x) + \int _{0}^{1} \nabla f(x+\gamma p)^{T}p \, d\gamma $$
	- Proof that Taylor B is Taylor A
		- Assume $f : \mathbb{R} \to \mathbb{R}$
		- $\int_{o}^{1}\nabla f(x+\gamma p)^{T}p\ d\gamma$
		- =$\frac{1}{p}f(x+\gamma p)\ |_{0}^{1}$
		- $=\frac{1}{p}(f(x+p)-f(x))$
		- $=\frac{f(x+p)-f(x)}{p}$
		- From Taylor A: $\frac{f(x+p)-f(x)}{p}=\nabla f(x+\gamma p)^{T}p$
		- Therefore $\int_{0}^{1}\nabla f(x+\gamma p)^{T}p\ d\gamma = \nabla f(x+\gamma p)^{T}p$
	- Intuitively, the proof is this: The integral over all gradients of f from $x \to p$ is the average slope between $x$ and $p$
# L-Smoothness
- A function $f: \mathbb{R}^{d}\to \mathbb{R}$ is **L-Smooth** if $\nabla f$ is Lipschitz continuous with parameter $L$
- $$\|\nabla f(x)-\nabla f(y)\| \leq L\|x-y\|,\,  \forall x,\, y \in domf$$
- Lipschitz functions have bounded gradients.
	- This means the hessian of a smooth function has eigenvalues equal to l
- An equivalent definition of smoothness:
- $$f(y) \leq f(x) + \nabla f(x)^{T}(y-x) + \frac{L}{2}\|x-y\|^{2} $$
	- The final term of the sum enforces that $f$ grows slower than a quadratic
	- Notice that this is the opposite inequality of the definition of strong convexity. A function can only be strongly convex and L-smooth if $f(y) = f(x) + \nabla f(x)^{T}(y-x) + \frac{L}{2}\|x-y\|^{2}$
		- If the function grows as fast as the tangent line plus a quadratic at all points
- In other words, smooth functions are not 'too curved'
	- ![[Pasted image 20250130183057.png]]
## Proof of equivalent definition
- $$f(y) \leq f(x) + \nabla f(x)^{T}(y-x) + \frac{L}{2}\|x-y\|^{2} $$
- $$f(y) - f(x) - \nabla f(x)^{T}(y-x) - \frac{L}{2} \|x-y\|^{2} \leq 0$$
	- $p=y-x$
- $$ \int_{0}^{1}\nabla f(x+\gamma (y-x))^{T}(y-x)\ d\gamma- \int_{0}^{1}\nabla f(x)^{T}(y-x)\ d\gamma$$
	- Because we proved that the integral of a gradient times a line from the point of the gradient is the same as the gradient times that line
- $$=\int_{0}^{1}(\nabla f(x+\gamma(y-x))-\nabla f(x))^{T}(y-x)\ d\gamma$$
- By Cauchy Schwartz: $$\leq \|\ \int_{0}^{1}\nabla f(x+\gamma(y-x))-\nabla f(x)\, \| * \|y-x\|\ d\gamma$$
	- By smoothness: $\|\nabla f(x+\gamma y-\gamma x)-\nabla f(x)\| \leq L\|\gamma y-\gamma x\|$
- $$\leq \int_{0}^{1} L\gamma \|y-x\| * \|y-x\|\ d\gamma $$
- $$\leq L \int_{0}^{1}\gamma d\gamma \|y-x\|^{2}$$
- $$= \frac{L}{2}\|y-x\|^{2}$$

For class #optimization-ml