Continues [[Numbering Systems]]
Related to [[Boolean Algebra]]
Continued by [[Adders, Subtractors, and the ALU]]
- ### One's Complement
	- Set the first (most significant) to 1 and flip all other bits to represent a negative number
		- Same as flipping every bit
		- $-2_{10} = 1101_2$
		- ![[Signed Integers in Binary 2022-08-31 11.37.22.excalidraw]]
		- Doing operations requires adding 1 at the end
			- This is a wacky property of One's Complement
		- No need for a subtraction circuit/procedure since it is now possible to just add negative numbers instead
- ## Two's Complement
	- Flip every bit to find One's Complement
		- Then pre-add 1 to the result to get Two's Complement
		- $-2_{10} = 1101 + 1 = 1110_2$
		- ![[Signed Integers in Binary 2022-08-31 11.47.11.excalidraw]]


	Binary representation |Unsigned Eq |One's Complement | Two's Complement
	----------------------- | --------------|----------------------|---------------------
	0000|0|0|0
	0001|0|0|0|


Binary Rep | Us Eq | OC | TC 
------------ | ------------ | ---- | ---- 
0000 | 0 | 0 | 0
0001 | 1 | 1 | 1 
0010 | 2 | 2 | 2
0011 | 3 | 3 | 3
0100 | 4 | 4 | 4
0101 | 5 | 5 | 5
0110 | 6 | 6 | 6
0111 | 7 | 7 | 7
1000 | 8 | -7 | -8
1001 | 9 | -6 | -7
1010 | 10 | -5 | -6
1011 | 11 | -4 | -5
1100 | 12 | -3 | -4
1101 | 13 | -2 | -3
1110 | 14 | -1 | -2
1111 | 15 | 0 | -1

- ## Overflow and Carry-Out
	- Sometimes an addition operation will produce overflow
	- This can be detected with the carry chain
		- Overflow = XOR(Last 2 digits of carry chain)
		- ![[Pasted image 20220915183121.png]]
	- Deal with this with sign extension
		- Extend the msb out to the left
		- 1001 (-7) = 11111001
-Systems-1

For class #Logic-Systems-1 
