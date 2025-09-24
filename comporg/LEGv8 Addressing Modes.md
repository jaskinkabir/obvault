Continues [[LEGv8 Procedure Calling]]
Continued by [[From C to Machine]]
# Wide Immediate Operands
- Sometimes an immediate constant is wider than the 12 bits allotted in immediate instructions.
- For these cases, LEGv8 provides

# Addressing Mode
- An **Addressing Mode** is a way to address data, **Where to find data**
	- "The method of specifying and accessing an operand in an assembly statement"
1. Immediate addressing
	1. Data is in the instruction
2. Register addressing
	1. Address is in the register
3. Base addressing
	1. Address is in the register plus a constant offset in the instruction
	2. Used by D type instructions
4. PC-relative addressing
	1. The address is the sum of the PC and a constant in the instruction
	2. Used by B and CB type instructions
# Register Transfer Notation
- $x_{2} \gets x_{1}$: Contents of x1 transferred to x2
- $x_{1} \gets [x_{2}]$: Access memory location pointed to by x2 and store contents in x1
- 

For class #comporg