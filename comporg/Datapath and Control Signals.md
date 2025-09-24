# IF
## Data
- Instruction
- PC Target
# ID
## Data
- Current PC Value
- Rn1
- Rm2
- Rd
## Control Unit
- RegWrite
- Reg2Loc
	- Source Reg B is either at the beginning or end of instruction
		- End for CBZ/CBNZ instructions
- Branch
	- Switches PC source from PC+4 to target address
	- ANDed with output from adder
- UncondBranch
	- ORed with Branch
- Memread
- Memwrite
- Mem2Reg
	- Controls Register source, ALU vs memory out
- ALUOp1/2
	- D: 00
		- Hardwired addition op
	- CBZ: 01
		- Pass B input for 0 test
	- R: 10
		- ALU op determined by instruction
- ALUSrc
	- ALU Src2 either comes from immediate operand or register file port 2
## Hazard Detection
- IF.FLUSH
	- Zero IF/ID reg's instruction field
	- Zero ID/EX
- IF/IDWrite
	- When high, IF/ID reg is updated
- PCWrite
	- When low, PC stays static
## Register File
- Rn1Data
- Rm2Data
## Target Adder
- PC Target
## Sign Extender
- Immediate value
# EX
## Data
- ALU out
- ALU B in
## Forwarding Unit
- ForwardA
	- 00, ALUsrc1 is from register
	- 01, ALUsrc1 is from MEM/WB.Rn1
	- 10, ALUsrc1 is from EX/MEM.Rn1
- ForwardB
	- Same as above but for Rm2
# MEM
## Data
- MEM Data out
# WB
## Data
- Reg in


|           | Source | Control | Hazard Detection | Forwarding |     |
| :-------- | :----- | :------ | :--------------- | :--------- | :-- |
| **Stage** |        |         |                  |            |     |
| IF        |        |         |                  |            |     |
| ID        |        | Reg2Loc | ALUOp1/2, ALUSrc |            |     |
| EX        |        |         |                  |            |     |
| MEM       |        |         |                  |            |     |
| WB        |        |         |                  |            |     |
For class #comporg