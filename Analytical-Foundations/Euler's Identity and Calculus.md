Continues [[Complex Phasors]]
- $$\large{e^{x}cos(x) = Re\{e^{x+jx}\}} $$
-  $$\large{e^{x}sin(x) = Im\{e^{x+jx}\}}$$
- You can use Euler's identity to convert expressions involving trig functions into simpler ones involving complex numbers
	- This makes calculus and other operations easier
- EXAMPLE: $\int{e^{3x}\cos{5x}dx}$
	- $cos(5x) = Re\{e^{j5x}\}$
	- $\int{e^{3x}\cos{5x}dx} = Re\{\int{e^{3x} * e^{j5x}}\}$
	- $\large{\int{e^{3x}\cos{5x}dx} = Re\{\int{e^{x(3+5j)}dx}\}}$
		- $\int{e^{(3+5j)x}} = \frac{1}{3+5j}e^{(3+5j)x} + C$
		- $ae^{3x}e^{5jx}$
			- $a = \frac{1}{3+5j}$
			- $a = (3+5j)^{-1}$
			- $a = \frac{1}{sqrt(34)}e^{-59.036^{\degree}}$
	- Taking the real part
		- $\frac{1}{3+5j} = |a|e^{\angle a} = \frac{1}{sqrt(34)}\angle -59^{\degree}$
		- $e^{(3+5j)x} = e^{3x}e^{5jx}$
		- $|a|e^{3x}e^{j(5x+\angle a)}$
			- $\frac{1}{sqrt(34)}e^{-59.036^{\degree}}e^{3x}e^{5jx}$
		- TAKE THE REAL
			- ${=\frac{e^{3x}}{\sqrt{34}}(cos(5x-54)+jsin(5x-54))}$
		- $$\LARGE{\int{e^{3x}\cos{5x}dx}=\frac{e^{3x}}{\sqrt{34}}cos(5x-54)} + C$$
		- 
- EXP $sin(3x)cos(4x)$
	- $= (\frac{1}{2j}e^{3jx}- \frac{1}{2j}e^{-3jx})(\frac{1}{2}e^{4x}+ \frac{1}{2}e^{-4x})$
		- = $\frac{1}{4j}e^{j7x}- \frac{1}{4j}e^{-j7x} -\frac{1}{4j}e^{jx} + \frac{1}{4j}e^{-jx}$
	- $$=\large{\frac{1}{2}sin(7x) - \frac{1}{2}sin(x)}$$
	- This is much easier to integrate/differentiate

For class #Analytical-Foundations