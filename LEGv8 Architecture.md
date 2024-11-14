Continues [[8 Great Ideas in Computer Architecture]]
Continued by [[LEGv8 Branch Instructions]]
# Register Operands
- In legV8, there are only 32 registers
	- This is because numerous registers would require a longer clock period for the CPU to be able to traverse a longer register file
	- A longer register file would also require a longer address space in the instruction
- LEGv8 has a 32 x 64-bit register file
	- 64-bit data is called a **"doubleword"**
		- 31x64-bit general purpose registers X0-X30
	- 32-bit data is called a word
		- 31x32 bit general purpose sub-registers W0 to W30
- Register purposes:
	- X0-X7: Procedure args/results
	- X8: Indirect Result location register
	- X9-X15: Temporaries
	- X16-X17 (IP0-IP1) may be used by linker as a scratch register, otherwise a temp reg
	- X18: Platform register for platform independent code, otherwise temp
	- X19-X27: saved/reserved
	- X28 (SP): Stack pointer
	- X29 (FP): Frame pointer
	- X30 (LR): Link register (return address)
	- XZR (register 31): The constant value 0
# Memory Operands
- Main memory used for composite data
- Data transfer instructions (load and store) transfer data between memory and registers
- To access a word or doubleword in RAM, the instruction must supply the memory address, typically starting at 0
- LEGv8 is **BYTE ADDRESSABLE**
	- Each byte in memory is individually addressable
	- Consider a C array called A which contains 8 byte doublewords at each array index
		- why 96, why not just 12? If it's byte addressable not bit addressable?
			- Because the array contains doubleword elements
		- A starts at byte 0 of register X22
		- `A[0]` represents the 8 bytes contained in reg X22
		- `A[1]` represents the next 8 bytes, which is written as `[X22, #8]` or 8 bytes after the start of X22
		- If the C code calls for `A[12]`, the corresponding operand would be `[X22, #96]`
			- 96=8x12
	- This means that we can derive a formula for accessing array elements
		- Consider an array whose first element is stored at address $B$ and has elements of size $S$ bytes
		- Accessing the $n^{th}$ element of this array would require accessing the memory address $A=B+Sn$
- LEGv8 does not require words to be aligned in memory, except for instructions and the stack
- For Store (STUR) and Load (LDUR) instructions, the first operand is the register to be stored from or loaded into. The second operand is a register which contains a memory address, plus some offset
	- Format: `LDUR X20, [XZR, #50]`
		- There must be an immediate (constant) offset included
		- This instruction loads the value of memory address 50 into register X20
# Instruction Format and Representation
- All LEGv8 instructions are 32 bits wide
- Depending on the instruction format, these bits will be organized into fields of different sizes that each represent a different piece of the instruction
## Field Names
- **Opcode**: Type of operation
- **Rm**: Second register source operand
- **shamt**: Shift amount
- **Rn**: First register source operand
- **Rd:** Destination register
- **Rt:** Can be source or destination register
## Instruction Formats
### R-Type
- Register operations
#### Assembly Format
1. Opcode
2. Operands are in the opposite order in assembly vs machine code
`ADD Rd, Rn, Rm`
#### Machine format
![[Pasted image 20240830173028.png]]
1. 11 bit opcode
2. 5 bit Rm
3. 6 bit shamt
4. 5 bit Rn
5. 5 bit Rd
### I-Type
- Immediate operations
- Adds a larger 12 bit section for immediate operand
#### Assembly Format
`ADDI Rd, Rn, #immediate`
#### Machine format
![[Pasted image 20240830173803.png]]
1. 10 bit opcode
2. 12 bit immediate
3. 5 bit Rn
4. 5 bit Rd
### D-Type
- Used for memory access
#### Assembly Format
`LDUR Rt, [Rn, #address]`
#### Machine Format
![[Pasted image 20240830174913.png]]
1. 11 bit opcode
2. 9 bit address (offset in case of LDUR/STUR)
3. 2 bit op2
4. 5 bit Rn
5. 5 bit Rt
	1. Note this is Rt instead of Rd because it can be a data source during store or destination during load

## B-Type
- Used for branch operations
- Only instruction that doesn't work with data, only program counter
#### Assembly format
- Note that this instruction is written with labels, which are an assembly abstraction above machine code
```
Label: do thing

B [Label]`
```
#### Machine Format
- 6 bit opcode, 26 bit exit
## CB-Type
- For conditional branches
#### Assembly format
```

```

#### Machine Format
- 8 bit opcode
- exit address 19 bits
- source register 5 bits

![[Pasted image 20240830175438.png]]

![[Pasted image 20240912193424.png]]
From [cheat sheet ](https://www.usna.edu/Users/cs/lmcdowel/courses/ic220/S20/resources/ARM-v8-Quick-Reference-Guide.pdf)

For class #comporg