# Second Order Discretization
Continues [[Discrete Time and Numerical Solutions]]
- For the second order system ${\frac{d^{2}t}{dt^{2}}} + b\frac{dy}{dt} + cy(t) = x(t)$
	- Let $y_{1} = y(t)$
	- Let $y_{2} = \frac{dy}{dt}$
	- $\frac{d^{2}t}{dt^{2}} = \frac{d}{dt}y_{2}= x(t) - b\frac{dy}{dt} - cy(t)$
	- $y_{1}(n+1) = y_{1}(n) + \Delta t y_{2}(n)$
	- $y_{2}(n+1) = y_{2}(n) + \Delta t(x(n) - by_{2}(n) - cy_{1}(n))$ 
- ## Approach for Discretizing DiffEQ
	- ### Step 1: Find Discretized Eqns
	- ### Step 2: Find Time Step
		- Examine steady state and transient response time features
			- Consider decaying exponentials
				- Make sure $5\tau >> \Delta t$
			- Consider sinusoids
			- Makse sure $T >> \Delta t$ 
- EXP: $y'' + 4y' + 100y = 1$
	- STEP 1: FIND DISCRETE EQNS
		- $y_{1}(n+1) = y_{1}(n) + \Delta t y_{2}(n)$
		- $y_{2}(n+1) = y_{2}(n) + \Delta t(1 - 4y_{2}(n) - 100y_{1}(n))$ 
	- STEP 2: FIND DT
		- Steady State:
			- $y_{p} = 1$
				- Has no interesting time features
				- No effect on dt
		- Transient:
			- The transient response is underdamped
			- $y_{c} = 2|C|e^{\frac{-t}{\tau}}cos(\omega_{d}+\angle C)$
				- Use roots function: Real(s1) = -2
					- tau = 0.5
					- $\Delta t << 5\tau$
					- $\Delta t << 2.5$
					- $\Delta t = 0.025 sec$
			- $T_{d}= \frac{2\pi}{\omega_{d}} = 0.6413$
				- $\Delta t << 0.6414$
				- $\Delta t < 0.006414$

For class #Analytical-Foundations 