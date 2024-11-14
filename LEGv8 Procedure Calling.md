Continues [[LEGv8 Branch Instructions]]

# The Stack and Stack Pointer
- Register X28 is reserved as the Stack Pointer (SP)
- It contains the address in memory that corresponds to the top of the stack, which is where any register values that will be modified by a procedure can be stored and restored from
- To store $n$ register values onto the stack:
	- Push the stack pointer back by $8n$.
	- Store the values to $SP[0]\dots SP[8(n-1)]$
- To restore $n$ register values from the stack:
	- Load the values from $SP[8(n-1)]\dots SP[0]$
	- Pop the stack pointer forward by $8n$
- Note that the stack pointer is only preserved if it is pushed back and popped forward an equal amount upon loading and storing.
	- The convention is that the stack expands downwards in the memory address space
# Procedure Calling Steps
1. Place parameters in registers X0 to X7
	1. If X0-X7 are already occupied, copy their values into stack
	2. The register X28 is the stack pointer (SP)
	3. The stack is stacked goes down
2. Transfer control to procedure
3. Acquire storage for procedure
	1. Note that the copying of occupied registers onto the stack is performed by the procedure and not the caller
	2. This is to provide a black box to the caller
4. Perform procedure operations
5. Place result in register for caller
6. Return to place of call (address in X30)
	1. If X0-X7 were occupied before, return them from the stack
	2. X30 is the Link Register (LR) stores return address (point of origin)

## Leaf Example

```c
long long int leaf_example(int g, int h, int i, int j ) {
	int f;
	f = (g + h) - (i + j);
	return f;
}

X9 = 1;
X10 = 2;
X11 = 3;


X13 = leaf_example(X9,X10,X11,4);
```
- Since X9-X11 are already occupied by global scope variables, they must be placed into the stack
- Assume
	- X0=g
	- X1=h
	- X2=i
	- X3=j
- Steps
	- Push the stack pointer back by 3 (1 for each occupied reg)
	- Store X11-X9 onto the stack (note that order doesn't matter like a data structures stack)
	- Perform the function operations
	- Store the result in X0
	- Return stack values to registers
	- Push stack pointer forward 3
	- Branch to the return address in link register X30
```c
main:
// Insert 1,2,3 into X9-X11
// Copy X9-11 into X0-X2
// Insert 4 into X3
BL leaf_example
ADD X13, X0, XZR // Place result into specified register

leaf_example:
// 3 values are occupied, 3x8 bytes must be added on top of the stack
SUBI SP, SP, #24  // Move SP back 3
STUR X11, [SP, #0]
STUR X10, [SP, #8]
SUR X9, [SP, #16]

// Perform 
ADD X9, X0, X1
ADD X10, X2, X3
SUB X11, X9, X10
ADD X0, X11, XZR // Result in X0

SUR X9, [SP, #16] // Return stack values to reg
STUR X10, [SP, #8]
STUR X11, [SP, #0]
ADDI SP, SP, #24 //Push SP forward 3

BR LR
```
## LEGv8 Abstractions
- LEGv8 makes the following register reservations to make function calling easier
	- LEGv8 reserves X0-X7 as eight registers to hold the function parameters and return values
	- LEGv8 also reserves X30 as the Link Register (LR) to hold the return address for the point of origin
	- Additionally, X27 is reserved for the stack pointer, which holds the memory address for the 'top' of the stack
- Additionally, the architecture provides the **Branch-And-Link** instruction, which branches to some procedure address and saves the next instruction's address to the link register
	- Format: `BL ProcedureAddress`
- For returning to the return address, LEGv8 provides a **Branch Register** operation that allows the CPU to branch to an address stored in a register
	- Format: `BR Rs`
		- Typically Rs is LR

# Nested Procedures
## Leaf and Non-Leaf Procedures
- A Leaf Procedure does not call another procedure (tree metaphor)
- Non-Leaf, or nested procedures, call other procedures and create complications. Suppose the Main program calls procedure `A` with an argument `3` by placing `3` into register X0, and then running `BL A`. Then suppose procedure `A` calls `B` via `BL B` with an argument of 7, also placed into X0.
	- Since A isn't finished yet, there is now a conflict over who gets register X0
	- Similarly, `BL B` now updates LR, which is another conflict
	- This conflict will eliminate procedure A's ability to return to its caller or properly access its original arguments
## Solution:
- Push all registers that must be preserved onto the stack. The caller of the non-leaf procedure pushes any argument registers (X0-X7)  or temp registers (X9-X17) to the stack that are needed after the call
- The called non-leaf procedure will then store the return address (LR) onto the stack and execute its operations
- Upon return, the registers are returned from memory and the stack pointer is readjusted
## Factorial Example
Consider the following C code
```c
int fact (int n) {
if (n < 1) return 1;
return n * fact(n-1);
}

X19 = 4;
X1 = fact(X19);
X20 = X19 + X0;
```
The compiled function code would:
- Adjust the stack to store return address and argument
- Perform its procedure
- Adjust the stack pointer after restoring the argument and link register

```c
ADDI X19, XZR #4 // X19 = 4
ADD X0, X19, XZR // X0 = X19 (for arg)
BL fact // X1 = fact(X0) = fact(X19) = fact(4)
ADD X20, X19, X1 // X20 = X0

fact:
	// Allocate and store LR and X0 on the stack
	SUBI SP, SP, #16 // SP -= 16
	STUR LR, [SP, #8] // SP[8] = LR
	STUR X0, [SP, #0] // SP[0] = X0 = n

	SUBIS XZR, X1, #1 // Test n lt 1
	B.GE Else // If n geq 1 goto else
	ADDI X1, XZR, #1 // X1 = 1 (return 1)
	ADDI SP, SP, #16 // Adjust stack pointer
	BR LR // Return (LR has not been changed, no restore)

	Else: 
	SUBI, X0, X0, #1 // X0-=1
	BL fact // X1 = fact(X0) = fact(n-1)

	LDUR X0, [SP, #0] //X0 = SP[0] = n
	LDUR LR, [SP, #8] //LR = Sp[8] = original LR
	ADDI, SP, SP, #16 // SP += 16

	MUL X1, X0, X1 // X1 = X0 * X1 = n * fact(n-1)
	BR LR // Return n X1 = n * fact(n-1)
	
```
# Preserved and Non-Preserved Registers
- When a procedure is called, the registers that are preserved or not can be found in the following table

| Preserved                        | Not Preserved                    |
| -------------------------------- | -------------------------------- |
| Saved Registers X19-X27          | Temp Registers X9-X15            |
| Stack pointer register: X28 (SP) | Argument/Result registers: X0-X7 |
| Frame pointer: X29(FP)           |                                  |
| Link Register: X30 (LR)          |                                  |
| Stack above SP                   | Stack Below SP                   |
- Note that X16-18 are also temporary registers, but they can be used for other purposes, so their use is discouraged
- If a procedure must use or modify any preserved registers, it must save them onto the stack and restore them before returning
## Global Pointer and Static Vars
- A variable that is global and should not change upon procedure calls is stored in the **static** area of memory
- The **Global Pointer** is a register that is reserved to point to the static area of memory (heap)
	- This register is not reserved by LEGv8 and is optional
	- If it is reserved, it must also go in the preserved column of the above table
# Procedure Frame and Frame Pointer
- The **Procedure Frame** aka **activation record** is a segment of the stack containing all of a procedure's saved registers and local variables
	- The stack is not just used to store register values, but also local procedure variables that cannot fit into registers, like arrays or other structures.
- The **Frame Pointer** (FP, or X29) points to the first doubleword of the frame, which can be considered the bottom of the stack.
	- The stack is adjusted to make room for all saved regs and local vars
	- Referencing variables saved at the bottom of the stack is easier when the static Frame Pointer is used as the base address
		- This is a 'syntactic sugar'; all local variables could be referenced using the stack pointer and some arithmetic
		- This means that whenever the stack is pushed down at the beginning of a procedure, the frame pointer should first be pushed down to the current value of the stack pointer. It should then be restored as the stack pointer is restored. 
			- THIS IS UP TO THE PROGRAMMER
	- If there are no local variables that must be saved to the stack during a procedure, the compiler will typically save time by *not* setting and restoring the frame pointer
## What If A Procedure Uses >8 Arguments?
- The LEGv8 convention is to place the extra parameters onto the stack below the frame pointer
	- The procedure then expects the first eight parameters to be in registers X0 through X7 and the rest in memory, addressable via the frame pointer
	- This procedure may push the stack pointer downwards for its own local variables, but it will not modify the frame pointer
- The steps for calling a procedure with >8 arguments is as follows:
	- The caller stores the frame pointer onto the stack
	- Move the frame pointer to the stack pointer.
	- Push the extra arguments onto the stack.
	- Restore stack and frame pointers upon return
# The Heap and Heap Allocation
## LEGv8 Memory Allocation
 - The stack starts at the high end of memory and grows down
 - The first part of the low end of memory is reserved, followed by the **text** section, which houses the machine code to execute
 - Above the code in the text section is the **static data segment**, where static global variables are stored.
 - Although arrays and other fixed length structures can live in the static data segment, other more complex structures like linked lists tend to grow and shrink during their lifetime. The segment for such structures is called the **heap,** and it is placed next in memory
	 - Note that this allocation allows the stack and heap to grow into each other, which allows for the most efficient use of memory
	 - This can also allow for collisions like stack and heap overflow

For class #comporg