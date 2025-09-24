Continues [[Fourier Series]]
Continued by [[Fourier Transform]]
- # Method
	- ## Step 1: Identify a suitable period over which to integrate
		- Usually from 0 to T
	- ## Step 2: Determine an equation for the function
		- Usually piecewise
	- ## Step 3: Determine the $\Large\alpha_{n}$ coefficients for n $\neq$ 0
		-  Multiply the function by some harmonic and find the average value
		- $$\large{\alpha_{n} = \frac{1}{T}\int_{0}^{T} x(t)e^{ -jn\omega_{0} t } \, dt }$$
	- ## Step 4: Determine the DC offset
		- $$\large\alpha_n =\frac{1}{T}\large{\alpha_{n} = \frac{1}{T}\int_{0}^{T} x(t) \, dt } $$
	- ## Step 5: Relate to other forms of the series
		- Use image from previous note
		- Sine/Cosine $$f(t) = \frac{a_{0}}{2} +   \sum_{n=1}^{\infty}(a_{n}\cos(n\omega_{0}t)+b_{n}\sin(n\omega_{0}t)) $$
		- Shifted Cosine: $$f(t) = \frac{c_{0}}{2} +   \sum_{n=1}^{\infty}(c_{n}\cos(n\omega_{0}t+\theta_{n}))$$
		- Complex: $$f(t) = \alpha_{0} +   \sum_{n=-\infty}^{\infty}(\alpha_{n}e^{ jn\omega_{0}t })$$
- Example: Square Wave with 50% duty cycle, period T
	- ![[Pasted image 20221026135114.png|200]]
	- Define x(t) as a piecewise function
		- $$x(t) = \left\{ 2: 0<t<\frac{T}{2},\ \  0: \frac{T}{2} < t < T\right\}$$
		- Find Alpha Values
			- ${a_{n} = \frac{1}{T}\int_{0}^{T} x(t)e^{ -jn\omega_{0} t } \, dx }$
			- =$\frac{1}{T}\int _{0}^{\frac{T}{2}}x(t)e^{ -jn\omega_{0} t }\, dx + \frac{1}{T}\int _{\frac{T}{2}}^{T}x(t)e^{ -jn\omega_{0} t }\, dx$
			- =$\frac{1}{T}\int _{0}^{\frac{T}{2}}2e^{ -jn\omega_{0} t }\, dx + 0$
			- $\frac{2}{T}\left( \frac{1}{-jn\omega_{0}}e^{nj\omega_{0}t} \right)$
			- $\frac{2}{-j\omega_{0}nT}\left(e^{nj\omega_{0}(\frac{T}{2})}-1 \right)$
				- $T = \frac{2\pi}{\omega}$
			- $\frac{1}{jn\pi}\left(1-e^{nj\pi}\right)$
			- 
- Example $s(t) = 10 + 50\cos(2\pi 1000t)+20\sin(2\pi 1750t) + 2\sin(2\pi 15000t)$
	- Fundamental frequency: 250Hz
	- The following table can be constructed for the first form
	- 
n|f|$a_{n}$|$b_{n}$|C|$\phi$
-|-|-|-|-|-
0|0|20|0|20|0
1|250|0|0|0|0
2|500|0|0|0|0
3|750|0|0|0|0
4|1000|50|0|50|0
5|1250|0|0|0|0
6|1500|0|2|2|-90
7|1750|0|20|20|-90
- Since Alpha goes from -inf to +inf, the table must be expanded

n|f|$\alpha_{n}$
-|-|-
-7|-1750|$10\angle90$
-6|-1500|$1\angle90$
-5|-1250|0
-4|-1000|$25\angle0$
-3|-750|0
-2|-500|0
-1|-250|0
0|0|$10\angle0$
1|250|0
2|500|0
3|750|0
4|1000|$25\angle 0$
5|1250|0
6|1500|$1\angle-90$
7|1750|$10\angle-90$





For class #Analytical-Foundations 
