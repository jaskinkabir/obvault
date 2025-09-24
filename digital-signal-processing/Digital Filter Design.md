Continued by [[Impulse Invariance IIR Design]]
Continued by [[Bilinear Transformation IIR Design]]
Continued by [[Pre-Warped Bilinear Transform]]
Continued by [[FIR Design Windowing Method]]
- ## Overview
	- Digital Filter Design involves selecting some parameters for the filter, and then finding some $H(e^{j\omega})$ that satisfies these requirements
		- This becomes the desired $H(e^{j\omega})$
		- This is a continuous time filter with an s response in the Laplace domain
	- Consider![[Pasted image 20240403220358.png]]
		- $T$ is chosen such that no aliasing occurs
		- The effective frequency response is as follows
			- ![[Pasted image 20240403220420.png]]
			- $H_{eff}(\Omega)=H(e^{j\Omega T})$
			- Since the signal is sampled at with period T, any component with a period lower than T will not be considered by this system
		- In relating the continuous time (CTFT) frequency $\omega$ to the DTFT $\Omega$ with $\omega=T\Omega$, we can find that
			- $H(e^{j\omega})=H_{eff}\left( j \frac{\omega}{T} \right), \, |\omega|<\pi$
			- This only holds over one period, as the DTFT is periodic over $2\pi$ rad/sample
		- 
	- These methods start with some analog continuous time filter design
	- Defined by impulse response $h_{c}(t)$ or by a continuous time Laplace-transform $H_{c}(s)$
	- This is then converted to a digital filter with $h_{c}[n] \iff H_{c}(Z)$
- ## Why Bother?
	- The desired frequencies can be passed or rejected by simply zeroing the corresponding components of an FFT and reconstructing the signal. For example:
		- ![[Pasted image 20240416173138.png]]
		- This will remove the high frequency components just fine
	- However, the effect of this must be examined in the time domain. Simply zeroing out certain frequencies is in effect, multiplication in the frequency domain by a box function, or some linear combination of shifted unit step functions
	- In the time domain, this means convolving the input function with a linear combination of shifted sinc functions.
	- Sinc functions have large ripples, where some of these ripples extend the full length of the time domain. This will distort the filtered output signal
For class #digital-signal-processing