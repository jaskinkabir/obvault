Continues [[Signal Manipulation]]
Continued by [[Assembling The Fourier Series]]
Using [[Sinusoidal Function Format]]
- ## Definition of the Fourier Series
	- #### Any periodic waveform can be expressed as a linear combination of periodic basis functions
		- They are **Harmonically Related** which means their frequencies are integer multiples of each other
	- Approach 2
		- $C\cos(\alpha + \beta)=C\cos(\alpha)\cos(\beta)-\sin(\alpha)\sin(\beta)$
			- $A\cos(\sigma t+\phi)=a\cos(\omega t)-b\sin(\omega t)$
				- $\alpha = C\cos(\phi)$
				- $\beta = -C\sin(\phi)$
		- EXP:
			- $x(t) = 2\cos(2\pi 1000t+45\degree)$
			- $x(t) = 2\cos(2\pi 1000t)\cos(45)-2\sin(2\pi 1000t)\sin(45)$
	- Approach 3
		- $$x(t)=C\cos(\omega t+\phi) = \frac{ce^{ j\phi_{n} }}{2}e^{ j\omega t } + \frac{ce^{ j\phi_{n} }}{2}e^{ -j\omega t }$$
		- $$x(t)=C\cos(\omega t+\phi) = \alpha e^{ j\omega t }+\alpha e^{ -j\omega t }$$
	- Approach 4
		-  $x(t)=C\cos(\omega t+\phi) = Real\{ce^{ j\omega t }e^{\phi}\}$
- ## Core Definitions
	- ### Fundamental Frequency/Period
		- The smallest amount of time over which the function repreats
		- For a series of sinusoids with Frequencies $f=\{f_{0},f_{1},f_{2},f_{3}\}$$
			- Fundamental frequency $f_{0} = GCD(f)$
			- Fundamental period $T_{0}=\frac{1}{f_{0}}$
	- ### Harmonic Number n
		- The nth harmonic function has frequency $nf_{0}$
	- ### DC or Average Value
		- Function with frequency 0
- ## 3 Formats for Fourier Series
	- ### Sine Cosine Approach
		- $F(t) = \frac{a_{0}}{2} + \sum[a_{n}\cos(n\omega_{0}t)+b_{n}\sin(n\omega_{0}t)]$
	- ### Shifted Cosine Approach
		- $F(t) = \frac{c_{0}}{2} +\sum[C_{n}\cos(n\omega t+\phi_{n})]$
	- ### Complex Phasor Approach
		- $\large{F(t) = \sum{a_{n}e^{ jn\omega_{0}t }}}$
			- Starts at n=$-\infty$
- ![[Pasted image 20221020141055.png]]
- # Fourier Series For Square Wave
	- ![[Pasted image 20221024174332.png]]
	- 

For class #Analytical-Foundations 