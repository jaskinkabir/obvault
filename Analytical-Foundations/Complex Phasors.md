Continues [[Complex Numbers]]
Using [[Sinusoidal Function Format]]
- ## The Complex Exponentional Vector:
	- For the function $Ae^{j\theta} = A^{j\omega t}$
		- As t increases, the vector formed on the real/complex plane rotates about the origin
		- ![[Complex Phasors 2022-09-02 13.43.10.excalidraw]]
		- As the vector rotates, the real and imaginary components of the vector oscillate sinusoidally
			- Track the real part, it approaches 0, then moves away from 0 in the negative direction, then comes back
			- Explains the Euler's formula allowing a complex exponential number to be decomposed into 2 sinusoidal functions
- ## Phasors:
	- If y = $A\cos(\omega t + \phi)$
		- y = $Ae^{j\phi}Ae^{j\omega t}$
			- Static Phasor: $Ae^{j\phi}$
				- Made up of constants
			- Dynamic Phasor: $Ae^{j\omega t}$
				- Varies with t
	- The sum of the 2 components of the decomposition will be entirely real
		- Complex conjugates
	- ![[Complex Phasors 2022-09-02 13.54.25.excalidraw]]
	- ### Sinusoidal functions can be thought of as the combination of 2 vectors (on the real/complex plane) that move over time
		- One vector rotates forward (CCW): $Ae^{j\omega t }$
		- The other rotates backward (CW): $Ae^{-j\omega t}$
		- The angles are opposites of each other, and so only the real part remains
	- For 4cos(1000t + 30):
		- Real{$4e^{j30}e^{j1000t}$}
			- Static Phasor:
				- $4e^{j30}$
			- Dynamic Phasor
				- $4e^{j1000t}$
	- ## Sinusoidal functions can be broken down in the following ways
		- $$\large{A\sin(\omega t+\phi) = \frac{A}{j_{2}}(e^{j\omega t}-e^{-j\omega t})}$$
		- $$\large{A\cos(\omega t+\phi) = \frac{1}{2}(e^{j\omega t+\phi}+e^{ -j\omega t -\phi})}$$

	For class #Analytical-Foundations
	Continued by [[Euler's Identity and Calculus]]