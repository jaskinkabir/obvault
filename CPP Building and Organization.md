- Order
	- Preprocessor
		- Looks at header files and adds a symbol to each reference to the objects and waits until the implementation file is built to implement them
	- Compiler
	- Assembler
	- Linker
	- Executable
- If there's some fucked up linker mistake include the following to protect from that
	- 

```C++
 #ifndef CLASSNAME_H
 #define CLASSNAME_H

```
```