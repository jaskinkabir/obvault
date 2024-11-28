# Make
- A tool that directs compilation of applications
	- Make: Determines which source files need to be recompiled
	- Makefile is a file that holds the rules for compiling
		- The makefile contains a set relation on the set of all files in the program
			- Ex: Antireflexive, antisymmetric, transitive relation
## Makefile
- An explicit rule consists of a target, pre-reqs, and a sequence of commands
	- An implicit rule omits the commands
	- Directives give special rules
```
util.o: util.c ../include/util.h config.h
		gcc -c -g util.c
```
```
main: main.o util.o
```

For class #research-tools