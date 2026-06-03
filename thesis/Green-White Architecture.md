# Green Vs. White Cores
## White Core
- The White core is the host CPU
- Is hard silicon, in our case the 96 core EPYC CPU
- Runs code written in a divide-and-conquer fashion
- Identifies acceleration targets and sends those targets to the green core array
- The targets are the leaves of the call graph, the base cases
- Divides the work until it is small enough to fit in the local memory of a green core, then sends it to green cores to be executed in parallel
## Green Core
- A small core, currently RISC-V
- Could be an HLS core in the future
- Currently running Micropython
- Has **Banked BRAMs**
- The core itself sees a single 64KB address space, but there are actually 4 64KB BRAMs within a green core connected to the compute core through a DeMUX
- This allows 3 things to happen concurrently
	- Transferring data and instructions into a BRAM
	- Executing code from a BRAM
	- Transferring result data from a BRAM
- The green core can switch tasks by holding the compute core in reset, switching BRAM banks, and then waking up the compute core.
- Will be implemented in 1 or many V80 FPGAs
- The green cores do not have to be lightning fast, they only need to be fast enough to keep the bandwidth of the HBM fully utilized at all times
## Etymology (Fun Fact, Not Important)
- Inspired by green and red salsa
- The green salsa isn't as spicy, likewise the green core doesn't have much computing power
- Too many things are already called Green-Red
- Thus the faster, hotter core is called the White core
# The DMA
- The addresses of BRAM banks will be contiguous from the global view (Vivado address editor)
- The DMA core could simply transfer data from DDR to an arbitrary BRAM across the AXI bus using these global addresses
	- This would require two AXI masters on the DMA core
	- Would be best for a central pool of DMA engines
- The DMA core could have a BRAM controller built into it
	- Single cycle access to the BRAMs, no AXI shenanigans
	- Must be within the Green Core block to attach directly to BRAM Generators
## Smart DMA Concept
- The white core could generate an ELF containing the micropython interpreter and precompiled code for the base case execution
- The DMA controller, written with HLS and implemented in PL, could read the ELF and DMA only the required bytes into local memory
- This component is my master's thesis