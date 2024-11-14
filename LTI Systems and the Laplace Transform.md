orContinues [[The Laplace Transform in Signal Analysis]] 
- ## Causality: 
	- The ROC of $H(s)$ for a causal system is right-sided
		- A causal signal has a right-sided $h(t)$
			- The reverse is only true iff $H(s)$ is rational
	- A right sided, rational $H(s)$ belongs to a causal signal
- ## Stability
	- A system is stable iff the ROC of its $H(s)$ contains the $j\omega$ axis
		- This means the line $\sigma=0$ is a valid value for $s$
		- The Laplace Transform when $\sigma=0$ is the Fourier Transform
			- Only stable functions can have a Fourier Transform, and so the system must be stable.
	- A causal, stable system with rational $H(s)$ must have all poles to the left of the $j\omega$ axis
- ## Systems Described by Some DiffEQ
	- $\sum^{N}_{k=0} a_{k} \frac{d^ky(t)}{dt^{k}}=\sum^{M}_{k=0} b_{k} \frac{d^kx(t)}{dt^{k}}=$
		- Take LT of both sides
	- $$H(s)=\frac{\sum^{M}_{k=0} a_{k}s^k}{\sum^{N}_{k=0} a_{k}s^k}$$
		- Rational $H(s)$
	- Exp: For series RLC circuit?
		- $x(t)=y(t)+RC \frac{dy(t)}{dt} + LC \frac{d^2y(t)}{dt^2}$
		- $H(s)=\frac{1}{LCs^{2}+RCs + 1}$
		- R, L, and C are positive, so all poles must lie to the left of the $j\omega$ axis
			- A system defined by some series RLC circuit must be causal and stable
	- 

$(μ_nC_{ox} \frac{W}{L})[(V_{GS}-V_{th})V_{DS} - \frac{V_{DS}^2}{2}](1+\lambda V_{DS})$


For class #sigsys 