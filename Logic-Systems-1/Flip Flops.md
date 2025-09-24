Continues [[Sequential Circuit Memory]]
- # Enabled Flip Flop
	- ![[Pasted image 20221026115735.png|250]]
	- A multiplexer is used to switch the data input between the previous latched output and a new input from the dataline
	- **Even if the clock signal changes, the output Q doesn't change unless the enable line is high**
- # Resettable Flip Flop
	- ![[Pasted image 20221026120449.png]]
		- This design is synchronous.
	- Has one more input that will clear the output, setting it to 0
	- Has two types
		- **Asynchronous**: Clears whenever the reset input is high. Level based
		- **Synchronous**: Clears on the edge of the clock signal based on the reset input. Edge based
	- The synchronous version can be achieved by ANDing the data input with the inverted reset signal
		- When reset is high, the data input will become 0 and reset the latch.

For class #Logic-Systems-1 