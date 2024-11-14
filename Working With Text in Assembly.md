Continues [[LEGv8 Addressing Modes]]
# ASCII and LDURB and STURB
- Because ASCII characters take up only a byte, LEGv8 provides the `LDURB` and `STURB` instructions to
	- Load a single byte from memory into the rightmost 8 bits of a register
	- Store the rightmost 8 bits of a register into a byte of memory
		- Sign extend the rest
		- STURB overwrites the remaining bits of the register

# String Representation
- Strings are variable length arrays. This problem can be solved in 1 of 3 ways
	- Reserve the first position of a string to hold the length
	- An accompanying variable contains the length
	- The last position of a string is indicated by a terminal character
		- This is the technique used by C
		- In C, this character is 0x0, or `\0`
# Unicode and LDURH and STURH
- The Unicode format uses 16 bits per character
- LEGv8 provides LDURH and STURH to load and store 16 bit **half-words**
- 

For class  #comporg 