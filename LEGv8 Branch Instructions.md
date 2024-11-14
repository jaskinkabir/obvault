Continues [[LEGv8 Architecture]]
Continued by [[LEGv8 Procedure Calling]]


# Compiling Loops
- Implement these mental strategies
	- For loops can be written as while loops
	- `while(cond) {code;}` can be rewritten as `while(1) {if (!cond) break; code;}`
	- `while (cond) {code;}` is the following in assembly
```
Loop: (check cond operation (should return 0 if cond))
CBNZ Xn, Exit
code
Exit: 
```
- Similar to the guard clause pattern


# Basic Blocks
- A basic block is a sequence of instructions with
	- No branches except for the exit
	- No branch entrances except at the entrance
- Compiler identifies these for optimization
# More Conditional Operators
- The ALU sets Condition Codes (CCs) when an instruction with the -S(set flags) suffix is executed (ie SUBS)
	- Negative (N): Result had 1 MSB
	- Zero (Z): result was 0
	- Overflow (V): Result overflowed
	- Carry (C): Result had carryout from MSB
- Many relations between two numbers subtracted from each other can result in 10 comparisons from just these 4 bits
- Results in 10 branch instructions
	- B.EQ
	- B.NE
	- B.LT : **Less than signed**
	- B.LO : **Less than unsigned**
	- B.LE : **Leq, signed**
	- B.LS : **Leq, unsigned**
	- B.GT :  **GT, signed**
	- B.HI :  **GT, unsigned**
	- B.GE : **Geq signed**
	- B.HS : **Geq, unsigned**
- The following table can be constructed which shows how these instructions are implemented
- 
	![[Pasted image 20240909183146.png]]
	- TODO: Understand this table
For class #comporg