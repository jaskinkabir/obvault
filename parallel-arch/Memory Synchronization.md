Continues [[Sequential Consistency]]
# Types
## Mutual Exclusion
- Only one thread may execute code
- Critical region, lock, monitor, synchronized method, ...
- ![[Pasted image 20260502154154.png]]
## Barrier
- Multiple threads must reach the same synchronization point before any may continue
- Barrier, join, etc
- ![[Pasted image 20260502155138.png]]

## Producer-Consumer
- One thread must write before other threads read
- Post-wait, events, flags, semaphores
- ![[Pasted image 20260502155257.png]]
- ![[Pasted image 20260502155305.png]]
- Is this code guaranteed to be correct?
	- Meaning will this print 5?
- ![[Pasted image 20260502155337.png]]
- By **sequential consistency**, this is guaranteed to be correct
	- Assume `datum` was set to 0 at some point before the first instruction
	- The only execution that allows a print of 0 would be 
		- D is datum, R is datumIsReady
		- $S^{x}(D)0\to S^{x}(R)0\to S^{0}(R)1 \to L^{1}(R)1\to L^{1}(D)0\to S^{0}(D)5$
		- Aka S2, S3, S4, S1
		- S2 happening before S1 violates thread order and therefore SC
# Definition of Atomicity
A set of actions is **Atomic** if 
1. Either all actions are performed, or none
2. Only one processor can perform the sequence at a time; operations by multiple processors must be serialized
## Atomic Instructions
- Many processors have atomic instructions, like
	- test-and-set
	- fetch-and-incr
	- fetch-and-op
	- exchange
	- compare-and-swap
# Lock Implementation
- Can we enforce mutex with just loads and stores?
## Metrics for Evaluation
- Uncondented acquisition latency
- Traffic
	- When acquiring a free lock
	- When waiting to require a contested lock
	- When releasing a lock
- Fairness and starvation-freedom
- Storage
## Naive
- ![[Pasted image 20260502161840.png]]
- If lockvar is 1, someone has the lock so wait
- If 0, the lockvar is available. Set it to 1 to acquire it
- ![[Pasted image 20260502162057.png]]
- This doesn't work
	- Both threads read 0 at the same time
	- Both threads 'acquire' the lock by writing 1 at the same time
- Note that this is not a memory consistency issue; there is only one variable. This is managed by the coherence protocol
- We need an **atomic** read-modify-write operation, so no other thread can come in between these 3 actions
## Test-and-set Lock
- The T&S instruction reads (tests) and sets the value of a memory location atomically
- ![[Pasted image 20260502170529.png]]
- Reads and sets lockvar to 1 atomically
- If the loaded value is 1, the lock is held by someone else
- If 0, the lock was free and it was atomically set to 1 (acquired)
- Only one thread will succeed
### Evaluation
![[Pasted image 20260502171134.png]]
- The **Uncontended Lock Acquisition Latency** is low, essentially the same as a write
- **Bus Traffic** is high when contending for the lock
	- Thread 1 is constantly putting ReadX's onto the bus and consuming
- **Fairness:** All processors have an equal chance, but starvation can occur
	- If there is a cc-NUMA kind of noc architecture, the physically closest PEs to the home node of the lock variable is more likely to get the lock
	- It is possible for a processor, especially a far one, to never receive the lock because another processor can always take it before they can get it
- **Storage:** One variable, constant size
## Test-and-T&S Lock (TTS)
- Read the lock variable, then only attempt T&S if lock appears available
	- As a processor spins waiting to acquire the lock, the reads to the lock variable will all hit
		- No bus traffic while spinning
	- Then, when the holder of the lock writes 0, it will invalidate all the sharers
	- The next read to the lockvar will be a miss, the processor will issue a BusRd
	- Every other sharer will do the same
	- Now every thread will issue a T&S, but only one will get it first. This thread will see 0 in its test register. Next every other sharer will see 1 in their test registers and fall back to the first phase
### Evaluation
- The **Uncontended Lock Acquisition Latency** is still low, but a little higher than T&S
	- In T&S an acquisition is 2 instructions (T&S, cmp)
	- In T&T&S, it is 4 (LD, cmp, T&S, cmp) 
- **Bus Traffic** is low when waiting for lock, bursty when lock is released
	- A bunch of load misses will happen
- **Fairness:** Same as T&S
- **Storage:** One variable, constant size
## Software Locking
### Ticket Lock
- To implement a fair lock, each thread will 'take a number' and wait for its turn
- Two global variables, now serving and next ticket
- To acquire, atomically fetch and increment next ticket, then spin until now serving is equal to this ticket
- To release, increment now serving
	- Doesn't *have* to be atomic
	- But the lock holder may have the now serving variable in 
![[Pasted image 20260502202045.png]]
#### Evaluation
- The **Uncontended Lock Acquisition Latency** is higher than LL/SC, but still low – just a single atomic operation + one load
- **Bus Traffic** is similar to TTS
	- While waiting, spin on local cache reads
	- Burst of traffic on release, all waiters invalidated followed by BusRd
- **Fairness:** Order of f&inc will determine order of lock acquisition. No starvation is possible
- **Storage:** Two variables, constant space
### Array-Based Queuing Lock
- Once thread has received its ticket number, use it as an index into an array of 0/1 values
- When it sees 1, the lock has been required.
- To release, set the current array element to 0 and the next array element to 1
- Only <u>one</u> reader will be invalidated
#### Implementation
![[Pasted image 20260502202712.png]]


## Lock Design Consideration
- Parallel code should be written to avoid contention as much as possible. It creates serialization and loses parallelism
- Therefore, contention on locks is not always an important design consideration
- If there are multiple threads on a core, the OS/scheduler may force a thread switch when the thread fails to acquire the lock. In this case, the thread is not spinning on the T&S so the bus contention isn't much of an issue
- In some cases, the overhead of a TTS lock isn't necessary
### TTS With Delay
- ![[Pasted image 20260502173918.png]]
- TTS can scale significantly better than T&S
- But the bursts in bus traffic on release can slow down execution
- Instead, have threads backoff for some time when they fail to acquire the lock
- ![[Pasted image 20260502174208.png]]
![[Pasted image 20260502202824.png]]
# How Are Atomic Instructions Implemented?
1. Instruction is treated as a write, and cache fetches/upgrades put the block in E/M state
2. Protocol prevents other accesses while instruction is in progress
	1. Could lock the bus, preventing others from requesting
		1. Even on other lines
		2. Unnecessarily serializes transactions
	2. Owner (E/M) can defer responding to other requests until modify operation is complete, or send a NACK to require a retry
- Lock The Bus
	- Requires specific hardware signal on the bus
	- Only supports one atomic for all PEs
	- Doesn't scale to non-bus interconnects
- Defer/NACK incoming requests
	- Requires buffering and complicates control
	- Generates NACK traffic
- For RISC architectures, having atomic instructions defeats the philosophy of RISC and complicates pipelines and optimizations gained from reducing the instruction complexity
## LL/SC
- We can instead provide the illusion of atomicity by issuing a pair of non-atomic instructions
- LL/SC is a general (non-bus) implementation of atomic operations
- LL/SC is a pair of non-atomic operations that provide atomic T&S
- **Load-Linked or Load-Locked (LL)**
	- AKA Load-reserved in RISC-V (LR)
	- Loads value into cache and into register
	- Also loads address into another special register (linked register)
	- If an invalidation arrives for the same address, clear the linked register
- **Store-Conditional (SC)**
	- If linked register still matches the address, perform the store (propagated to other caches)
	- If linked register does not match, cancel the store
- **Key Observation**
	- If the processor can load and store with no intervening stores, then the load/store pair appears to have been executed atomically
	- Therefore, if the LL/SC succeeds, it is seen as atomic
	- If it fails, then the store doesn't happen and the rest of the system does not see the new value.
		- The cancelled write does not propagate and the processor can retry
### Implementing T&S with LL/SC
![[Pasted image 20260502181250.png]]
- The T&S instruction can be replaced with this procedure
- Notice the loop
- An atomic sequence can either be performed or not. Therefore, the T&S procedure cannot return until the conditional store succeeds.
### LL/SC Lock
- ![[Pasted image 20260502181433.png]]
- Similar to TTS, but not exactly
- The burstiness is reduced
- Instead of everybody sending upgrade requests as soon as the unlock is observed, they will instead check if their link register has been cleared. Only if it has, will they send the write across the bus.
- Only one processor will send this write.
### LL/SC Other Atomics
- The instructions between the LL and SC are (somewhat) general, so it can be used to implement many atomic operations
- Try to keep only one instruction between LL and SC

| fetch-and-incr   | Ld X, store X+1                   |
| ---------------- | --------------------------------- |
| fetch-and-op     | Ld X, store X op Rx               |
| exchange         | Ld X, store Rx (swap values)      |
| compare-and-swap | If Rx==X, swap values of X and Ry |
#### Pseudo assembly examples

```
CAS:Add R2, R0, Ry // R2=Ry (save value)
	LL R1, X // R1=X
	BNE R1, Rx, Return // If Rx does not equal x return
	SC R2, X // X=R2
	BZ R2, CAS // If failure, retry
	ADD Ry, R0, R1 // Ry=R1
Return:
	// exit

SWP:ADD R2, R0, Rx // R2=Rx (save)
	LL R1, X // R1=X
	SC R2, X // X=R2(=Rx)
	BZ R2, SWP
	ADD Rx, R0, R1 // Rx=R1(=X)
```

- If an LL instruction reads block X, and X is evicted before the associated SC instruction, what happens?
	- Should the SC instruction succeed if X has not been written by another processor, and fail otherwise?
		- This could depend on the coherence protocol
		- If the line is evicted, the cache could stop tracking other processors' writes to it. The directory may stop sending invalidations
	- Instead, most architectures will make the SC instruction always fail in this case
	- Other loads should not happen in between LL and SC because it could cause an eviction or page fault
# Barrier Implementation
## Evaluation Metrics
- Latency
- Traffic
## Basic Implementation Strategy
1. Know how many threads are participating
2. Each thread atomically increments a counter when it reaches the barrier, then spins on a flag
3. When the last thread arrives (known by counter value), set the flag to allow others to continue

```c
int numArrived = 0;
mutex_lock barLock = 0;
int canGo = 0;


void barrier() {
	lock(&barLock); // Lock so only 1 thread can be first
	if (numArrived == 0) // I am first
		canGo = 0; // initialize flag for waiting
	numArrived++;
	int myCount = numArrived;
	unlock(&barLock);
	
	if (myCount < NUM_THREADS) while(!canGo);
	else { // I am last
		num_arrived = 0; // reset count
		canGo = 1; // release to waiters
	}
}
```
### Barrier Reuse Problem
- If the same barrier is reused, the implementation becomes incorrect
- A thread can re-enter the barrier after the canGo flag has been set, and then rewrite it to 0 before anyone else has seen it.
- Then nobody will be able to set the flag on the second barrier, so it will stall indefinitely
- ![[Pasted image 20260503173533.png]]
### Sense Reversal Barrier
- To solve this, we could require leaving threads to decrement the counter and wait for every thread to leave before exiting
	- This requires another critical section and potentially another counter, more latency, higher traffic
- We could change the value used by the flag
	- Wait for 0, then 1, then for 0
	- This is called **sense reversal**
```c
void barrier() {
    // Each thread gets its own persistent, private copy of this variable
    static thread_local int localSense = 0; 

    localSense = !localSense; // Toggle the private sense

    lock(&barLock);
    numArrived++;
    
    if (numArrived == NUM_THREADS) {
        numArrived = 0; 
        unlock(&barLock);
        globalSense = localSense; // Release all threads
    } 
    else {
        unlock(&barLock);
        while (globalSense != localSense); // Spin on private sense
    }
}
```
#### Performance
- Critical section
	- The critical section increments numArrived and checks for synchronization
	- In the worst case, all processors reach the barrier at the same time, which fully serializes the process
	- High traffic, depending on lock implementation
	- O(p)
- Incrementing counter
	- O(p) because it is part of the critical section
- Release
	- O(p) invalidations + reads
	- Burst of traffic on release
## Combining Tree Barrier
- Group of d threads participate in d-way barrier. Last thread to arrive moves to next level.
- At root, last thread to arrive notifies all threads
- Lower traffic and latency (scales with logP)

![[Pasted image 20260503180451.png]]
## Hardware Barrier
- Simplest: Global wired-AND signal – becomes 1 when all cores assert 1
- More scalable: Tree based network that combines barrier signals
- ![[Pasted image 20260503181241.png]]
- Expensive, only really for specialized systems

For class #parallel-arch