7- ## Dirac Delta Function $\delta$ 
	- Very large near t=0
	- Very small away from t=0
	- Has integral 1
	- Is the derivative of the unit step function
	- Exact shape of function doesn't matter
		- ![[Pasted image 20221014121910.png]]
	- On plots, $\delta$ is shown as a solid arrow
		- ![[Pasted image 20221014121956.png]]
	- $\int_{a}^{b}\delta(t)f(t)\ dt = f(0)$
		- Provided a<0<b, and f is continuous at t=0
		- $\delta$ Acts over a very small interval, over which f(t) $\approx$ f(0)
		- 
	- ## Scaled Impulses
		- Can multiply $\delta(t)$ by a to scale its magnitude
		- Notation is arrow with magnitude next to the arrow
			- ![[Pasted image 20221014123314.png]]
	- ## Shifted Impulses
		- It is possible to shift the point at which the impulse occurs
			- For $\delta(t-T)$, the impulse now happens at t=T
			- The integral property becomes 
				- $\int^{b}_{a}f(t)\delta(t-T) = f(T)$  
	- ## Combining Impulse properties
		- $a\delta(t-T)$
			- Impulse at time T with magnitude a
			- $\int^{b}_{a}af(t)\delta(t-T) = af(T)$

For class #Analytical-Foundations 