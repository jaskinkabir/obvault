Continues [[The Continuous Time Fourier Transform (CTFT)]]
- ## Linearity
- ## Time Shifting
	- $$x(t-t_{0})\iff X(j\omega)e^{-j\omega t_{0}}$$
- ## Conjugation
	- $$x^{*}(t)\iff X^{*}(-j\omega)$$
- ## Differentiation and Integration
	- $$\frac{dx(t)}{dt} \iff j\omega X(j\omega)$$
	- $$\int _{-\infty}^{t}\, dt \iff \frac{X(j\omega)}{j\omega}+\pi X(0)\delta(\omega)$$
- ## Time Scaling
	- $$x(\alpha t)\iff \frac{1}{|\alpha|}X\left( \frac{j\omega}{\alpha} \right), \alpha \neq_{0}$$
	- $$x(-t)\iff X(-j\omega)$$
	- $$x(\alpha t+\beta)\iff \frac{1}{|\alpha|}X()$$
- ## Duality
	- If $x(t) \iff X(\omega)$, then $x(t)\iff 2\pi X(-\omega)$
	- 
- ## Parseval's
	- $$\int _{-\infty}^{\infty}|x(t)|^2\,dt =\frac{1}{2\pi}\int _{-\infty}^{\infty}|x(\omega)|^2\,d\omega$$
- ## Convolution
	- $x(t)\circledast y(t)=X(j\omega)Y(j\omega)$
	- $X(j\omega)\circledast Y(j\omega)=x(t)y(t)$
- $x(t) \iff X(j\omega)$

$CTFT(X(j\omega)) = x(t)$

For class #sigsys 