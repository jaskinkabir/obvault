Continues [[Properties of the CTFS]]
Continued by [[Properties of the CTFT]]
- ## The CTFT
	- Consider the function $\phi(t)=e^{jk\omega_{0}t}, k\in\mathbb{Z}$
		- Periodic with $T=\frac{2\pi}{\omega_{0}}$
	- Consider the infinite sum $\sum_{k=-\infty}^{\infty}\phi_{k}(t)$
		- Must also be periodic with $T=\frac{2\pi}{\omega_{0}}$
			- Since $k\in\mathbb{Z}$, the periods must be integer multiples
			- All components of this sum are **harmonically related**
	- Vertical Scaling and Addition
		- For LTI, operations are equivalent in freq dom
	- Time reversal
		- k becomes negative
	- Time scaling
		- New period is $\large\frac{T_{0}}{\alpha}$
- ## Common CTFT Definitions
	- $$CTFT\left( rect\left( \frac{t}{2T_{1}} \right) \right)=2T_{1}sinc\left( \frac{\omega T_{1}}{\pi} \right)$$
		- $\large{ sinc(\theta)=\frac{\sin(\pi \theta)}{\pi\theta}}$
		- If you take the CTFT of a sinc, you get a rect
			- Duality
- $\:\left(\left(4je^{4j}t+\left(4j-1\right)e^{j4}\right)e^{j4t}+1\right)e^{-j4\left(t+1\right)}+e^{j4t}-j4t-j4-1$
- 
$$\Large-\frac{4je^{-j^4+4j}t-j^4t+e^{-j^4\left(t+1\right)}+e^{j^4t}+4j-j^4-2}{\left(t+1\right)^2}$$

For class #sigsys 