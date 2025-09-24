Continued by [[System Software]]
# Baremetal
- Compiles directly to executable
- No system/driver code
# Standalone
- Xilinx provides
	- Library
	- System (runtime)
	- Drivers
- There is no supervisor mode, every application has direct hw access
- Only physical address space
# Real Time (RTOS)
- Fully fledged operating system
- Provides the abstraction of processes
	- Each application above the driver and system layers operate in virtual memory addresses
		- Driver/System are physical addresses
		- Library/App are virtual addresses
		- They each have copies of the system and drivers
			- Can run independently
- Has a memory management unit that converts from virtual to physical memory addresses
	- Virtual memory organized into pages
	- 
## RTOS Organization
- Shell
- Application
- Library
	- Only virtual address space here above
- System
	- Kernel is everything below library
	- Has access to mmu in both physical and virtual spaces
	- Run in privileged state
- Drivers
- Hardware
## System Vs. Library Calls
- System calls are much slower/take more cycles than library calls
- The library can handle abstractions like buffering inputs to make one slow system call for many faster library calls

For class #reconfig