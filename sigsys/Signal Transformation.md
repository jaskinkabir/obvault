Continues [[Energy and Power Signals]]
Continues [[Signal Manipulation]]
Continued by [[Signal Parity and Decomposition]]
- ## Dependent Variable Signal Transformation:
	- Differentiation: 
		- If an input signal in the form of a current is given to a series RL circuit, the voltage across the inductor will be equal to
			- $$L \frac{di}{dt}$$
		- Integration:
			- Passing an input current signal to a series RC circuit allows the voltage across the capacitor to be read as the integrated input signal
				- $V_{c}=\frac{1}{C}\int_{-\infty}^{t} I(\tau) \, d\tau$
- ## Independent Variable Transformation
	- ### Time Scaling:
		- $y(t) = x(\alpha t)$
			- The time axis gets divided by $\alpha$
	- ### Time Reversal
		- $y(t)=x(-t)$
			- The signal is flipped across the Y-axis
	- ### Time Shifting
		- $y(x+\beta)$
			- If $\beta$ is positive, this is an advance; shift to the left
			- If $\beta$ is negative, this is a delay; shift to the right
	- ### Order of Operations:
		- Distribute
		-  Shift
		- Reverse
		-  Scale
			- 
For class #sigsys 