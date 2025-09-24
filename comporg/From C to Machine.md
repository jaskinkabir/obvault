Continues [[LEGv8 Procedure Calling]]

# Producing an Object Module
- The compiler translates the program into assembly
- The assembler translates this into machine instructions
- This software provides the following information for building a complete program
	- Header: Described contents of object module
	- Text segment: translated instructions
	- Static data segment: Data allocated for the life of the program
	- Relocation info: For contents that depend on absolute memory location of loaded program
	- Symbol table: Global definitions and external references
	- Debug info: For associating instructions with source code
# Linking Object Modules

# C Sort Example
```c
void swap(int v[], int k) {
int temp;
temp = v[k];
v[k] = v[k+1];
v[k+1] = temp;
} 
```
```c
// V* is in X0
// K is in X1
swap: LSL X9, X1, #3 // X9 = k*3
	  ADD X9, X9, X0 // X9 = X9 + X0
	  LDUR X10, [X9, #0] // X10 = v[k]
	  LDUR X11, [X9, #8] // X11 = v[k+1]
	  STUR X11, [X9, #0] // v[k] = v[k+1]
	  STUR X10, [X9, #8] // v[k+1] = v[k]
	  BR LR
```
For class #comporg