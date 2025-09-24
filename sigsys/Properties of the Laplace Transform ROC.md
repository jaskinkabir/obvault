Continues [[The Laplace Transform in Signal Analysis]]
- ## 1. Linearity
	- Standard linearity definition
	- $ROC\subseteq R_{1}\cap R_{2}$
		- The intersection of ROCs must be included in the final ROC
- ## 2. Time shifting
	- $x(t-t_{0})\iff X(s)e^{-st_{0}}$
		- Same ROC
	- $e^{s_{0}t}x(t)\iff X(s-s_{0})$
		- $ROC = R+Re\{s_{0}\}$
- ## 3. Convolution
	- $x(t)\circledast y(t)\iff X(s)Y(s)$
		- $ROC\subseteq R_{x}\cap R_{y}$
- ## 4. Differentiation
	- $\frac{d}{dt}x(t)\iff sX(s)$
		- $ROC\subseteq R$
	- $-tx(t)\iff \frac{d}{ds}X(s)$
		- $ROC=R$
- ## 5. Integration In Time
	- $\int_{-\infty}^{t} x(\tau) \, d\tau \iff \frac{X(s)}{s}$
		- $ROC\subseteq R\cap \{ Re\{ s \} >0\}$
- ## 6. Initial and Final Value Theorems
	- $x(t=0^+)=\lim_{ s \to \infty }sX(s)$
		- Initial value
	- $\lim_{ t \to \infty }x(t)=\lim_{ s \to 0 }sX(s)$


For class #sigsys 