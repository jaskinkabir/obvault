Continues [[Periodic Signals]]
- ## Exponentials:
	- ### Real Exponentials
		- In the form $x(t)=e^{\sigma t}$
		- #### Exponential Modulation
			- Modulating the amplitude of a sinusoid based on an exponential function
				- $x(t) = e^{\sigma t}\cos(\omega t+\phi )$
			- A damped/decaying sinusoid is formed when $\sigma<0$
	- ### Complex Exponential
		- In the form $Ce^{j\gamma}=Ae^{j\theta}+Be^{j\theta}$ 
		- When plugging in a complex number for $\sigma$ in the previous format:
			- $e^{\sigma+j\omega}e^{j\theta }$
		- Can simplify to the following form
			- $e^{\sigma t}[\,\cos(\omega t+\phi)+j\sin(\omega t+\phi)\,]$
			- Traces the following trajectory on the complex plane
				- ![[Pasted image 20230125161659.png|250]]
	- ### Discrete time complex exponential
		- $x[n]=C(\alpha)^{n}$
			- $C$ and $\alpha$ can be complex
		- #### Modulating $\Large \alpha$:
			- Growth Function
				- ![[Pasted image 20230125161953.png]]
			- Decay Function
				- ![[Pasted image 20230125162056.png]]
			- Oscillating Function
				- ![[Pasted image 20230125162210.png]]
			- Oscillating decay
				- ![[Pasted image 20230125162307.png]]
- ## Discrete Time Complex Sinusoids
	- $X[n]=e^{j\omega n}$
		- If this is periodic: $x[n+N]=x[n]$, where $N$ is the period
		- If we want the starting point to be 1, $e^{j\omega N}$
			- This means $N$ is a multiple of $2\pi$
		- #### Finding N
			- Find some number that, when multiplied with $\omega_{0}$, will result in a multiple of $2\pi$
			- $$N=\frac{m{2}\pi}{\omega_{0}}$$
				- $m$ is the smallest integer such that $N$ can be found as an integer
				- If no such integer $N$ can be found, the signal is NOT periodic
- 

For class #sigsys 