# 1. Show that if a function is convex and concave then it must be affine.
Suppose $f: \mathbb{R}^{d} \to \mathbb{R}$ is convex and concave
1. Because $f$ is convex we have,
	1.  $f(\lambda x+ (1-\lambda)y) \leq \lambda f(x)+(1-\lambda)f(y)$
2. Because $f$ is concave we have,
	1.  $f(\lambda x+ (1-\lambda)y) \geq \lambda f(x)+(1-\lambda)f(y)$
3. Combining 1 and 2 we have,
	1. $f(\lambda x+ (1-\lambda)y) = \lambda f(x)+(1-\lambda)f(y)$
4. Let $g(x)=f(x)-f(0),\,0 \in\mathbb{R}^{d}$
	1. $f(x)=g(x)+f(0)$
5. $g(\lambda x+(1-\lambda)y)=f(\lambda x+(1-\lambda)y)-f(0)$
	2. $=\lambda f(x)+(1-\lambda)f(y)-f(0)$
	3. $=\lambda g(x)-\lambda f(0)+(1-\lambda)g(y)+(\lambda-1)f(0)$
	4. $=\lambda g(x)+(1-\lambda)g(y)$
6. $g(\lambda x)+g((1-\lambda)y)=f(\lambda x)-f(0)+f((1-\lambda)y)-f(0)$

# 2. Show that if a function is convex and upper-bounded then it must be  constant.
1. $f(x) \leq B\ \forall x \in \mathbb{R}^d$
2. $B \geq f(y) \geq f(x) + \nabla f(x)^{T}(y-x) \forall x,\,y \in \mathbb{R}^{d}$
# 4. Given an example of a function that is  
(a) convex but not strictly convex.  
- $f(x)=5x$
(b) strictly convex but not strongly convex;
- $f(x)=\sqrt{ x }$
# 5. Smoothness of cubic functions. Show that the function  $f (x) = x^3$is smooth over $Ω = [0, 1]$, and find a smoothness parameter $L$
- $\|\nabla f(x)-\nabla f(y)\| \leq L\|x-y\|,\,  \forall x,\, y \in [0,\,1]$
- $\| 3x^{2}-3y^{2}\| \leq L\|x-y\|,\,  \forall x,\, y \in [0,\,1]$
- $\frac{\| 3x^{2}-3y^{2}\|}{\|x-y\|} \leq L$