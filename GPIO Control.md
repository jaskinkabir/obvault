- ## Peripherals
	- A hardware component included in a microcontroller's architecture to perform some task.
	- Are controlled by control registers
- ## GPIO Registers
	- ### Direction register
		- Determines if a pin is input or output
		- For Shue board, 0:input 1:output
	- ### Output Register
		- A 1 or a 0 on the bit corresponding to some pin will set that pin's output voltage to a high or low level.
	- ### Input Register
		- Read only register that shows the digital value read by a pin
	- ### Pull-up/Pull-down Resistor Enable Register
		- Can control if a resistor should be connected to a pin
		- **Whether the pin is connected through pull-up or pull-down is determined through the output register**
			- 1: pull-up 0:pull-down