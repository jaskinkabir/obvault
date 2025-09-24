# What Happens at an Interrupt
- CPU backs up all registers
- The Cortex-M0 automatically pushes these rigesters onto the stack
	- R0, R1, R2, R3
	- R12
	- LR
	- PC
	- xPSR (Prog Status Reg)
- This save is called exception stack frame
- After saving, jumps to ISR address from vector table
# The Interrupt Vector Table
- A lookup table stored at the beginning of Flash memory (0x0)
- Contains addresses of all exception and interrupt handlers
- First entries are reserved for stack pointer and reset handler
## Structure (Cortex-M0)
![[Pasted image 20250923161711.png]]
- What are these entries?
	- Initial Main stack pointer value
	- Reset Handler address
	- NMI Handler
	- HardFault Handler
	- ...
	- Later entries: Peripheral interrupts
- How are they used?
	- The first entry is an address in SRAM for the beginning of the stack, which is loaded into the MSP
	- Second entry is used as Reset_Handler address, which holds the address of the first line of code
# The Nested Vectored Interrupt Controller (NVIC)
## Interrupt Priority
- NVIC supports up to 4 priority levels (0-3)
- Lower priority levels must wait for higher priority IRQs to finish
For class #embedded