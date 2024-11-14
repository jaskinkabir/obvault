Continues [[AC Power]]
Continued by [[Power Factor]]
- A phasor quantity defined in terms of V and I such that the real component of S is equal to the real average power absorbed by the load impedance Z
	- $$S = \frac{1}{2}VI^*$$
		- Where $I^*$ is the complex conjugate of the phasor current
			- $S = V_{rms}I_{rms}cos(\theta_{v}-\theta_{i}) + jS = V_{rms}I_{rms}sin(\theta_{v}-\theta_{i})$
				- The first term is the real average power
				- The second term is the reactive power
				- $$S = P_{av} + jQ$$
					- The real power is dissipated by the reactive elements, the reactive power is stored and then released by the reactive components in the load
						- Q is specifically the peak amount of power exchanged

- ### Complex Power for a load
		- Impedance of a load has a real, resistive component R and an imaginary, reactive component X such that
			- $Z = R + jX$
			- If the reactive component is positive, the load is inductive; capacitive if negative
		- If $V = ZI$, the expression $S = \frac{1}{2}VI^*$ becomes
			- $S = \frac{1}{2}ZII^*$ 
			- $$S = I^{2}_{rms}(R+jX)$$
				- $$S = \frac{1}{2}|I|^2(R+jX)$$
				- $$P_{av} = I^{2}_{rms}R$$
				- $$Q =I^{2}_{rms}X$$
	- The Magnitude of S is called the **Apparent Power**
	- Taking the cosine of the angle of the impedance gives the **Power Factor**
		- Defined as the ratio of average power to S
		- The fraction of apparent power that is actually lost to the load
		- $pf = \frac{P_{av}}{S} = \cos(\theta_{v}-\theta_{i}) = \cos(\theta_{Z})$
	- We can then talk about the power in terms of the two angles with the voltage as a reference poin
		- If $\theta_{I}>\theta_{V}$, Current is leading, angle is negative
		- ![[Pasted image 20221014140549.png]])
		- 
	- The Complex Power can be used to form a **Power Triangle**
		- ![[Pasted image 20221012123833.png]]
		- This means trigonometry can be used to solve complex power problems
- $\left( \frac{1}{3300}+\frac{1}{5600}+\frac{1}{2200}\right)^{-1}$
For class #Network-Theory-II 