Continues [[The Laplace Transform in Signal Analysis]]
- ## Inverse LT
	- $$x(t)=\frac{1}{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty} X(s)e^{st} \, ds $$
		- Called contour integration
	- We will focus on rational $X(s)$
		- $$\mathscr{L}[e^{-at}u(t)]\iff\frac{1}{s+1},\,Re\{s\}>-a$$
		- $$\mathscr{L}[-e^{-at}u(t)]\iff \frac{1}{s+a},\,Re\{s\}<-a$$
			- These relationships will allow for very simple ILTs for rational $X(s)$
	- EXP:
		- $X(s)=\frac{1}{(s+1)(s+2)}$
			- If ROC is $\sigma>-1$?
				- $x(t)$ is right sided by prop 4
				- 

For class #sigsys 