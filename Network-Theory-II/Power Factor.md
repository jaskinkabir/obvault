Using [[Summary of Power-Related quantities]]
Continues [[Complex Power]]
- Reactive Loads
	- Inductive Load
		- $Z_{ind} = R + j\omega L$
		- Since both components of the inductance are positive, $\phi_{z}$ must be between 0 and 90, where an angle of 90 corresponds to a purely inductive load, and 0 for a purely resistive one
	- Capacitive Load
		- $Z_{cap} = R-\frac{j}{\omega C}$
		- The imaginary component is negative, so $\phi_{z}$ must be between 0 and -90, where -90 is a purely capacitive load
	- Since the cosine function doesn't care about the sign of $\phi_{z}$, the power factor cannot differentiate between an inductive and a capacitive load.
		- This means that the power factor must be further qualified as either leading or lagging, depending on whether current lags or leads voltage
			- Lagging: I < V
		- ![[Pasted image 20221016201403.png]]
- ## Power Factor Significance
	- The power provided to a circuit is S, but that value S is made up of a real and reactive component. A power company may provide power based on S, but the only power consumed by the circuit is the real component $P_{av}$
		- The Power factor is then the fraction of power supplied to the circuit that is actually consumed
	- Because a power supplier would have to supply more current for a reactive load, even though it would supply the same amount of consumed power as a resistive load, the efficiency of the system can be raised by correcting the power factor to be closer to 1.
- ## Power Factor Compensation
	- Raising the power factor of an inductive load can be achieved using a shunt capacitor
	- ![[Pasted image 20221016202504.png]]
	- The new source current becomes $I_{s}^{'} = I_{L} +I_{C}$
	- ![[Pasted image 20221016204509.png]]
	- The shunt capacitor acts in the opposite direction of the resistor and increases the power factor by reducting $\phi_{z}$
	- $$C = \frac{P_{av}\tan(\theta_{initial})-\tan(\theta_{final})}{\omega*V_{M}^2}$$

For class #Network-Theory-II 