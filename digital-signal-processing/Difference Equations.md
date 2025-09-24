Continues [[Explanation of Convolution]]
- ## Definition of Difference Equations
	- Provide another way to represent discrete-time systems
	- Analogous to differential equations used in continuous time systems
	- A given system may be described by several difference equations
		- **Not unique to the system**
	- General form: $$\sum^{N}_{p=0}a_{p}y[n-p]=\sum_{q=0}^Mb_{q}x[n-q]$$
		- Sum of weighted delays of $y[n]$ is equivalent to a different sum of weighted delays of $x[n]$
	- ### Example: Accumulator
		- $y[n]=\sum_{k=-\infty}^{n}x[k]$
			- $h[n]=u[n]$
		- This difference equation is not unique
			- $y[n]=\sum_{-\infty}^{n}x[k]=x[n]+\sum_{-\infty}^{n-1}x[k]$
				- $y[n-1]=\sum_{-\infty}^{n-1}x[k]$
				- $y[n]=x[n]+y[n-1]$
			- $y[n]-y[n-1]=x[n]$
				- ![[Pasted image 20240130102941.png]]
		- Each difference equation results in a different block equation
			- Choose the correct one based on situation
			- ![[Pasted image 20240130102951.png]]
				- Notice that both difference eqns have the same impulse response
				- Easier to understand from block diagram
- ## Solving Difference Equations
	- Solution is analogous to differential equations
	- ### Procedure:
		- 1. Find homogenous (transient) solution $y_{k}[n]$
		- 2. Find particular (forced) solution $y_{p}[n]$
		- 3. Use initial conditions to find solution $y[n]$
			- $y[n]=y_{p}[n] + y_{k}[n]$
	- ### Homogenous Solution
		- Solution for no input, $x[n]=0$
		- Use method of guessing: guess $y[n]=A\alpha^n$
			- $\sum^{N}_{p=0}a_{p}y[n-p]=\sum_{q=0}^Mb_{q}x[n-q]$
				- Guess $y_{k}[n]=A\alpha^{n}$
			- $A\sum_{p=0}^{N}\alpha^{n-p}=0$
		- Solve for N roots of the polynomial
		- Then $y_{}[k]$
	- ### Particular Solution
		- Solution with input $x[n] \neq 0$
		- Guess $y[n]$ has same for as $x[n]$
		- Example: $x[n]=B\beta^{n}$, $y[n]\approx G\gamma^{n}$
			- $\sum^{N}_{p=0}a_{p}y[n-p]=\sum_{q=0}^Mb_{q}x[n-q]$
			- $G\sum^{N}_{p=0}a_{p}\gamma^{n-p}=B\sum_{q=0}^Mb_{q}\beta^{n-q}$
			- Solve for G and $\gamma$
			- Then $y_{p}[n]=G\gamma^n$
	- ### Complete Solution
		- $y[n]=y_{k[n]}+y_{p}[n]$
		- Use initial conditions to solve for remaining constants
- ## Recursive DiffEq. Solution and IIR Systems
	- It is possible to find the impulse response from a DiffEq using the recursive method
	- Example 
	- ![[Pasted image 20240130105425.png]]
		- Solve for $y[0]$ using initial rest and initial conditions
		- Increment
		for following values of n
		- Find patt
		ite general form of $h[n]$
		- This is a
		inite impulse response
			- Infin
			ation
	- 
	
For class #digital-signal-processing 
cess