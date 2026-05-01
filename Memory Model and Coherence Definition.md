Continues [[Directory Coherence Ordering and Correctness]]
Continued by [[Memory Consistency]]
# Mem Model Definition
- Governs legal interleaving of mem accesses in shmem multiprocessors
- Determines order in which accesses by one thread can be observed by other threads
- Part of ISA spec
- Includes cache coherence and memory consistency
- Provide simple rules governing the behavior of memory
	- Compromise between hardware efficiency and programmability
	- Isolates programmers from the complexities of hardware
	- Guarantees backwards compatibility

# Load-Store Ordering
- Loads and stores can sometimes arrive at memory in different orders
- A **Store Buffer** allows processor to continue while a store completes
	- Value in store buffer may be forwarded to satisfy a load
	- This is called store-to-load forwarding
# Memory Coherence for Uniprocessors
- Single threaded: match the programmers expectation
- A load must return the value of the latest store with the same address in thread order
- Thread order is the order in which instructions are fetched/decoded/executed
- Enforcing thread order requires cooperation between the processor and memory 
- **Processor** may issue memory accesses out of order but memory dependencies are enforced and accesses to the same address appear to be executed in thread order
- **Memory** may handle multiple requests at the same time but the value returned by each load must be the latest value stored in thread order
## Examples
- Processor
	- Load value forwarded from store buffer
	- Multiple stores to the same address can be merged in the SB
- Memory System
	- Load hit can be satisfied on a pending store miss
	- Multiple stores can be merged in a pending miss
- We will always assume intra-thread ordering is enforced
# Multiprocessor Coherence
- For multiprocessors there is no single multi thread ordering
	- They should be able to do stuff at the same time in whatever order
- ![[Pasted image 20260428180819.png]]
	- For a write-through cache, event 4 is coherent (will get 1) but event 5 is not
	- For a write-back cache, neither event will be coherent
		- P3 won't write 1 back to X in main mem
- Coherence is maintained if
	- There is only one copy of data in the system Or
	- There are multiple copies but all have the same value
- Coherence does not require that all copies are the same at all times
- If software doesn't see multiple values, it doesn't matter. Coherence is only enforced from the perspective of correctness of the program
	- The system is coherent as long as P1 doesn't load X
	- The system needs to only **Appear** coherent
## Overlapping Accesses
- The **Lifetime** of a memory access is the interval between the time of instruction fetch and the time at which all activities for the instruction have completed in the entire system
- Suppose instructions 3 4 and 5 were initiated at the same instant
- Coherence allows P1 to see X=0 and P2 to see X=0
- The point is **Coherence Allows Race Conditions**
	- To prevent them is a problem of correctness
	- Responsibility of the programmer
# Strict Coherence
- A memory system is **Strictly Coherent** if the value returned on a load is always the value of the latest store instruction with the same address
- Difficult to enforce in a multiprocessor because the order of loads and stores in multiple threads is not defined
- A global temporal ordering of all stores to the same address must be imposed
## Enforcement
1. Allow only one copy of data (not practical)
2. Ensure stores do not overlap with loads (not practical)
3. Stores can be propagated to all copies in the system instantaneously
	1. This known as **Store Atomicity**
	2. We can create the illusion that this is true
4. Rely on synchronization primitives to force the separation of accesses to the same location
## Store Atomicity
- Stores are **Atomic** if different threads can never observe more than one value of the same memory location at the same time
- Only one value is available to read at any time
- Therefore values are ordered in real time
### Bus-Based Store Atomicity
- Processors access caches locally in parallel
- When an access must leave the cache, it is performed atomically in memory and across all caches
- A load or store from memory will hold the bus until it is done
- ![[Pasted image 20260428182709.png]]
	- APT: Atomic Protocol Transaction
	- On a split transaction bus, only one coherence action per address at any time
# Performed Vs Globally Performed ST/LD
- A store is **Performed** with respect to thread i at the point in time when a load from thread i cannot return a value prior to the store
- A store is **Globally Performed** once it is performed with respect to all threads
- A load is **Performed** at the point in time when its value is bound and cannot be recalled
	- When the value is in a register in the processor
- A load is **Globally Performed** when it is performed and the store providing the value is also globally performed
	- Everybody else also has that value
- A system is **Store Atomic if**
	- A global order to each address is enforced and
	- All loads must be globally performed
- ![[Pasted image 20260428183724.png]]
	- If a load's lifetime overlaps two globally performed stored values, either value satisfies store atomicity

# Plain Coherence
## Store Atomicity may not be necessary
- Store Atomicity does not allow forwarding from the store buffer
	- The stores are not yet globally performed
- Is there a less restrictive definition of coherence that allows for such optimizations?
## Definition
- A system is **(Plain) Coherent** IFF for <u>every execution</u>, it is possible to construct some <u>serial order</u> of all memory operations to each memory location such that
	- The memory operations of each thread to the location are in **thread order** and
	- The value returned by a load is the value of the *latest store* to the same location in the **serial order**
- This means different caches may have different values at a particular instant
- Coherence only enforces ordering of writes on a per-address basis
	- ![[Pasted image 20260428193409.png]]
- ![[Pasted image 20260428192331.png]]
# Proving Coherence
- Need to construct a serial ordering of all memory accesses to each memory location for *all possible executions*
	- An execution meaning a possible ordering of operations
- For a single execution, this is NP-complete
- For all executions, it's incomputable; there are infinite possible executions
- Instead, we design a system with hardware serialization points that constrain possible executions such that a serial order can be constructed
	- Constrain the number of possible executions to a finite number
## Example: Forwarding Store Buffers
![[Pasted image 20260428194618.png]]
- At t3 there are 3 different values of A stored in different store buffers
- This violates store atomicity
### Constructing Serial Order
1. List all GP accesses in order
2. Replace all WB with the thread-local loads and stores serviced by that store-buffer entry
	1. The WB serves as an insertion of all those accesses into the global order
	2. That's when the accesses become globally visible
	3. This is where the thread's known history of the value is committed to the global order
- Temporal order of values is a0,a1...a6
- Coherence order: a0,a1,a4,a3,a5,a2,a6
- Breakdown of how coherence order was constructed

| **Time** | **Committing Processor** | **Local Order** | **Global Order**         |
| -------- | ------------------------ | --------------- | ------------------------ |
| t0       | na                       | a0              | a0                       |
| t10      | 1                        | a0,a1,a4        | a0,a1,a4                 |
| t13      | 2                        | a3,a5           | a0,a1,a4,a3,a5           |
| t16      | 3                        | a0,a2           | a0,a1,a4,a3,a5,a2        |
| t22      | 2                        | a3,a5,a2,a6     | **a0,a1,a4,a3,a5,a2,a6** |
- Threads:
	- T1 observes a1, a4, a5, a2
		- Skips a3
	- T2 observes a3, a5, a2, a6
		- Skips a0, a1
	- T3 observes a0, a2
		- skips a1,a4,a3,a5,a6
- Notice that all threads observe values according to the global order
- No threads violate it, they can only skip certain values/steps in the order
# Generalizations
- **Privacy Principle:** A thread may load and use its own latest values before they propagate to other threads without violating coherence.
	- In lockup free caches, a cache line may be allocated on a store miss while the store miss is pending. Values can be filed by local stores and used by local loads
	- Threads sharing the same core or cores sharing the same cache line in a multithreaded cmp can read each other's values in the cache even if the values are pending (not Globally Performed). 
	- Clusters of cores or multicores in hierarchical cache systems may share non-GP values in shared buffers or in shared lockup-free caches at multiple levels of the hierarchy
- In cc-NUMAs with invalidate protocols, a thread may modify a block when it receives it and use its own values and share them with other local *threads*, even if the coherence transaction is not closed at the directory.
![[Pasted image 20260430164251.png]]
- The gray area shows difference between plain coherence and store atomicity
- T0 can perform the write locally at t2 and use it
# Summary
## Coherence
- All stores must be globally ordered
- The system needs a serialization point
- Each thread has a store pipeline of all pending stores
- Can read values from that pipeline even if they are not globally performed
	- Return value from nearest coherent store
	- In a store atomic system, the core would have to wait for global performance before the value can be used
## Importance of Coherence
- Facilitates implementation of memory consistency
- Coherence protocol takes care of ordering accesses to each address individually
- If computation stops (eg context switch) coherence makes sure memory state settles by waiting for all memory ops to be globally performed
## Plain Coherence and Multiple Addresses
- Plain coherence is not composable with other orderings that may be imposed on accesses to different memory addresses
- Plain coherence only guarantees global order on a per-address basis
![[Pasted image 20260501171948.png]]
- This example is not coherent if these other orderings are imposed
	- Loads within a thread must be globally ordered
	- Calculating the address (A) depends on the value loaded by $L^{2}(B)$
	- Programmer inserts a barrier between the two loads in both threads
```c
initial: A = flag = 0;
Thread T1:  Thread T2:
A = 1;      
flag = 1;   while (flag = 0);
            print(A);
```
- If T2 prints "0", the system is coherent
- There is no temporal ordering between the store of A vs flag.
	- T2 can observe `flag = 1` and then observe `A=0`
	- The global order for each address is preserved: 0->1
- But execution is wrong from the programmer's perspective; it violates correctness.
```c
initial: A = B = 0;
Thread T1:  Thread T2:
A = 1;      print(B);
B = 1;      print(A);
```
- If T2 prints "1 0", the system is coherent
- T2 observes B=1, then A=0. Global order per address is coherent
```c
initial: A = B = 0;
Thread T1:      Thread T2:
A = 1;          B = 1;
while (B = 1);  while (A = 1);    
<critical>       <critical>
A = 0;          B = 0;
```
- Can the two critical sections execute at the same time? 
	- For T1
		- A: 0→1→0
		- B: 0(→1→0)
	- For T2
		- A: 0(→1→0)
		- B: 0→1→0
	- The two global orders are coherent
- YES, this satisfies plain coherence

For class #parallel-arch