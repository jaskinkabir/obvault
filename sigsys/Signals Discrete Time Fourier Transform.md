Continues [[The Continuous Time Fourier Transform (CTFT)]]
Continued by [[Properties of the DTFT]]
- ## The DTFS
	- $\Large a_{k}=\frac{1}{N}\sum_{n=<N>}^{\infty} x[n]e^{-\frac{jk2\pi}{N}n}$
	- $x[n]=\sum_{k= <N>}a_{k}e^{\frac{jk2\pi}{N}n}$
		- $a_{k}=\frac{1}{N}X(e^{\frac{jk_{2}\pi}{2}})$
- ## The DTFT
	- $$X(e^{j\omega})\doteq \sum_{n=-\infty}^{\infty} x[n]e^{-j\omega n}$$
	- $$x[n]=\frac{1}{2\pi}\int _{<2\pi>}X(e^{j\omega})e^{j\omega n}  \, d\omega$$
	- The DTFT is continuous and periodic with $N=2\pi$
For class #sigsys 