- ## Contour Integral
	- $x[n]=\frac{1}{2\pi j}\oint X(z)z^{n-1} \, dz$
	- Lookup Table
		- Don't forget ROC
	- Power Series Expansion (long division)
- ## Z-Transform Vs DFT
	- Z-Transform is sampled Laplace
	- $X[k]=X(z)|_{z=e^{j\frac{2\pi}{N}k}}$
- ## Partial Fraction Expansion
	- Consider $X(z)=\frac{N(z)}{D(z)}$
		- If degree(N(z))<degree(D(z))
	- Set $N(z)=zQ(z)$
		- $X(z)=\frac{zQ(z)}{D(z)}$
		- $Q(z)=\frac{N(z)}{z}$
	- Factor denominator
		- $X(z)=\frac{zQ(z)}{(z-p_{1})(z-p_{2})\dots (z-p_{i})}=\sum_{\alpha=1}^{i} \frac{c_{\alpha}}{z-p_{\alpha}}$
	- $X(z)=z\sum_{\alpha=1}^{i} \frac{\frac{(z-p_{\alpha})Q(z)}{D(z)}|_{z=p_{\alpha}}}{z-p_{\alpha}}$
	- $(z-p_{k}) \frac{Q(z)}{D(z)}=\frac{(z-p_{k})Q(z)}{(z-p_{1})(z-p_{2})\dots(z-p_{i})}=( z-p_{k})\sum_{\alpha=1}^{i} \frac{c_{a}}{z-p\alpha}$
	- At $z=p_{k}$, solve for $c_{k}$
		- $(z-p_{k}) \frac{Q(z)}{D(z)}|_{z=p_{k}}=c_{k}$
	- $X(z)=\frac{N(z)}{D(z)}=z \frac{Q(z)}{D(z)}=\sum_{\alpha=1}^{i} \frac{zc_{a}}{z-p_{\alpha}}$
	- $x[n]=\sum_{\alpha=1}^{i}c_{\alpha}(p_{\alpha})^{n}u[n]$
	-


$\int_{-\infty}^{\infty} x(\tau)h(t-\tau) \, d\tau$
$h[n]=\frac{1}{4}(\delta[n]+\delta[n-2])+\frac{1}{2}\delta[n-1]$

For class #sigsys