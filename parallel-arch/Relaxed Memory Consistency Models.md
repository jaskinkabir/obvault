Continues [[Sequential Consistency]]
# Overview
- Consistency models that have weaker hardware restrictions than SC are called **relaxed**
- The programmer and compiler must know what is and isn't possible, and to explicitly impose stricter ordering when necessary

# Hardware Ordering
- Within a thread, hardware specifies the order in which operations must be globally performed
- ![[Pasted image 20260503182336.png]]
- SC requires ordering among all memory ops
# SC Ordering
- Load-load and load-store
	- Load stalls pipeline, and all following loads/stores are stalled
- Store-load: 
	- Loads can return values from the store pipeline
	- If not in the pipeline, load must wait for store to be GP
- Store-store:
	- Stores must be executed in FIFO order
	- No combining, unless there is no intervening store
	- If T1 says X=10 then X=30, they can be combined into X=30
	- If T2 says X=20 in between, X=30 cannot be combined into X=10, because it would violate SC. The order has to be 10,20,30
# Store-Load Relaxation
- Allow a load to bypass a store to a different address
- Allows effective use of store buffers
- If a store misses in cache, following loads (to a different address) can proceed, whether they hit or miss
- This violates SC, but this is an ok compromise because it prevents the stall
![[Pasted image 20260503183415.png]]
- We removed the thread order arrows from the store to the load, so there is no loop
- This relaxation violates thread order and therefore SC

## Without Forwarding
- If load-forwarding within the store pipeline is not allowed, then every load returns a GP value. The system is store-atomic
- This prohibits localized memory optimizations
	- No forwarding in store buffer
	- In lockup-free cache, no read hits during pending write miss (same or different threads)
## With Forwarding: Total Store Ordering (TSO)
- ![[Pasted image 20260503192703.png]]
- The store and load to the same address can happen globally in any order
- Therefore, there is no ordering rule between the store and load, so the loop is removed
# Relaxed Memory Ordering
- Only enforces intra-thread coherence; no ordering among different threads
- Provides MEMBAR instruction to allow software to specify ordering
- MEMBAR is a fence that requires prior memory operations to e completed
- The argument specifies which of the four orderings to enforce
	- load-load
	- load-store
	- store-load
	- store-store
- Inserting MEMBAR 1111 between every pair of memory operations would enforce SC
![[Pasted image 20260503193725.png]]
- Remember that TSO enforces all 4 orderings except store-load
- T2 must enforce load-store ordering
- T3 must enforce load-load ordering
- MEMBAR is a local intra-thread ordering operation, not the same as a barrier synchronization (global, inter-thread)
# Relaxed Consistency based on explicit synchronization
- If variables are read and written by multiple threads, they should be in critical sections or ordered using barriers
- Programmer can label **synchronization variables**, and accesses to those memory locations can be treated differently by hardware
- The hardware can then enforce correct interleaving of synchronization accesses, rather than all accesses
## Producer-Consumer Example
- ![[Pasted image 20260503200627.png]]
- T2 will wait for A=1 to perform before issuing FLAG=1
- T1 cannot observe FLAG == 1 without loading 1 for A
- Access to the synch variable becomes a fence

## Mutex Example
![[Pasted image 20260503201100.png]]
- Suppose code requires SC to be correct
- SC values of R3 are 0, 1, 3
- RMO would allow B=2 to happen before A=1
	- This means the execution could be $S^{1}(B)2\to \text{all of T2}\to S^{1}(A)1$
	- This would allow R3=2
- We can instead declare a lock variable so that only one thread can read or write to A and B at a time
- ![[Pasted image 20260503201353.png]]
- The critical section enforces serial ordering of T1's stores and T2's loads; allowed values are 0,3
- Within the critical section, ordering is relaxed. The fence is inserted around accesses to L
## Synchronization-based ordering
![[Pasted image 20260503201642.png]]
- In non-critical code, there are only private and read-only variables, so ordering doesn't matter
## Globally-performed Lock/Unlock
- Atomic operations: Read-Modify-Write (RMW) is globally performed when both the load and store components are globally performed
- The lock is not acquired until the RMW is globally performed
- Unlock is no longer a normal store; it must wait until earlier operations within the critical section have been performed
# Weak-Ordering
- ![[Pasted image 20260503202710.png]]
- In weak ordering, synchronization variables must be marked, and accesses to those variables are ordered with respect to each other, and with respect to any operation on other variables
- No ordering is imposed on non-synch variables
# Release Consistency
![[Pasted image 20260503202945.png]]
- A refinement of weak ordering in which ordering is related to the type of synchronization action
- Two types of synchronization
	- Ops in a critical section must wait for the lock to be acquired
	- Ops in a critical section must complete before lock can be released
- In Weak Ordering, fences are two-sided (past and future)
- In RC, the fences are one-sided (past OR future)
# The Difference
![[Pasted image 20260503203153.png]]
- Thread 2 of previous example
- In WO (a), the lock and unlock are both fences.
- In RC, only the unlock enforces order.
- This can allow for more concurrency
# Example ISAs
- Intel 64
	- TSO
	- Total order on locked instructions (eg RMW)
	- Ifence, sfence mfence
- ARM v8-A
	- Only intra-thread dependencies
	- Memory barrier (DMB) with lots of options
	- Very flexible for explicit ordering
	- ARM can do release consistency
- RISC-V
	- RVWMO (RISC-V Weak Memory Ordering)
	- Only intra-thread dependencies
	- FENCE instruction, similar to MEMBAR
# Memory Consistency and Software
- OpenMP
	- Assumes relaxed consistency
	- Enforces ordering at synchronization:
		- `Critical`, `barrier` `atomic`,` parallel region`
	- Provides `flush` for explicit consistency
- C++
	- `std::atomic` library
	- Ordering options
		- Default is relaxed
		- Can enforce sequential, acquire, or release consistency
- 

For class #parallel-arch