Continues [[AC Filters]]
Continued by [[The Decibel Scale]]
- ## Circuit Scaling
	- When designing a filter, it is convenient to design a prototype model, where the units are large and easy to work with, and then scale the prototype into a practical circuit that has different component values but the same frequency response.
	- Each component in the prototype is given an unprimed symbol, and its scaled equivalent is given the prime signal.
		- $Z_{R}' = K_{m}Z_{R}$
- ## Magnitude Scaling
	- Changes values of the circuit elements, but keeps the frequency response the same
	- If all impedances are multiplied by some factor $K_{m}$, the frequency response will remain unchanged
		- $R'=K_{m}R'$
		- $L'=K_{m}L$
		- $C'=\frac{C}{K_{m}}$
		- $\omega'=\omega$
- ## Frequency Scaling
	- Shifts the frequency response along the x-axis, but keeps circuit component values the same
	- Creates relation $\omega'=K_{f}\omega$
	- In order to keep impedances the same, the values must be inversely scaled
		- $R'=\frac{R}{K_{f}}$
		- $\large L'=\frac{L}{K_{f}}$
		- $\large C'=\frac{C}{K_{f}}$
		- $\omega'=K_{f}\omega$
- ## Combined Scaling
	- $R'=K_{m}R'$
	- $L'=\frac{K_{m}}{K_{f}}L$
	- $C'=\frac{1}{K_{m}K_{f}}C$
	- $\omega'=K_{f}\omega$
	- 

For class #NetworK-Theory-II 