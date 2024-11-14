
# Library Call
- Regular C function call
	- Fast
	- Simple for programmer
	- Never leaves application layer
# System Call
- Generates an interrupt or exception
- Transfers control to OS
- Changes to super/privileged mode
- System calls are slow and expensive. 
	- Typically, many system calls are buffered to be executed all at once rather than interrupting application execution every time a system call must be made
# Shell and Kernel Organization
1. SHELL
2. Application
3. Library
4. System
5. Drivers
	1. System and Drivers make up the kernel
6. Hardware

# C Statements
-  A C function is composed of statements, which are either
	- A basic assignment
		- Two expressions on either side of an equal sign
	- Or a compound statement
		- Sequence 
			- Join two statements to mean 'do these two steps in sequence'
		- Alternation
			- Do one step or the other, but not both, based on some condition
		- Iteration
			- Repeat some step so long as some condition holds
## Combining Statements
Consider:
```c
x = 0;
x = x + 1;
```
- These two statements can be combined into a single compound statement: `x=0 + 1;`
	- This is the juxtaposition join
	- The first `;` symbol is the join operator
# Variables (Objects)
- Must be declared
	- To know how many bytes of memory to set aside to store them
- Have lifetime and scope
	- Lifetime - When the variable is assigned and possibly de-assigned a space in memory
	- Scope - vars declared within a function are local to and can only be referenced within that function. The syntax delineates what the symbol means.
For class #research-tools

