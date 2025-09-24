Continued by [[The Continuous Time Fourier Transform (CTFT)]]
- ## Characterizations by Response
	- Through convolution, the system can be entirely characterized by these three functions
	- ### Impulse Response: $\Large \delta\to h$
	- ### Step Response: $\Large u\to s$
	- ### Exponential Response
		- Continuous and Discrete have different forms
			- $\Large e^{st}\to e^{st}H(s)$
				- $H(s)=\int _{{-\infty}}^{\infty}h(\tau)e^{-s\tau} \, d\tau$
					- If $H(s)  < \infty$ 
			- $\Large Z^{n}\to Z^{n}H(Z)$
				- $H(Z)=\sum_{n=-\infty}^\infty h[n]Z^{-n}$
					- If $H(Z)<\infty$
		- Based on the complex transfer function $\large H$ and some complex number $\large Z$
- ## Characterization By Complex Exponential
	- If $x(t)$ can be represented in terms of complex exponentials, $y(t)$ can be found without convolution
		- $x(t)=a_{1}e^{s_{1}t}+a_{2}e^{s_{2}t}$
		- $y(t)=a_{1}e^{s_{1}t}H(s_{1})+a_{2}e^{s_{2}t}H(s_{2})$
	- The following formula can be used to find an LTI system's output
		- $$y(t)=\sum_{-\infty}^{\infty} a_{k}H(s_{k})e^{s_{k}t}\,if\,x(t)=\sum_{-\infty}^\infty a_{k}e^{s_{k}t}$$ 
- ## Causal LTIs
	- Linear constant coefficient DiffEqs
		- Ex: Series RC circuit
	- Linear Const. Coeff. Difference Equation
		- Ex: Investment
			-  $y[n]$: return on investment after the $n^{th}$ month, where 10% is returned each month
			- $x[n]$: net profit
			- $y[n]=1.1 y[n-1]+x[n]$
	- ### Initial Rest
		- A system is causal LTI **IFF it shows initial rest
			- if $x(t)=0$ for $t\leq t_{0}$, $y(t0)=0$
			- $h(t)=0,t\leq0$


$\frac{V_{x}-V_{n}}{4k}+\frac{V_{x}-V_{i}}{R}+\frac{V_{x}-V_{o}}{4k}=0$

$\frac{V_{n}-V_{i}}{2k}+\frac{V_{n}-V_{x}}{4k}=0$


For class #sigsys 