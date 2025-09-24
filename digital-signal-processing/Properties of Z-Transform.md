Continues [[The Z-Transform]]
- ## Linearity
- ## Shift
	- $x[n-n_{0}] \iff z^{-n_{0}}X(z)$
	- Common
	- $z^{-1}$
- ## Convolution
	- $x[n]\circledast h[n] \iff X(z)H(z)$
		- No circularity
		- ROC is usually intersection of ROCs
- ## Exponential Modulation
	- $(e^{j\omega_{0}})^{n}x[n] \iff X\left( \frac{z}{e^{j\omega_{0}}} \right)$ where
	- $X\left( \frac{z}{e^{j\omega_{0}}}\right)=X(re^{j\omega}e^{-j\omega_{0}})=X(re^{j(\omega-\omega_{0})})$
		- Z-domain version of frequency shift property
- ## BIBO Stability
	- BIBO stable IFF ROC includes unit circle
		- Fourier transform exists if system is BIBO stable
		- Fourier transform exists if ROC includes unit circle
- ## Initial Value
	- $\lim_{ z \to \infty }^{X(z)}{=x[0]}$ for causal $x[n]$
		- Since $\lim_{ z \to \infty }^{X(z)}=\lim_{ z \to \infty }\sum_{n=-\infty}^{\infty}$
- 

For class #digital-signal-processing 