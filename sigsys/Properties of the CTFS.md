Continues [[The Continuous Time Fourier Transform (CTFT)]]
- ## Properties
	- ### Linearity
		- $$\alpha x_{1}(t)+\beta x_{2}(t)\iff\alpha a_{1_{k}}+\beta a_{2_{k}}$$
	- ### Time Shifting
		- $$x(t-t_{0})\iff a_{k}e^{-jk\omega_{0}t_{0}}$$
	- ### Time Reversal
		- $$x(-t)\iff a_{-k}$$
	- ### Time Scaling
		- $$x(\alpha t)\iff a_{k}$$
	- ### Differentiation
		- $$\frac{dx(t)}{dt}\iff jk\omega_{0} a_{k}$$
	- ### Integration
		- $$\int x(\tau) \, d\tau \iff \frac{a_{k}}{jk\omega_{0}} + \pi a_{0} $$
	- ### Multiplication
		- $$x(t)y(t)\iff \sum_{m=-\infty}^\infty a_{m}b_{k-m}$$
	- ### Periodic Convolution
		- $$\int _{<T>}x(\tau)y(t-\tau) \, d\tau \iff Ta_{k}b_{k} $$
	- ### Conjugation
		- $$x^{*}\iff a_{-k}^{*}*$$
		- The real operator of $X(j\omega)$ is even, and the imaginary is odd
		- The Fourier Transform is an even function, meaning 
	- ### Even and Oddness
		- A real and even signal will have a purely real and even transform
		- Real and odd signal will be purely imaginary and odd
		- $Ev\{x(t)\}=Re\{X(jw)\}$
		- $Odd\{x(t)\}=Im\{X(jw)\}$
	- ## Parseval's Theorem
		- $$\frac{1}{T}\int _{<T>}|x(t)|^{2} \, dt=\sum_{k=-\infty}^\infty |a_{k}|^{2}$$
			- Energy per unit period
			- The square of each CTFS coefficient corresponds to the energy of one frequency component of the overall signal
		- The CTFS is discrete and aperiodic
		- The DTFS is discrete and periodic 
			- Perodic with the same period as the original signal


For class #sigsys 