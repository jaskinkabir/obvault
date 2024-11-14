Supplements [[Transformers]]
![[Pasted image 20221021124413.png]]

# Steps
1. Find voltage ratios
	1. Dot rule: Dotted terminals are both plus, so ratio is positive
	2. From ratio listed on problem: $$\frac{V_{1}}{V_{2}}=+\frac{1}{2}$$
		1. $$V_{2} = 2V_{1}$$
2. FInd Power Ratios
	1. $P_{1} + P_{2}= 0$
	2. $I_{1}V_{1}-I_{2}V_{2}=0$
		1. From passive sign convention, current enters negative of V2
3. FInd current ratios
	1. $I_{1}V_{1}=I_{2}V_{2}$
	2. $$I_{2} = \frac{I_{1}}{2}$$
4. KVL
	1. For first loop:
		1. $12 = (2-j2)I_{1}+V_{1}$
	2. For second loop:
		1. $V_{2}=(4-j2)I_{2}$
	3. Substitute ratios into second equation and create system of equations
		1. $2V_{1}=(2-j)I_{1}$
		2. $V_{1}=(1-.5j)I_{1}$
	4. Substitute this expression for I1 in first eq
		1. $12 = (2-j2)I_{1} + (1-.5j)I_{1}$
	5. Solve for I1
		1. $I_{1}=\frac{12}{(3-j 2.5)}$
		2. $$I_{1}=3.07\angle 39.81\degree$$
	6. Solve for V1
		1. $V_{1} = (1-j0.5)I_{1}$
		2. $$V_{1}=3.44 \angle 13.24 \degree$$
![[Pasted image 20221021130001.png]]
# Solve
1. Find Voltage Ratio
	1. Dotted terminals are positive
	2. $$\frac{V_{1}}{V_{2}}=+2$$
2. Find Current Ratio
	1. $P_{1}+P_{2}=0$
	2. $I_{1}V_{1}-I_{2}V_{2}=0$
		1. From passive sign convention
	3. $\frac{I_{1}}{I_{2}}=\frac{V_{2}}{V_{1}}$
	4. $I_{1}V_{1}=I_{2}V_{2}$
	5. $\frac{I_{1}}{I_{2}}=\frac{V_{2}}{V_{1}}$
	6. $$\frac{I_{1}}{I_{2}}=+\frac{1}{2}$$
3. Source Transform left voltage source
	1. ![[Pasted image 20221021130933.png]]
	2. 


For class #Network-Theory-II 