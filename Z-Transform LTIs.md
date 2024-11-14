Continues [[The Z-Transform ROC]]
- ## Time Shifting
	- $$x[n-n_{0}] \iff X(z)z^{-n_{0}}$$
- ## Convolution
	- $$x_{1}[n] \circledast x_{2}[n] \iff X_{1}(z)X_{2}(z)$$
		- $R_{1}\cap R_{2}\subseteq ROC$
- ## Causality
	- ROC must be that of a right sided signal that includes $Z=\infty$
		- Exterior of circle bounded by outermost pole
		- $|\lim_{ z \to \infty } H(z)| < \infty$
	- For rational $H(z)$, the degree of the numerator must be less than or equal to that of the denominator
- ## Stability
	- Causality iff the ROC contains $|Z|=1$
		- Unit circle
	- Same condition for existence of DTFT

For class #sigsys 