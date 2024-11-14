Continues [[Assembling The Fourier Series]]
- In the frequency domain, x(t) has the following frequency spectrum
	- $$x(\omega)=\large \sum_{n=-\infty}^{+\infty} \alpha_{n}\delta(\omega-n\omega_{0})$$
	- For $x(t) = 3\cos(2\pi t-30\degree)$
		- $$x(\omega)=\alpha_{-1}\delta(w+2\pi)+\alpha_{1}(\omega-2\pi )$$
		- $$x(\omega)=\frac{3}{2}e^{ j30\degree}\delta(w+2\pi)+\frac{3}{2}e^{ -j30\degree}(\omega-2\pi )$$
	- This means the Fourier Transform $x(\omega)$ is a complex function of a real variable
		- It is a complex number of the form
		- $$x(\omega)=|x(\omega)|e^{\angle x(\omega)}$$
	- Therefore, its visualization requires a graph of its magnitude and its angle

For class #Analytical-Foundations 