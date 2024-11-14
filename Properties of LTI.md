Continues [[Calculating Discrete Convolutional Sum]]
- ![[Pasted image 20240123104532.png]]
	- Parallel systems add impulse responses
	- Series convolve impulse responses
- ## BIBO Stability
	- An LTI is BIBO Stable if $$\sum_{k=-\infty}^{\infty}|h[k]| < \infty$$
	- A bounded impulse response results in a bounded output
- ## Examples
	- ![[Pasted image 20240123105130.png]]
		- $h[n]$?
			- Replace $x[n]$ with $\delta[n]$
				- $h[n] = \frac{\delta[n] + \delta[n-1] + \delta[n-2]}{3}$
		- Is this LTI?
			- Linearity?
				- Doubling the input results in a doubled output
			- Time Invariance?
				- a
- a
	- ![[Pasted image 20240123105714.png]]
	- 


For class #digital-signal-processing