1. What is a peripheral?
	1. A peripheral is a hardware component connected to a microcontroller through its peripheral control registers and exists to perform specific tasks, such as creating input output interfaces.
2. Describe the process to set a high voltage to Port 1 Pin 3. (using the msp430.h header for simplicity)
	1. Set the 3rd bit of the P1DIR register, at address 0x0204, to 1.
		1. `P1DIR |= BIT3`
	2. Set the 3rd bit of the P1OUT register, at address 0x0202, to 1
		1. `P1OUT |= BIT3`
3. Describe the process to set Port 2 Pin 5 as an input with an internal pull-up resistor enabled.
	1. Set the 5th bit of the P2DIR register to 0
		1. `P2DIR &= ~BIT5`
	2. Set the 5th bit of the P2REN register to 1
		1. `P2REN |= BIT5`
	3. Set the 5th bit of the P2OUT register to 1
		1. `P2OUT |= BIT5`
4. How would I make a bit mask that isolates bit 5 in a register?
	1. `unsigned char BIT5 = 1 << 5`
