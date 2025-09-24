Continues [[Strong Convexity and Smoothness]]
Expands [[2D Linear Regression and the Loss Function]]
# Gradient Descent
- The objective is to identify a sequence of points ${x_{t}}$ that converge to the optimal solution
- A direction $d$ is called a descent direction at x if $$f(\overrightarrow{x} + t\overrightarrow{d}) < f(\overrightarrow{x}),\, \forall t<\overline{t}$$
	- Where $\overline{t}$ is some arbitrary maximum step size. $\overline{t}$ must be small
## Claim: For continuously differentiable functions, any direction $d: \nabla f(x)^{T}d<0$ is a descent direction of $f$ at $x$
## Proof
-  $\nabla f(x)^{T}d < 0 \implies \exists \overline{t} \text{ s.t }\nabla f(x+td)^{T}d < 0\ \forall t<\overline{t}$
	- Because the function is continuously differentiable
- $f(\overrightarrow{x} + t\overrightarrow{d})=f(\overrightarrow{x})+\nabla f(\overrightarrow{x}+t\gamma \overrightarrow{d})^{T}t\overrightarrow{d}$
	- By Taylor A
	- The second term is less than 0 from the first point
- Thus $f(\overrightarrow{x} + t\overrightarrow{d}) < f(x),\, \forall t<\overline{t}$
## Steepest Descent
- Among all unit vectors, which one points in the direction of the steepest descent down the objective function?
- In other words, what is $d^{*}$ for $$\min_{d} \nabla f(x)^{T}d\ \text{s.t. } \|d\|=1$$
- From Cauchy-Schwartz, $d^{*} = - \frac{\nabla f(x)}{\|\nabla f(x)\|}$
	- $u^{T}v=\|u\|*\|v\|*\cos(\theta)$
	- In this case, $\|v\|$ is always 1, and the value is minimized when $\theta=180 \degree$
	- As such, $\nabla f(x)^{T}d^{*}=-\|\nabla f(x)\|$
	- The only vector $d^{*}$ that satisfies this equation is $- \frac{\nabla f(x)}{\|\nabla f(x)\|}$
	- This is the unit vector pointing in the direction of $-\nabla f(x)$
# Gradient Descent Algorithm
- $$x_{t+1} = x_{t} - \gamma_{t}\nabla f(x_{t})$$
	- Where $\gamma$ is the step size / learning rate (can vary with t)
- We are guaranteed to achieve lower values of $f$ for $\gamma_{t}$ small enough, unless $\nabla f(x_{t})=0$

# Analysis of Gradient Descent for Any Function
- let $g_{t} := \nabla f(x_{t})$ for convenience
- By GD: $g_{t}=\frac{1}{\gamma}(x_{t}-x_{t+1})$
- $g_{t}^{T}(x_{t}-x^{*})=\frac{1}{\gamma}(x_{t}-x_{t+1})^{T}(x_{t}-x^{*})$
- $=\frac{1}{2\gamma} \left(\|x_{t}-x_{t+1}\|^{2}+\|x_{t}-x^{*}\|^{2}- \|x^{*}-x_{t+1}\|^{2}\right)$
	- Because $2v^{T}w = \|v\|^{2}+ \|w\|^{2}- \|v-w\|^{2}$
- $$=\frac{\gamma}{2}\|g_{t}\|^{2}+\frac{2}{\gamma}(\|x_{t}-x^{*}\|^{2}- \|x_{t+1}-x^{*}\|^{2})$$
	- This is called G.D1
- Summing GD1 over $t=0,\,\dots ,T-1$, the last two terms of gd1 have a telescoping effect
	- This refers to the fact that between $t=0$ and $t=T$, the intermediary values will cancel each other out
	- ![[Pasted image 20250130204655.png|250]]
- $$\sum_{t=0}^{T-1}g_{t}^{T}(x_{t}-x^{*})=\frac{\gamma}{2}\sum_{t=0}^{T-1}\|g_{t}\|^{2}+\frac{1}{2\gamma}(\|x_{0}-x^{*}\|^{2}-\|x_{T}-x^{*}\|^{2})$$
	- This sum is called GD2
- We will use equations GD1 and GD2 to prove convergence results for various function classes
For class #optimization-ml