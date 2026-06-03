# Overview
# Interface
- Core exposes tail pointer value to PS
	- Core should also expose head pointer value for debugging
- PS takes note of tail ptr val and writes cmd params
	- Only if the buffer is not full
	- Now it can poll that address for the completion status
	- Writing to the length register issues the command
- If a datamover becomes available,
	- The scheduler will assign the command and provide the commands over the command ports
	- Advance the head pointer
- The entry does not become free until the PS acks the completion (clear on write)
- 
# Queue Format
- Two FIFOs, command and status
## Command Queue
- SRC: 40 bit
- DST: 40 bit
- LEN: 23 bit
## Status Queue
- ID: $\log_{2}(L)$ bits
	- L is the command queue depth
- STATUS: 8 bit
	- \[0:3\]  S2MM
	- \[7:4\] MM2S
	- Note the status output from the datamover is 8 bits, but 4 are for the ID which will always be 0
- 


