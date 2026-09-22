# Chip Multiprocessor Programming Models
- System Partitioning
	- Multiprogramming workloads, server consolidation
- Thread-level Speculation
	- Automatic loop-based parallelism
	- Assign a thread to each iteration of the loop
	- Hardware can detect dependency violations and roll back when needed
- Transactional Memory
	- Speculative access to shared memory without locks
	- Hardware detects non-atomic access, rolls back when needed
# Hardware Transactional Memory (TM)
- Allows a group of statements (memory ops) to be **atomic** and **serializable** without using locks
- *Atomic*: Either <u>all</u> ops are performed (and become visible) or <u>none</u> of them. A transaction is **committed** if its memory ops are performed
- *Serializable:* Global view of memory is consistent with ordering <u>all</u> transaction ops <u>as a group</u> in an interleaved serial execution of the program
# RGB Histogram Example
- ![[Pasted image 20260504153754.png]]
## Serial Code
![[Pasted image 20260504153838.png]]
- Read/write conflicts on elements of the histograms
## Coarse-grained lock
![[Pasted image 20260504153930.png]]
- Serializes the entire program, no parallelism at all
## Per-histogram lock
![[Pasted image 20260504153947.png]]
- Additional lock/unlock overhead
- But different elements of the red array should be writeable at the same time, however this locking scheme doesn't allow that
## Fine-grained lock
![[Pasted image 20260504154053.png]]
- Bigger storage overhead but more parallelism
## Coarse-grained Transaction
- ![[Pasted image 20260504154220.png]]
- ![[Pasted image 20260504154259.png]]
- Two threads write to different indices of the blue and red arrays, but the same green array. The operation fails
- If one operation fails all operations must fail so both threads roll back the changes to the other two arrays when they didn't actually need to
- Too many conflicts leads to many rollbacks and re-executions
	- Can be worse than the coarse grained lock even
## Fine-grained Transaction
![[Pasted image 20260504154445.png]]
- Only have to redo conflicting transactions

# Benefits of TM
- No need to allocate lock variables, or decide which data should be protected by each lock. Should simplify programming
- Composable: transactions can be nested
- Avoids problems associated with locks
	- Priority inversion: low-priority task blocks a high-priority tasks that needs the same lock
	- Convoying: holder of lock gets delayed/de-scheduled/thread-switched, blocks all other tasks
	- Deadlock: all tasks must acquire locks in the same order, but sometimes the set of locks is not known in advance
		- T1 has A and needs B, T2 has B and needs A
# Requirements of TM
- Must keep track of every variable read or written during transaction
	- These are known as the *read set* and *write set*
	- If I have read and another thread wrote, then they aren't atomic
- The written data is speculative, success is unknown
- The new version cannot be made visible to other threads until the transaction **commits**
	- This is called **version management**
- If two transactions access the same variable, and at least one access is a write, this is a conflict
	- The process is called **conflict detection**
- Once a conflict is detected, it must be resolved
	- This is called **conflict management**
	- Includes aborting or delaying a transaction
# TM Implementation
- TM can be implemented in software STM or hardware HTM
- STM generally introduces a lot of overhead, and is not competitive in performance with lock-based approaches
- There are efficient implementations of lock-free data structures
# Hardware TM
- Much lower performance overhead than STM
- Mostly transparent to software
- Significant h/w complexity
- Amount of work per transaction limited by buffering capacity
Requires:
1. Instructions to mark beginning/end of transaction
	1. Intel XBEGIN XEND
	2. Requires CPU support,
	3. May require fence before XBEGIN to make sure prior operations are not part of the transaction
	4. The signal is sent to the cache to trigger transactional mode and trigger the commit
2. Tracking of read and write sets
	1. ![[Pasted image 20260504155639.png]]
	2. Bits to mark cache lines that have been read or witten during current transaction
	3. Usually have abulk clear capability to reset when transaction ends
	4. In many implementations, speculative state is stored in the L1 cache
	5. If a speculative block is evicted, the transaction must abort
3. Buffering for speculative data from writes
4. Mechanism for detecting conflict
	1. Cache coherence protocol
	2. Invalidation for a line in the read set = conflict
	3. Intervention/invalidation for a line in the write set = conflict
	4. May be **eager** (at the time of the remote request)
	5. May be **lazy** (only notified when commit happens)
5. Policy for responding to a conflict
	1. Requester wins: Receiver of conflicting request provides data and aborts
	2. Requester stalls: Receiver either defers (buffers request) or NACKs (requester retires)
		1. Requester only aborts if there is possibility of deadlock
	3. Committer wins: compatible with lazy detection
6. Mechanism for committing transactional data
	1. If speculative data is in cache, clear R/W (speculative) bits
	2. Later requests for owned data will be handled as usual and become visible
	3. More complicated in lazy scheme
7. Mechanism for aborting transaction, rolling back execution to restart
	1. Invalidate all W lines after clearing bits
	2. On retry, new transaction will load non-speculative data as needed
	3. Clear R/W bits
	4. Signal ABORT to processor, which must rollback execution (similar to mispredicted branch)
## Speculative Lock Elision (SLE)
- Observation: Concurrent accesses to a shared data structure might not conflict, and lock/unlock is not in fact needed
	- Example: ![[Pasted image 20260504160421.png]]
		- If the branch is not taken, the lock is unneeded
	- ![[Pasted image 20260504160507.png]]
		- Different threads accessing different parts of a shared data structure don't need to be serialized
### Silent Store
![[Pasted image 20260504160828.png]]
- Observation: Stores to acquire a lock(=1) and to release the lock(=0), as a pair, cancel each other out and have no effect. This is known as a **Silent Store Pair**
- If nobody reads the lock in between lock and unlock, the lock didn't do anything
- We should remove silent stores
### Speculative Execution
![[Pasted image 20260504160805.png]]
- Don't bother locking and unlocking (stores), just execute the critical code in speculative mode
- If there are no conflicts, the operation *appeared* atomic
- Otherwise, roll back
### SLE Algorithm
1. If a candidate load (LL) is followed by a store (SC) to the same address, **predict** that a second store will follow, restoring address to its original value
2. Predict the memory ops in the region between will occur atomically and **elide** (remove) the store
3. Execute speculatively, and buffer results
	1. NOTE: Dirty blocks must be written to memory before writing speculative data
4. If hardware cannot provide atomicity, trigger **misspeculation**, recover and **explicitly acquire the lock**
5. If second store (step 1) is seen, atomicity was not violated. **Elide the store, commit state**, and exit speculative mode
![[Pasted image 20260504161432.png]]
454## Transactional Lock Removal (TLR)
- SLE works well when there is little/no contention within the critical region
- When there is contention, threads acquire the lock as usual
- ![[Pasted image 20260504162005.png]]
- TLR adds **Timestamp-based Conflict Resolution** to allow transaction to continue when conflicts occur
- ![[Pasted image 20260504162059.png]]
- Counter is incremented (locally) for each transaction
- Lower timestamp has priority
- When abort/restart, counter does not change – it eventually becomes the lowest
- SLE is requester wins, if somebody else writes to data then abort
- TLR instead uses this priority scheme
- Example
	- ![[Pasted image 20260504162255.png]]
		- P1 writes to A
		- P2 writes to B and invalidates P1's A, so A must restart
		- P1 has a write miss to A as P2 writes to A
		- P2 must restart when it sees P1's invalidation
		- They both continually restart because neither can ever complete the critical section
	- ![[Pasted image 20260504162541.png]]
		- Processor 1 has TS1 < TS2 of processor 2
		- When P1 sends the ReadX for B to P2, P2 realizes there is a conflicting request with a lower timestamp
		- P2 loses, it must provide data and retry
		- When B's ReadX for A reaches P1, it sees the lower priority and instead buffers/defers the request until it finishes the transaction
		- Then P1 will service B's ReadX
### TLR Drift
- One processor isn't doing a lot of transactional code, its counter stays low
- Other processors are doing transactions and their counters drift higher
- The first processor has an unfair advantage when it eventually does do transactions
- To avoid drift, whenever a transaction is committed, set counter to highest value across the system instead of just incrementing
### Deadlock
- With more than two processors, cyclic dependencies can create deadlock
- ![[Pasted image 20260504163426.png]]
- At t1, P1 sends ReadX to A. Cache directory marks P1 as A's owner, sends FlushX to P0. P0 has higher priority so it defers this request
- At t2, P2 sends ReadX to B. Directory marks P2 as B's owner, sends FlushX to P1. P1 has higher priority than P2 so it defers
- At t3, P0 sends ReadX to B. Cache marks P0 as B's new owner, sends FlushX to P2.
	- P2 has lower priority than P0 so it should send data to P0
	- But it doesn't have the data, P2 is waiting on P1 to service its request
	- But P1 is still waiting for P0 to service P1's  request
	- P0 needs P2's data
	- Everyone is waiting on everyone; deadlock
- For block A, P0 is aware of P1, but P1 is not aware of P0
- For block B, P1 is aware of P2, but P2 is not aware of P1
#### Marker and Probe messages
![[Pasted image 20260504164242.png]]
- When P1 gets the lower priority request from P2 for B, it will send a **marker** (green) message to say it is deferring
- When P2 receives P0's request, P2 sends a **probe** (blue) to P1 (with P0's timestamp)
- When P1 receives probe with lower timestamp, it aborts and releases (orange) B to P2, breaking the deadlock
## Intel ISA
- Added XACQUIRE and XRELEASE prefixes for store instructions
	- Allows speculative exec between stores
- **Restricted Transactional Memory (RTM)**
	- XBEGIN, XEND, XABORT instructions
	- XBEGIN provides address of fallback routine to recover from abortion
- Commercial support for HTM is **best-effort**
- Programmer must provide specific fallback code, which can inspect reason for abortion
- From 2012-2020, HLE or Hardware Lock Elision was in intel processors
- RTM support is only in specific processors

For class #parallel-arch