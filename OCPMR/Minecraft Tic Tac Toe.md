- ## Memory Cells
	- S/R Latches
		- Set is tied to the turn flip flop
		- Reset to the reset button
	- Each of the 9 cells will be stored with 2 bits
		- On or off bit
		- X or O bit
	- Two repeater memory cells stacked vertically
	- Layout
		- In a line seems like the best option
	- Requirements:
		- Clear functionality
			- Input is fed through a comparator that is locked by the reset line
			- The clear input should be on either side to connect all 9 together
		- The write input should be able to be connected to the turn flip-flop
			- Maybe connect all write inputs together to create 1 18 bit memory module
		- Protect the memory from overwriting
			- If tie detector or any of the win detectors are activated, do not allow writing.
		- The write signal must have a NAND gate with the following inputs:
			- On/Off bit
			- Tie detection
			- Win detection
			- NOT write input
		- Falling edge detector on the write signal for valid space detection
		- Must be able to output to both screen and win/tie detection
- ## Win detection
	- Each of the 8 ways to get 3 in a row will be connected to their own 3-way and gate
		- And gate must also make sure all 3 inputs have their On/Off bit set
		- Standard Horizontal design
		- Either a vertical and diagonal design, or one design for both
- ## Tie detection
	- 9-way AND gate taking all the On/Off bits as inputs
- ## Valid Space detection:
	- Attach falling edge detector to each space's write line
	- Connect these falling edge detector outputs together
	- After any user button press:
		- If any of the FEDs send a pulse, toggle the turn flip-flop
- ## Reset game
	- Activate clear line of each memory cell
- ## User Interface
	- ### Button Input Panel
		- 9 different output lines going to each memory cell?
			- The memory cell's XO input will be tied to the turn line
			- The button input will activate the write input line
			- Very complicated
- adder
	- 3 bits to 7
		- 7 8 9 10
	- 



i|i|i|i|o|o|o|o
-|-|-|-|-|-|-|-
0|0|0|0||||
0|0|0|1||||
0|0|1|0||||
0|0|1|1||||
0|1|0|0||||
0|1|0|1||||
0|1|1|0||||
0|1|1|1||||
1|0|0|0||||
1|0|0|1||||
1|0|1|0||||
1|0|1|1||||
1|1|0|0||||
1|1|0|1||||
1|1|1|0||||
1|1|1|1||||

For topic #OCPMR