Continues [[Memory Model and Coherence Definition]]
Continued by [[Memory Model Comparison]]
Continued by [[Memory Synchronization]]
Continued by [[Relaxed Memory Consistency Models]]
# Sequential Consistency
- Accesses from different threads will be interleaved atomically in thread order
- A consistency policy that is meant to map closely to the programmer's intuition
- Some enforced global ordering of the way values change that is consistent with the interleaving of those thread-ordered accesses
## Formal Definition
- A system is *Sequentially Consistent* if the result of **any execution** is the same as if the memory operations of all threads were executed *in some sequential order* and the operations of each thread appear in thread order
- Sufficient conditions:
	- A global order of stores to the same address is enforced across threads
		- This is plain coherence
	- A thread may not issue any access to memory until *all its previous accesses* have been **globally performed**
		- Very restrictive and slow
## Examples
```c
initial: A = B = 0;
Thread T1:  Thread T2:
A = 1;      print(B);
B = 1;      print(A);
```
- The only SC printing outcomes are "1 1", "0 0", or "0 1"
- List of executions:
	- A=1; B=1; print(B); print(A); " 1 1"
	- A = 1; print(B); B=1; print(A); "0 1"
	- print(B); A=1; print(A); B=1 "0 1"
	- print(B); print(A); A=1; B=1; "0 0"
	- A =1 print(B); B=1 print(A); " 0 1"
- No interleaving of access can result in "1 0"
	-  This is because **B=1 has to happen after A=1**
	- Stores must occur in thread order
- Remember that "0 1" satisfies plain coherence. 
## How to prove that an Execution is SC
- Draw an execution graph with directed edges according to the ordering rules. If cycle, then SC is violated.
1. $\text{Op}^{i}(A) \xrightarrow{t.o} \text{Op}^{i}(B) \implies \text{Op}^{i}(A) \xrightarrow{s.c}\text{Op}^{i}(B)$
	1. Thread order implies SC order
2. $\text{Val}[S^{i}(A)]: \text{Val}[L^{j}(A)] \implies S^{i}(A)\xrightarrow{s.c}L^{j}(A)$
	1. Load comes after producing store in SC
	2. Prodcon rule
3. $(\text{Val}[S^{i}(A)]: \text{Val}[L^{j}(A)]) \land (S^{k}(A)\xrightarrow{s.c.}L^{j}(A)) \implies S^{k}(A) \xrightarrow{s.c}S^{i}(A)$
	1. If load j depends on store i, and store k is sequentially before load j, then store k must come sequentially before store i
	2. If $i\xleftarrow{depend} j$ and $k\xrightarrow{s.c} j$, then $k\xrightarrow{s.c} i$
		1. The only possible SC order is $S^{k}(A)\xrightarrow{sc}S^{i}(A)\xrightarrow{sc}L^{j}(A)$
	3. If load j depends on store i, but there is also a separate store k that must come before load j, it cannot happen after store i. The only possible order is store k, store i, load j
4. $(\text{Val}[S^{i}(A)]: \text{Val}[L^{j}(A)]) \land (S^{i}(A)\xrightarrow{s.c.}L^{k}(A)) \implies S^{j}(A) \xrightarrow{s.c}S^{k}(A)$
	1. If load j depends on store i, and store i comes sequentially before load k, then the store that generates load j must come sequentially before store k
	2. If $i\xleftarrow{depend} j$ and $i\xrightarrow{t.o}k$, 
- Rules 3 and 4 summarized is:
	-  If a store sources the value of a subsequent (SC) load, then no other store to the same address can be inserted between the dependent load and store ops. 
	- If a load depends on a store's value, those two ops must be globally atomic in SC order.
### Dekker Example
![[Pasted image 20260501191918.png]]
1. 
2. If $L^{1}(B)0$ happens and $S^{2}(B)1$ also happens, $L^{1}(B)0$ must come first
	- $L^{1}(B)0\xrightarrow{sc}S^{2}(B)1$
3. If $L^{2}(A)0$ happens and $S^{1}(A)1$ also happens, $L^{2}(A)0$ must come first
	- $L^{2}(A)0\xrightarrow{sc}S^{1}(A)1$
4. Putting this together yields: $$S^{1}(A)1 \xrightarrow{to/sc}L^{1}B(0)\xrightarrow{sc}S^{2}(B)1\xrightarrow{to/sc}L^2(A)0\xrightarrow{sc}S^{1}(A)1$$
	- This is a loop.
	- This execution violates SC
- ![[Pasted image 20260501192251.png]]
## SC Optimizations

### Inbound Message Processing
- ![[Pasted image 20260501194722.png]]
#### Invalidation Acknowledgements
- Consider an incoming invalidation message
- It may need to traverse multiple levels of buffers and caches before all copies are invalidated
- When can an InvAck be sent?
- ![[Pasted image 20260501195037.png]]
- Incoming messages can be optimized without compromising store atomicity and sequential consistency
- It's ok to acknowledge an invalidation as soon as it is received
	- The invalidation doesn't actually have to reach the cache yet
	- The CPU can keep using the local copy until it does
	- This is allowed because we can say all the 'stale' loads come before the store is performed in the global order
	- ![[Pasted image 20260501200437.png]]
	- T0 
		- Sends the store and can't do the load of the new value until it gets the GP signal
		- Its thread order of x is 0->1
	- T1 
		- Sends invack immediately as it receives the inv
		- Even though T0 has received the GP signal and does a load of x=1, T1 can load x=0 temporally afterward because it has not invalidated it yet
		- Once its invalidated, T1 sends a GetS to T0 and does a load x=1
		- Its thread order of x is 0->1
	- T2
		- Same shit really keeps loading x=0 even temporally after $L^{0}(x)1$
	- Global order of x is coherent across all threads. Plain coherence is satisfied
##### Updated Definition of Store Performance
- A store is **performed** with respect to thread i at the point in time when the processor node of thread i has been notified of the store (inv or update)
- 
##### Example of fast invack optimization
![[Pasted image 20260501201939.png]]
![[Pasted image 20260501201952.png]]
![[Pasted image 20260501202227.png]]
![[Pasted image 20260501202349.png]]
#### Intervention Requests
- Interventions (FwdGetS, FwdGetX) require a (data) response from the cache. Cannot be acknowledged early
- **All prior incoming requests must be serviced first** This preserves a globally-visible ordering
- Flush could be delayed, but that would slow down the requesting core's execution
### Store Buffers and SC
- Load forwarding violates SC
- The thread can't issue the load before the stores in the buffer have been globally performed
- Can we relax the definition of global performance to speed up operations and allow more concurrency?

## SC vs. Store Atomicity
- Sufficient conditions for SC
	- Global order of stores to the same address is enforced
	- A thread may not issue an access to memory until all its previous accesses have been globally performed
- Under previous conditions, this would also enforce store atomicity
- Under the new definition of globally performed, this no longer requires store atomicity. Threads can see different values at a particular time.
	- A store is globally performed only if it is performed for all other processors
	- Before, a store is performed only if the processor can't load an older value anymore
	- Now, a store is performed when it is notified of the store. It can keep loading old values until the invalidation happens.
## Store Buffers In SC
- Forwarding store buffers can be SC and store atomic
- If a load hits in the store buffer, forward the value
- If a store hits, merge
- If a load misses in the store buffer, drain and perform all stores in buffer before load miss is issued
- All local loads/stores are added to global order when SB is drained
# Store Synchronization
- A memory system is **Store Synchronized** if a global order is enforced on all stores to all addresses and if no two threads observe these stores in a different order
	- In software, store synchronized memory systems are indistinguishable from store atomic ones
- A memory system is **Store Atomic** IFF its stores are synchronized

# Compiler Optimizations
- SC is the strictest memory model expected by programmers
- Imposes constraints on hardware optimizations
	- Store buffers
	- Lockup-free caches
- Imposes constraints on compilers
	- Code motion (reordering)
	- Code removal
	- These two violate SC
![[Pasted image 20260503181722.png]]
- 

For class #parallel-arch