
Continued by [[High Level State Machine]]
- ## Compares two bus inputs 
	- Not to be confused with analog comparator like from Minecraft
- ## Equality Comparator
	- Checks if both inputs are equal
	- XNOR each bit of the inputs
		- Feed each XNOR into AND
- ## Greater/Less Than
	- If the leftmost bit follows the condition ab', then a>b
		- Go down the line from left to right, if any of them are true, then a>b
		- If any are false, b>a
		- If a=b, ignore this bit
	- Can ripple the previous output of the 1 bit full comparator of the previous bit to the next one
		- ![[Pasted image 20221128115034.png]]
- ## Full Comparator
	- Pulls 1 of its 3 output signals high depending on if A is greater, less than, or equal to B
	- ![[Pasted image 20221128115251.png]]



For class #Logic-Systems-1 