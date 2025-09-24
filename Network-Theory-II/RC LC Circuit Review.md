# First Order Circuits with DC Sources
- ## RC Circuits
	- $V(t) = V_{f} + (V_i - V_f)e^{\frac{-t}{\tau}}$
		- Time constant $\tau$ = RC
		- $V(t) = V_{Transient} + V_{Steady State}$
		- $V_{Transient} = Ae^{\frac{-t}{\tau}}$
		- Find A with initial voltage, set t=0
- Steps
	- 1. Find initial voltage 
	- 2. Find steady state
		- When switch has been in final position for a long time
	- 3. Write diffeq $\frac{dx}{dt} + \frac{1}{\tau} = C$
		- C is some constant
		- X can be voltage or current
	- 4. Solve for X
- ## RL Circuits
	- $V_{L}= L \frac{di}{dt}$
	- $\tau = L/R$
	- $i(t) = i_{f}+ (i_{i}- i_{f})^\frac{-t}{\tau}$
EXP:
![[RC LC Circuit Review 2022-08-31 12.58.20.excalidraw]]

# EXP 2:
![[RC LC Circuit Review 2022-09-02 12.56.49.excalidraw]]

For class #Network-Theory-II 