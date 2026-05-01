Continues [[Memory Model and Coherence Definition]]
# Sequential Consistency
- Accesses from different threads will be interleaved atomically in thread order
- A consistency policy that is meant to map closely to the programmer's intuition
- 
## Formal Definition
- A system is *Sequentially Consistent* if the result of **any execution** is the same as if the memory operations of all threads were executed *in some sequential order* and the operations of each thread appear in thread order
- Sufficient conditions:
	- A global order of stores to the same address is enforced
	- A thread may not issue an access to memory until *all its previous accesses* have been **globally performed**
## Proof that an Execution is SC
- Draw an execution graph with directed edges according to the ordering rules. If cycle, then SC is violated.

For class #parallel-arch