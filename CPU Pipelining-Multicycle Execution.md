Continues [[Single Cycle Instruction Execution]]
Continued by [[Data Hazards Forwarding and Stalling]]
Continued by [[Control Hazards and Branch Prcoediction]]
Continued by [[Exceptions and Interrupts]]
Continued by [[Parallelism Via Instructions]]
Continued by [[Datapath and Control Signals]]
# Pipeline Stages
1. **IF:** Instruction Fetch
	1. Uses instruction memory
2. **ID:** Instruction Decode
	1. Uses register file
	2. Includes register access for operands
3. **EX:** Execution
	1. Uses ALU
4. **MEM:** Memory access
	1. Uses data memory
5. **WB:** Write-back
	1. Uses register file
	2. This is the stage in which the result is written to the register file
# Pipeline Diagrams
- ![[Pasted image 20241023175358.png]]
- The shading of the box indicates whether the stage uses a resource and if the resource is being read from or written to
	- If the shading is on the right, the resource is being read from
	- If the shading is on the left, the resource is being written to
	- This shading also indicates which half of the clock cycle is being utilized
# Pipeline Speedup Formula
- $T_{pipe}=\frac{T_{nonpipe}}{\text{\# Of Stages}}$
	- This is assuming stages are balanced (take equal time)
- Without balanced stages the speedup is less
# Terms
- **Latency** or **Path Delay**
	- How long the instruction takes to execute from stage 1 to stage $n$
- **Throughput**
	- Instructions per unit time
	- Hz
## Dependencies
- Write after Write
	- No hazard
- Read after write
	- Can cause hazard!!!
	- **Data Hazard**
- Write after read
	- Can cause hazard !!!****
- Read after read
	- No hazard
- For a dependency statement in the form '$a$ after $b$' the dependency could cause a hazard iff $a \neq b$, where $a,\,b$ are either 'read' or 'write'
# Pipeline Registers
- Separate CPU into the hardware needed for each stage
- Add registers in between each stage to hold data transferred between each section
- ![[Pasted image 20241028180453.png]]
- There are 7 control signals, and they should be assigned to each stage
- ![[Pasted image 20241110184213.png]]
	- ![[Pasted image 20241110184253.png]]
	- The control unit generates its signals in the ID stage, so the IF stage's signal need not be propagated through the registers
- The registers also contain the values generated by the datapath
	- IF Stage
		- PCTarget
			- Can be updated by EX stage
		- Instruction
			- RegisterRn1
			- RegisterRm2
			- RegisterRd
	- ID Stage
		- SignExtenderOut
		- RegisterRn1Data
			- Not ever passed to MEM stage
		- RegisterRm2Data
	- EX Stage
		- Updated PC Target
		- ALU Flags
		- ALU Result
		- RegisterRdData
	- MEM Stage
		- ReadData
# Hazards
- Defined as some situation that prevents starting the next instruction in the next cycle
- Types include
	- Control Hazard
	- Data Hazard
		- Load use hazard
	- Structure Hazard
## Stalling
- A **Stall** is where a full cycle is inserted into the execution procedure in which the CPU does nothing
	- This called a **No-op**
	- It is represented in the pipeline diagram as a row of 5 bubbles.
## Control Hazard
- Deciding on control action depends on previous instruction
- Caused by conditional branch instructions
### Branch Prediction


## Structure Hazard
- A required resource is busy
- Ex: A multiply instruction is using the ALU, but an add instruction is now



For class #comporg
