- $$x(t)=\frac{4sinc^{2}(4(t-5))}{\pi}=\frac{4}{\pi}*\left(\frac{\sin(4(t-5))}{4(t-5)}\right)^2$$
- 
- 1. Write down a formula to express the square of a sinusoid in terms of a double angle argument. 
	- $$\sin^{2}(\theta)=\frac{1-\cos(2\theta)}{2}$$
- 2. What is the meaning of differential linearity?
	- When considering a system whose output $y$ is some function of an input $x$, the system is said to possess differential linearity if the input and output show the following relationship:
		- $\Delta Y=K\Delta X$, where $K$ is some constant
	- In other words, the change in the input must be constantly proportional to the change in the output
- 3. Consider the two conditions for linearity for a system S defined by y = S(x). 
	- Conditions:
		- $Ay(x)=S(ax)$: Homogeneity
		- $S(x_{1})+S(x_{2})=S(x_{1}+x_{2})$: Additivity
	- How would you apply these formulas in testing systems for linearity in this Lab? How many replicas of the system are needed for the additivity test? 
		- Using two replicas of the system, homogeneity can be tested as follows.
			-  Connect some input function to the input of a multiplier to be multiplied by some constant. Then connect the output of this multiplier to the system and record the output. Next, connect the unaltered input function to a replica of the system, then feed the output of the system into a multiplier with the same constant second input. If these two outputs are the same, the system is homogenous
		- Using three replicas of the system, additivity can be tested. 
			- Connect two inputs to an adder, then connect the adder to the system and record its output. Then connect each unaltered input to its own replica of the system, and connect these outputs to an adder. If the two outputs are the same, the system is additive. 


$\int_{0}^{t} x(t)\, dt=\sum_{n=0}^{t/\Delta t}x(n\Delta t)\Delta t$

$x(n\Delta t)=V_{p}$
$\sum_{n=0}^{t/\Delta t}x(n\Delta t)\Delta t=V_{p}\sum_{n=0}^\frac{t}{\Delta t}\Delta t=V_{p}*t$
$V_{out}=\frac{V_{pp}}{\frac{T}{2}} \int _{0}^t x(\tau)\,d\tau$

$y(t)=25210 \int _{0}^{t} x(\tau) \, d\tau$
Integration rate: $\frac{\Delta V}{\Delta t}  * \frac{1}{V_{in}}$
Output: $\frac{V_{out_{p}}}{V_{in_{p}}* \frac{1}{2f}}$

