Continues [[Combinational Logic Representations]]
Using [[Sequential Timing Diagrams]]
Continued by [[Level Or Edge Sensitivity]]
- # Sequential circuits
- A circuit whose behavior is dependent on its previous inputs
	- It must have memory
- It is synchronous
	- It depends on a clock signal to make sure unexpected conditions do not arise due to propogation time
	- Slower than combinational logic
	- More reliable, easier to design
- # S/R Latch
	- Simplest, most basic form of memory
		- ![[Pasted image 20221019121311.png]]
		- Reset input changes output to 0
		- Set input changes output to 1
		- 00 latches output to its current state
		- 11 is illegal/forbidden
- # D-Latch/Flip Flop
	-  To alleviate certain timing-based errors, the **D-Latch** is used
	- ![[Pasted image 20221024113333.png]]
	- The latch will update Q to the value of D if and only if the enable input is set high
	- A periodic clock signal can be fed into the enable input, and the period of the signal can be set equal to the critical path of the combinational logic
	- Removes the possibility of the illegal 11 on the S/R latch
- # Shift Register
	- ![[Pasted image 20221024115156.png]]
		- Triangle input represents clock signal
		- Same as enable input above
		- Important that the latches are alternatively inverted from the clock/enable signal
		- Pictured is a right shift register. Left shift variations also exist
	- As the clock goes from low to high, the second latch holds the output of the first latch, allowing it to store new data
	- Stores a series of bits in parallel
- # Latch Register
	- ![[Pasted image 20221024115359.png]]
	- Can store several bits at the same time
		- Parallel in both input and output
For class #Logic-Systems-1 