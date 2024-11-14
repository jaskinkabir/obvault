Continues [[Properties of Systems]]
- ## Definition
	- $y[n]=\sum_{k=-\infty}^{\infty}x[k]h[n-k]$
		- Essentially a linear combination of the two functions
		- Notation $x[n]\circledast h[n]$ 
	- The impulse response only works for LTI systems
- ## Graphical Computation Approach
	- Draw signals in terms of K
		- ![[Pasted image 20230201163815.png]]
	- Determine the values of $n$ such that there will be an overlap and a nonzero CS
		- Since $x[k]$ has no values before 0 or after 1, $h[n-k]$ will only overlap if $0\leq n\leq3$
	- Multiply and add for each n within this interval
		- $y[0]=\frac{1}{2}$
		- $y[1]=\frac{5}{2}$
		- $y[2]=\frac{5}{2}$
		- $y[3]=2$
	- Draw the resulting signal
		- ![[Pasted image 20230201164816.png]]
- ## Analytical Approach
	- ![[Pasted image 20230201171230.png]]
	- ![[Pasted image 20230201171210.png]]
- 
- ## Properties of Convolution
	- You will always end with a longer sequence; more nonzero values of n
	- Connecting LTI systems:
		- Distibutivity
			- $x\circledast (h_{1}+h_{2})=x\circledast h_{1}+x\circledast h_{2}$
			- $(x\circledast h_{1})\circledast h_{2}=x\circledast h_{1} \circledast h_{2}$
		- Identity
			- $x(t)\circledast \delta(t)=x(t)$
			- 
For class #sigsys 


If D1 is an open circuit, and D2 is closed, then the circuit becomes a straight line from the 10V voltage source to the -10V source. The current through this line can be found as $I=\frac{10V-(-10V)}{10k\Omega +10k\Omega}=1.333mA$.
$V_{0}=10-1.3333mA * 5k\Omega=3.333V$

$2t(u(t)-u(t-1))+2(2-t)(u(t-1)-u(t-2))$