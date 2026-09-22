Continues [[Processes]]
Continued by [[Interrupts and Rescheduling]]
# Context Switching
![[Pasted image 20260827103711.png]]
- Note that there is some time after execution is stopped where both processes are idle
- No two PCBs in the process table can have the running state at the same time
- Thus, the first process must be stopped while the state of the next process is changed in the process table
- ![[Pasted image 20260827104339.png]]
- The context switch has overhead, we need to ensure the OS does it as little as possible
## Where is State Saved
- State goes to memory
- Can either go to PCB or stack
	- Xinu saves to stack
# x86 Refresher
## Registers
### Pointers
- EIP: Instruction pointer, next instr to be executed (Automatically updated)
- ESP: Stack pointer; last element in **stack** (Automatically updated)
	- Updated by `PUSH` and `POP`
- EBP: Base pointer of last **stack frame** (Explicitly updated)
	- Used to index individual variables as offsets from EBP
	- Used to know the bounds of and deallocate stack frames
	- Updated by `CALL` and `RET` instructions
### General Registers
- EAX: Accumulator
	- Contains return value
- EBX: Base
- ECX: Counter
- EDX: Data
### Indexes (For string/array ops)
-  ESI: Source Index
- EDI: Destination Index
### Flags
- EFLAGS: Flags (for conditional branches, etc)

## Instructions That Interact With Stack
- `call`: Push a instr address onto th stack
- `ret`: Pops an instruction address from the stack
- `popal`/`pushal`: Pop/push all registers from/to stack
- `pushfl`/`popfl`: Pop/push flags
## Function Calling
### Creating New Stack Frame
![[Pasted image 20260827110630.png]]
![[Pasted image 20260827110702.png]]
![[Pasted image 20260827110719.png]]
### Passing Args
- How to pass arguments/parameters to called function?
	- x86 Convention places arguments in the caller's stack frame right before the return address
	- Called function accesses the arguments by indexing backwards from the base pointer
	- ![[Pasted image 20260827111411.png]]
- Caller must save current base pointer to the stack, then set the base pointer to the current stack pointer
- ![[Pasted image 20260827111603.png]]
### Saving Registers
- x86 convention saves some registers before the arguments in the caller frame and others after the saved EBP in the callee frame
- ![[Pasted image 20260827111901.png]]
### Local Variables?
- Saved after the saved register state
- Why not save local variables in heap?
	- Heap memory must be explicitly allocated and deallocated
	- Local variables are only used by the function, not shared
	- By saving locals to the stack, the return procedure–deallocating the entire stack frame—itself deallocates the local variables
- The Context Switch operation creates a context switch frame at the top of the old process's stack that contains state to be restored

# Xinu Context Switch (`ctxsw.S`)
![[Pasted image 20260827112524.png]]

# Context Switch 4 Phases
1. Push current process ($p_{old}$) state onto stack
2. Save ESP into `proctab[pold].prstkptr`
3. load ESP from `proctab[pnew].prstkptr`
4. Pop state of new program from stack