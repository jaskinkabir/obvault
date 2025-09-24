Explains [[The Discrete Convolutional Sum]]
Continued by [[Calculating Discrete Convolutional Sum]]
- Any LTI System can be characterized as $y[n] = x[n] \circledast h[n]$
	- Where $h[n]=T\{\delta[n]\}$
	- Why?
- Given some input $x[n]$
	- Break up $x[n]$ into a sum of impulses, shifted by $k$, multiplied by weights, given by the value of $x$ at $k$
		- $x[n]=\sum_{k=-\infty}^{\infty}x[k]\delta[n-k]$ 
		- 
	- Apply transformation $T$
		- $y[n]=T\{x[n]\}=T\{\sum_{k=-\infty}^{\infty}x[k]\delta[n-k]\}$
	- By linearity, $x[k]$ can be factored as it does not depend on $n$
		- $T\{kx[n]\}=kT\{x[n]\}$ where $k$ is some constant
		- $\therefore y[n]=\sum_{k=-\infty}^{\infty}x[k]T\{\delta[n-k]\}$
	- By time invariance, the transformation of a delta should result in the same output regardless of time shift
		- 
		- therefore $T\{\delta[n-k]\}$ can be rewritten as a function $h[n-k]$
			- Where $h[n] = T\{\delta[n]\}$
	- Therefore: $$y[n]=\sum_{k=-\infty}^{\infty}x[k]h[n-k]=x[n]\circledast h[n]$$
		- This is convolution
For class #digital-signal-processing 