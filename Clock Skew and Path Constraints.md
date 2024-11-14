Continues [[Transmission Gates and Tristate Logic]] 
Continued by [[Delay Estimation]]
Continued by [[Clock Distribution]]
- ## Path Constraints
	- In a pipelined system, there are two paths through the system that are considered for STA
		- $D$: Longest Path
		- $d$: Shortest Path
			- These variables represent the time required to traverse these paths
	- Input data, called $V_{n}$ will take either path $D$ or $d$ to become output data $X(V_{n})$, which is the output of the combinational function $X$ which we denote stage 1
		- When $X(V_{n})$ is available, latch $y$ should be ready to latch the output so that it can be fed into stage 2
- ## Skew
	- The clock from the perspective of one stage of the pipeline may not be the exact same signal as that of another stage. The difference between these clocks is called skew, denoted by $\Delta$
		- If this skew causes the second stage to latch before the output of stage 1 is ready, stage 2 will latch junk
	- We can denote the time of the rising edge of stage 1's clock as $t_{1}$ ad stage 2's clock $t_{2}$
		- $\Delta=t_{2}-t_{1}$
		- If $t_{2}>t_{1}, \Delta>0$, positive skew
			- Clock 2 is late
		- Negative skew: $\Delta<0$
			- Clock 2 is early
- ## Longest Path Constraint
	- With the considerations of just $D$, The minimum clock period $T_{cp}$ need only be greater than $D$
		- $T_{cp}\geq D$
		- This isn't realistic
	- Each flip flop has its own delay to read and store input
		- $T_{cp}\geq D + t_{ff}$
	- Flip-flops also have set-up time, which is the time before the clock signal where the input must be stable
		- $T_{cp} \geq D+t_{ff}+t_{su}$
	- ### Negative Skew Error
		- ![[Pasted image 20240219192738.png]]
		- If data $V_{0}$ is passing through stage 1 across path $D$, but the latch at the input of stage 2 will trigger before $X(V_{0})$ is ready.
			- It will latch junk data $X(V_{-1})$
		- We cannot allow the flip flops to trigger before data has fully passed through the stages
			- $$T_{cp} + \Delta \geq D+t_{ff}+t_{su}$$
				- This is the full Longest Path Constraint Formula
- ## Shortest Path Constraint
	- ### Positive Skew Error
		- ![[Pasted image 20240219191705.png]]
		- If data $V_{0}$ takes the path $D$ from stage 1 to stage 2, then after time $D+t_{ff} + t_{su}$, stage 2 should be ready to latch the stage 1 output $X(V_{0})$
		- However, there is positive skew, and latch Y won't be able to see the rising clock until $D+\Delta$
		- If data $V_{1}$ takes path $d$ to get to the output, and $d<\Delta$, then latch y will see the output $X(V_{1})$ and never see $X(V_{0})$
		- This means that 
			- $\Delta \leq d$
		- But if $\Delta$ must be adjusted such that latch Y cannot see $X(V_{1})$ before it latches $X(V_{0})$, the skew must account for the flip flop delay and the hold time
			- The flip flop delay means the flip flop cannot react to the $X(V_{0}) \rightarrow X(V_{1})$  transition immediately. so it gives some breathing room to $\Delta$
				- $\Delta \leq d + t_{ff}$
				- Really, $t_{ff}$ is part of $d$ so it's impossible to talk about $d$ without considering $t_{ff}$
			- But the flip flop needs time after the clock edge for the input data to remain stable, called hold time. (after clock edge)
				- $\Delta \leq d + t_{ff} - t_{ho}$
- ## Final Equations
	- ### Longest Path Constraint
		- $T_{cp} + \Delta \geq D + t_{su} + t_{ff}$
		- The **Big Steal** is using a positive skew to allow for a smaller $T_{cp}$ and therefore more throughput
	- ### Shortest Path Constraint
		- $\Delta \leq d + t_{ff} - t_{ho}$

For class #vlsi 

$y(t)=\sum_{n=0}^{t/dt}x(n)=y(t)=x(n)*t*dt$