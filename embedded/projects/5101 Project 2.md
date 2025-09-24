Jaskin Kabir 801186717
Uses [[The Memory Hierarchy]]
Uses [[Structs In Memory]]
![[Pasted image 20250913181124.png]]
![[Pasted image 20250913180851.png]]

The unused memory address 20007FD0 is likely padding. The addresses 20007FFC-F8, containing main's previous stack pointer and return address, are also unused because main should never return. The addresses 2007FEC-E8 could also be padding, but it is also possible that one of them was preallocated by the compiler to store the result of debugFunction.

For class #embedded/projects