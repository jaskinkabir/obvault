Continued by [[Signal Transformation]]
Continued by [[Famous Signals]]
- ## Energy Signal
	- Any signal whose total energy is finite, and whose total power is 0
		- If the total energy is finite, the average power must be 0
	- Calculating energy
		- $$\mathcal{E}_{\infty}=\int _{-\infty}^{\infty}x(t)^2 \, dx $$
	- Discrete time:
		- $$\mathcal{E}_{\infty}=\sum_{n=-\infty}^{\infty}x(n)^2$$
- ## Power signal
	- Any signal whose total energy is infinite, and whose total power is positive, nonzero, and finite
	- Calculating total power
		- $$P_{\infty}=\lim_{ T \to \infty } \frac{1}{T} \int _{\frac{-T}{2}}^{\frac{T}{2}}x(t)^2 \, dx $$
	- Discrete time:
		- $$P_{\infty}=\lim_{ N \to \infty } \frac{1}{N+1}\sum_{{n=-\frac{N}{2}}}^{N/2}x(n)^2 $$
	- A signal cannot be both an energy or a power signal, but some signals are neither.

For class #sigsys
