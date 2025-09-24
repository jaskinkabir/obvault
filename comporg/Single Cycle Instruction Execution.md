Continues [[LEGv8 Architecture]]
Continued by [[CPU Pipelining-Multicycle Execution]]
# Execution Cycle
1. Fetch
	1. This stage involves the program counter and instruction memory
2. Decode
	1. Figure out where operands are located
	2. Which signals to generate to execute instruction
	3. This stage uses the 
3. Execute
	1. Uses the ALU
4. Memory Access (optional)
5. Register Write
	1. Data in will come from either the Data memory or the ALU output
# CPU Diagram
![[Pasted image 20241009175819.png]]
## Register File
- Note that there are 3 register address inputs
	- This is because instructions only ever involve a max of three registers
- 
## MUXes
- 
- Input of ALU
	- Register or immediate value from instruction memory
- Input of register file
	- ALU output or Data memory output
- Program counter input
	- PC +4 or PC + offset from branch instruction
	- Branch instructions are **PC Relative**
	- This is because a block of code may be placed anywhere in memory by the linker. To ensure proper jumping operation, branch locations must be given relative to the current instruction address
## Control Logic
![[Pasted image 20241009180405.png]]
- Generates control signals based on the current instruction
	- RegWrite
	- MemRead/Memwrite
	- Branch
# Building a Datapath
## What is a Datapath
- The components required to execute instructions and the connections between them
	- This does not include components that generate control signals
- Any **Datapath Element** is a component used to operate on or hold data
- 
## Instruction Fetch
- Need a 32 bit program counter register
	- Updates on each rising clock edge
## R-Format Instructions
![[Pasted image 20241009183856.png]]
1. Read two register operands
2. Perform ALU operation
3. Write register result
## Load/Store Instructions
![[Pasted image 20241009183904.png]]
1. Read register operands
2. Calculate address using 16-bit offset
	1. Use ALU, but sign-extend offset
	2. This is because load-store instructions use a 9-bit memory address but branch instructions use 19 bits
	3. These values must be sign extended to 64 bits using the **Sign Extension Unit**
		1. This unit takes the whole 32-bit instruction as an input, extracts the relevant address bits, and sign extends it to 64 bits
3. Load
	1. Read memory and update register
4. Store
	1. Write register value to memory
## Branch Instructions
![[Pasted image 20241009183923.png]]
1. Read register operands
2. Compare operands
3. Calculate target address
	1. Sign-extend displacement
	2. Shift left 2 places
	3. Add to PC + 4
		1. Already calculated by instruction fetch
- Note that the PC offset value from the branch instruction must be left shifted by 2
	- This is because the value in stored in the instruction is in terms of instruction number (0,1,2,3,4...) in order to save two bits of memory
	- But the PC stores an address in terms of byte location (0,4,8,12,16...)
	- The instruction number is converted to a byte address through this left shift operation (multiply by 4)
## Full Datapath
![[Pasted image 20241021174107.png]]
# Building a Control Path
![[Pasted image 20241021180139.png]]
## Control Signals
- **Reg2Loc**
	- The first source register of any operation is in bits 5-9 of the instruction
	- However the second source register can be either 20:16 or 4:0
		- Only for conditional branch instructions is it 4:0
	- This signal selects which location
- **RegWrite**
	- Enables register write
- **Unconditional Branch**
	- Will always cause a branch when set high
- **Branch**
	- Changes source of PC register to ALU result
	- ANDed with 0 flag of ALU for CBNZ
- **MemRead**
	- Enables data memory read
- **MemWrite**
	- Enables data memory write
- **MemtoReg**
	- Selects whether the input of the write register is from the ALU output or the data memory output
- **ALUOp**
	- Two bits that tell the ALU controller which format of instruction is being read
	- Formats:
		- D: 00
			- For a LD/STR instruction, the operation for the ALU is addition
		- CBZ: 01
			- For a CBZ, the B input should be passed to test for 0
		- R: 10
			- ALU operation is determined by instruction
- **ALUSrc**
	- Controls whether second source operand of ALU comes from the register file or an immediate value from the instruction memory (after sign extension)


| ALU Control | Function         |
| ----------- | ---------------- |
| 0000        | **AND**          |
| 0001        | **OR**           |
| 0010        | **add**          |
| 0110        | **subtract**     |
| 0111        | **pass input b** |
| 1100        | **NOR**          |


For class #comporg