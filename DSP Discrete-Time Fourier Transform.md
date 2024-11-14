Continued by [[Properties of the DTFT]]
Continued by [[The DFT]]
- ## The DTFT
	- Consider an input sequence $x[n]=e^{j\omega n}$
	- Then the output from an LTI would be
		- $y[n]=\sum_{k=-\infty}^{\infty}h[k]e^{j\omega(n-k)}$
		- $y[n]=e^{j\omega n}\left( \sum_{k=-\infty}^{\infty} h[k]e^{-j\omega k} \right))$
		- $$H(\Omega)=\sum_{k=-\infty}^{\infty} h[k]e^{-j\omega k}$$
	- Therefore, 
		- $$x[n]=\frac{1}{2\pi}\int _{-\pi}^{\pi}X(e^{j\omega})e^{j\omega n} \, d\omega \iff \sum_{n=-\infty}^{\infty}x[n]e^{-j\omega n} = X(e^{j\omega})$$
			- Any interval for this integral of length $2\pi$ can be used, as the DTFT is periodic with $T=2\pi$
		- 
- $$X_{S}(\Omega)=\int_{-\infty}^{\infty} x_{s}(t)e^{-j\Omega t} \, dt $$
- $$\int_{-\infty}^{\infty} \left( \sum_{-\infty}^{\infty}x(nT_{s})\delta(t-nT_{s}) \right) \, dx $$
	- $X_{s}(\Omega)=\sum_{n=-\infty}^{\infty}x(nT_{s})e^{-j\Omega nT_{s}}$
- $$X(\omega)=\sum_{-\infty}^{\infty}x[n]e^{-j\omega n}$$
- $$x[n]=\frac{1}{2\pi}\int_{-\infty}^{\infty} X(\omega)e^{j\omega n} \, d\omega $$
- Comments on DTFT
	- DTFT Is continuous in $\omega$
	- Periodic with period $2\pi$
	- Since $\omega=\Omega T_{s}=\frac{2\pi f}{f_{s}}$, then $\omega=2\pi$ at $f=f_{s}$
	- Result of DTFT Is complex
	- Closely related to $X_{s}(\Omega)$
- 
Related to [[Sampling and The Nyquist-Shannon Theorem]]


For class #digital-signal-processing 

