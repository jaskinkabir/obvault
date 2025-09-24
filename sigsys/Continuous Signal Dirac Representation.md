Continues [[The Discrete Convolutional Sum]]
- Approximating $\delta$
	- ![[Pasted image 20230206161453.png]]
- Approximating a signal with deltas
	- $$\hat{x}(t)=\sum_{k\,=-\infty}^{\infty}x(k\Delta)\delta(t-k\Delta)\Delta$$
		- Taking the limit as $\Delta\rightarrow 0$ will result in the Riemann Sum
	- $y(t)=\int _{-\infty}^{\infty}x(\tau)\delta(t-\tau) \, d\tau$
		- If $y(t)$ is LTI, then $h(t)$, the impulse response, can be substituted into the integral
			- $y(t)=\int _{-\infty}^{\infty}x(\tau)h(t-\tau) \, d\tau$
				- The impulse response alone can completely characterize the system
			- $y(t)=x(t)\circledast h(t)$
			- 
- Combining LTI Systems
	- In parallel, add the convolutions
	- In series, convolve the systems
For class #sigsys 