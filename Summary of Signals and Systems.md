- # Time Domain Analysis
	- ## Power and Energy
		- ### Power
			- $P_{\infty}=\lim_{ T \to \infty } \frac{1}{T}\int _{-\frac{T}{2}}^ {\frac{T}{2}} |x(t)|^2\, dt$
		- ### Energy
			- $E_{\infty}=\int _{-\infty}^ {\infty} |x(t)|^2\, dt$
		- If $0<P_{\infty}<\infty$, Power signal and $E_{\infty}=\infty$
		- If $E_{\infty}<\infty$, energy signal and $P_{\infty}=0$
	- ## Time operations
		- **D**on't **S**hit in **R**ed **S**ocks
			- Distribute, Shift, Reverse, Scale
	- ## Even and Oddness
		- $\large x_{e}(t)=\frac{x(t)+x(-t)}{2}$
		- $\large x_{o}(t)=\frac{x(t)-x(-t)}{2}$
	- ## Sinusoids
		- Euler shit
	- ## Convolution
		- Can characterize a system without differential equations and complex Fourier analysis
		- $x(t) \circledast y(t) = \int_{-\infty}^{\infty} x(\tau)y(t-\tau) \, d\tau$
			- Pick narrower signal to shift and reverse
			- Graph both functions
			- Find ROC
			- Integrate 
	- ## LTI System Transfer Function
		- ### Causality: $h(t) = 0, \,t<0$
		- ### Memory: $h(t)=k\delta(t)$
		- ### Stability: $\int_{-\infty}^{\infty} |h(t)| \, dt<\infty$
		- ### Eigenfunction: $e^{st} \implies [h(t)] \implies e^{st}H(s)$
			- Transfer function $H(s)$ is the Laplace transform of $h(t)$
- # Frequency Domain Analysis 
	- ## Continuous Time
		- ### Fourier Series
			- $x(t)$ is T periodic and continuous
			- $a_{k}$ is aperiodic and discrete
			- $\large a_{k}=\frac{1}{T} \int _{<T>}x(t)e^{-jk\frac{2\pi}{T}t} \, dt$
			- $\large x(t) = \sum_{k=-\infty}^{\infty}a_{k}e^{jk \frac{2\pi}{T}t}$
			- No duality
		- ### Fourier Transform
			- $x(t)$ is aperiodic and continuous
			- $X(j\omega)$ is aperiodic and continuous
			- $\large X(j\omega) = \int_{-\infty}^{\infty} x(t)e^{-j\omega t} \, dt$ 
			- $\large x(t) = \frac{1}{2\pi}\int_{-\infty}^{\infty} X(j\omega)e^{j\omega t} \, d\omega$
	- ## Discrete Time
		- ### Fourier Series
			- $x[n]$ is N periodic and discrete
			- $a_{k}$ is periodic and discrete
		- ### Fourier Transform
			- $x[n]$ is aperiodic and discrete
			- $X(j\omega)$ is $2\pi$ periodic and continuous
	- ## Laplace Transform
		- Used for continuous systems
		- ROC of stripes
		- S-sided signal will have S-sided ROC
		- Two sided signal will have double-sided ROC
		- $X(s)=\int_{-\infty}^{\infty} x(t)e^{-st} \, dt$
	- ## Z-Transform
		- $X(z) = \sum_{n=-\infty}^{\infty}x[n]z^{-n}$
	- ## DFT/FFT
		- Learn this stuff
		- 

For class #sigsys inf