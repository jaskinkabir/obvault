Continues [[Exceptions and Interrupts]]
Continues [[CPU Pipelining-Multicycle Execution]]

# Instruction-Level Parallelism
- A deeper pipeline (with more stages) has a higher level of ILP
	- More things are done at once
	- From the laundry analogy, imagine the washing machine is split into a washer, rinser, and spinner thus creating a 4-stage pipeline rather than a 2-stage
	- Operations are overlapped
- But the steps must be rebalanced so that each one is the same length
# Multiple-Issue Parallelism
- Replicate the internal components of the system to launch multiple tasks in the same cycle
	- This is how multithreaded processors achieve parallelism
- More control logic is required to keep the components busy and manage the overall system
- There are two ways to implement multiple issue, and the difference is in the division of work between the compiler and the hardware
	- **Static Multiple Issue:**
		- The decision on how to split work is done at compile time
		- Simpler hardware, more complex compiler
	- **Dynamic Multiple Issue**
		- Decisions are made dynamically during execution time
		- Has more complex hardware
		- More flexible
- Two primary responsibilities must be handled by a multiple-issue pipeline
	- 1. Packaging instructions into issue slots
		- How does the processor determine which and how many instructions can be issued in a given cycle?
		- **Issue Slots:** The positions from which instructions could issue in a given clock cycle
	- 2. Dealing with Data and Control Hazards

# Speculation
- An approach in which the processor guesses the outcome of an instruction to remove it as a dependence in executing other instructions
- Examples:
	- We might speculate that a store that precedes a load does not refer to the same address, so the load can be performed before the store
	- Assume a branch is not taken, so the instructions directly proceeding the branch can be executed first
- Speculation can be wrong
	- A speculation scheme must include a mechanism to check if its guess was right and a way to roll back to correct its error
	- Recovery methods are different for static and dynamic specualtion
		- In static speculation, the compiler will insert some instructions that check if the speculation is correct and a recover procedure
		- In dynamic speculation, the speculated results are buffered until it is confirmed that the speculation was correct
# Very Long Instruction Word Pipeline
- The set of instructions issued in a given clock cycle is called an **Issue Packet**, which can be thought of as one large instruction with multiple operations
	- The original name for this approach is **Very Long Instruction Word (VLIW)**, because it's like 1 very long instruction executed at once
		- A single wide instruction with several opcode fields
## Static Double-Issue Example
### Requirements
- Assume some processor can issue two instructions at once
	- A Load/Store
	- And one ALU/branch
- The layout of simultaneously issuing instructions is restricted to simplify the decoding process
- In this case, require that the instructions are paired and aligned on a 64 bit double word, with the ALU/Branch portion appearing first
	-  (\[63:32])
- If one of the instructions cannot be used, it will be replaced with a nop
- Assume that the compiler tries to reduce the number of data/control hazards, but the CPU must still be equipped to handle them
### Additional Hardware Required
- Instruction Memory
	- Second output port to read out the second instruction of the packet
- Register file
	- Add two more read ports and one more write port to the register file
- Additional Adder
	- Represented as a second ALU, this is used to calculate the address calculations for data transfers
- Additional Sign Extender
	- One sign extender for immediate ALU operations, one for extending the offset of the target memory address
![[Pasted image 20241111193544.png]]
# Use Latency
- Use latency is the number of clock cycles required after a load instruction is fetched for an instruction that uses that loaded data to be fetched without stalling the pipeline
- In the single issue implementation, loads have a one cycle use-latency
- However, the double-issue system has a two-instruction use latency for loads, because the result of a load operation cannot be used in the next packet. An entire packet of 2 instructions must pass through the pipeline before the loaded data may be used
	- This is still just a one-cycle use latency, but the hazard handling is now more complicated
- Additionally, load instructions that immediately proceeded ALU instructions with a dependency do not have a use latency in the single issue implementation. Forwarding can alleviate this
	- However, in the double-issue system, these ALU instructions have a use latency of 1 cycle 
# Loop Unrolling
- **Loop unrolling** is the process by which multiple copies of a loop body are made to increase performance as instructions from different iterations are executed together
- Consider the following program
- ![[Pasted image 20241111194021.png]]
- The first 3 instructions have dependencies, and so do the final two
- **No Unrolling**
	- To execute this on the double-issue system, the instructions are packaged as follows
		- The LDUR, SUBI, ADD, and CMP instructions are executed one by one
			- Nop in the packet alongside
		- Then, the branch and store instructions are executed in parallel
	- This is okay, but only two instructions were parallelized
- **With Unrolling**
	- Assume that the initial loop index value is always divisible by 4
	- This means that we can execute 4 iterations at a time by simply subtracting 4(\*8) from the loop index on each iteration
		- The first load and subtraction of the loop index are issued together
	- The second load is done alone, since nothing else can occur yet
	- The first addition operation is done alongside the third load
		- Then 2+ with 4L
	- The third addition is done alongside the first store
		- Then 4+ with 2S
	- The comparison is done alongside the third store
		- Then the branch alongside 4S
	- ![[Pasted image 20241111194834.png]]
- The unrolling massively increased performance, but it had to **rename** the X21 register to deal with the fact that the original program stored the result of the addition in the same register for all iterations
	- This gives the illusion of a dependency between iterations, but it is not a true dependency
	- This is called an **Antidependency (or Name Dependency):** where ordering is forced by the reuse of a name, rather than a true dependence that carries a value between instructions
		- This antidepencency is solved through **Register Renaming**

# Superscalar Processors
- **Superscalar:** An advanced pipelining technique that enables the processor to execute more than one instruction per clock cycle by selecting them during execution
- A superscalar processor ensures that the hardware will correctly execute code, which is not true of VLIW processors.
## Dynamic Pipeline Scheduling
- **DPS:** Hardware support for reordering order of instruction execution to avoid stalls
- Consider this code
	- ![[Pasted image 20241111195530.png]]
	- There is a load-use hazard between the first two instructions. 
	- The SUB instruction may have to wait for a stall to be executed before the ADD, and then the ADD itself, even though it is ready to be executed already
### Organization
- A CPU with a dynamically scheduled pipeline is organized into three units:
	- Instruction Fetch/Decode/Issue Unit
	- Several functional units
	- **Commit Unit:** Decides when it is safe to release the result of an operation to registers and memory
- Each functional unit has a **reservation station** that holds the operands and the operation
- Execution Process
	- The Issue unit fetches and decodes instructions, then assigns them to the different functional units
	- Once the units have their operands in the reservation stations, the result is calculated and sent to the commit unit and any other reservation stations that need to read this value
	- The commit unit then buffers these results until they are ready to release
- **Reorder Buffer**
	- This buffer holds the results until they are safe to release
	- They also contain operands, in much the same way that forwarding is done in the statically scheduled pipeline
- ![[Pasted image 20241111200306.png]]
### Pseudo-Renaming
- The reservation stations and reorder buffer provide a form of register renaming
	- When an instruction issues, it is copied into the appropriate functional unit's RS. Any operands that are available in the register file or reorder buffer are also copied into the RS. This means that the actual register value is no longer required, and can be rewritten with no consequence
	- If the operand is not in the register file or reorder buffer, it is waiting to be produced by some FU. Whichever FU will produce that operand is tracked. Whenever it is produced, it is copied into the reservation station from the FU, bypassing the registers
### Out-Of-Order Execution
- On a high level, the dynamically scheduled pipeline analyzes the data flow order of the program and manipulates the instruction order to preserve the data flow while achieving maximum parallelism
- Because the actual instruction execution order is different from what was provided in the program, this is called **Out of Order Execution**
### In-Order Commit
- To make programs behave as they are written, the fetch unit is required to issue instructions in order, which allows dependencies to be tracked
- The commit unit must also write results to memory and registers in program fetch order
- This conservative scheme is called **In-Order-Commit**. If an exception occurs, the last instruction executed can be pointed to, and the only state that has been changed was the result of the instructions before the offending instruction.
	- The results of pipelined execution are written to programmer-visible state in the same order that the instructions are fetched

For class #comporg