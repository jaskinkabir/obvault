Continues [[Digital Filter Design]]
- ## Zero-Order Hold
	- An ADC will typically sample signals with a Zero-Order Hold
	- This means holding the sampled value by multiplying it by a zero-order polynomial, in most cases 1.
	- If we consider applying a zero order hold to the function $v_{k}[n]$ to convert it to $v(t)$, we can think of this as the sum of infinitely many sums of 1 positive and one negative step function such that:
		- $v_{n}(t)=v[n]u[t-nT]-u[t-(n+1)T]$
		- This only works for one held pulse of the signal
	- We can formulate an infinite sum equation to find the time domain function from $v(t)=\sum_{n=-\infty}^{\infty}v[n](u[t-nT]-u[t-(n+1)T])$
	- Taking the Laplace transform of this function is as follows $$L[v(t)]=V(s)=\left(\frac{1-e^{-Ts}}{s}\right)\sum_{n=-\infty}^{\infty}v[n]e^{-nTs}$$
	- If we want to apply some system with transfer function $G(s)$ to this input function, we can find the following equation $$Y(s)=\frac{1-e^{-sT}}{s}G(s)\sum_{n=-\infty}^{\infty}v[n]e^{-sTn}$$
	- If we apply the substitution $z=e^{sT},$ $$Y(s)=\frac{1-z^{-1}}{s}G(s)\sum_{n=-\infty}^{\infty}v[n]z^{-k}$$
		- The infinite sum term is simply the z-transform of the input signal
	- By taking the Z-Transform of the transfer function a new transfer function in terms of the Zero-Order Hold can be found:
		- $$\frac{Y(z)}{V(z)}=(1-z^{-1})Z\left\{ \frac{G(s)}{s} \right\}|_{t=nT}$$

For class #digital-signal-processing 