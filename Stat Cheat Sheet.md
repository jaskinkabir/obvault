- # 1 Var Stats
	- $$E(x)=\int_{-\infty}^{\infty} xP(x) \, dx $$
	- $$E(x^2)=\int_{-\infty}^{\infty} x^{2}P(x) \, dx $$
	- $$V(x)=\sigma^2_{x}=E(x^2)-E(x)^2$$
	- ### Gamma Distribution
		- $$P(x)=u(x)\frac{\beta^{\alpha}}{\Gamma(\alpha)}x^{\alpha-1}e^{-\beta x}$$
			- Shape parameter $\alpha$ and rate parameter $\beta$
			- $E(x)=\frac{\alpha}{\beta}$, $\sigma^2_{x}=\frac{\alpha}{\beta^2}$
			- $\Gamma(\alpha)=\int_{0}^{\infty} t^{\alpha-1}e^{-t} \, dt$
	- ## Exponential Distribution
		- $$P(x)=u(x)\lambda e^{-\lambda x}$$
		- $E(x)=\frac{1}{\lambda}$, $V(x)=\frac{1}{\lambda^{2}}$
		- CDF: $P(x\leq X)=1-e^{\lambda X}$
	- ## Poisson Distribution
		- $$P(x)=\frac{u(x)e^{-\lambda}}{x!}\lambda^{x}$$
		- $E(X)=V(X)=\lambda$
	- ## Std Norm (Gauss) Distribution
		- $Z=\frac{X-\mu}{\sigma}$
- # 2-Var Stats
	- ## Joint Probability
		- If $P(x,y)=f(x,y)$
			- $P(x)=\int_{-\infty}^{\infty} f(x,y) \, dy$ ,$P(y)=\int_{-\infty}^{\infty} f(x,y) \, dx$
			- $Cov(x,y)=E(xy)-E(x)E(y)$
				- $E(xy)=\int_{-\infty}^{\infty} \int_{-\infty}^{\infty} xyf(x,y) \, dx \, dy$
			- $Corr(x,y)=\frac{Cov(x,y)}{\sigma_{x}\sigma_{y}}$
			- For independent x and y, $P(x,y)=P(x)P(y)$
	- ## Conditional Probability
		- $P(x|y)=\frac{P(x\land y)}{P(y)}$
			- For independent x and y, $P(x)=P(x|y)$
		- $P(x,y=Y)=\frac{f(x,Y)}{\int_{-\infty}^{\infty} f(X,Y) \, dX}$
		- 