Continues [[Caching]]
Continued by [[Snoopy Coherence Protocols]]
# The Cache Coherence Problem
![[Pasted image 20260212160235.png]]
## Write-Back Cache
- ![[Pasted image 20260212160314.png]]
- In this write-back cache, the two processors now have an incoherent view of the sum variable
## Write-Through Cache
- ![[Pasted image 20260212160639.png]]
- To solve this, we can instead use a write-through cache
- P0 flushes the new value of sum to memory
- P1 flushes its new value to memory
- But P0 reads sum and gets a cache hit, which is the old, wrong value
- To solve this, assert that change must be propagated to other caches, not just memory
## Transaction Serialization Requirement
- Operations (reads and writes) to a memory location must be seen in the same order by all processors
### Write serialization
- ![[Pasted image 20260212160923.png]]
- P1 and P2 write simultaneously, but propagate at different speeds
	- Race condition: P1 and P2's writes race to memory
- P3 and P4 may see updates from P1 and P2 in a different order, and end up with different values
- Writes cannot occur at the same time, must be some mechanism to assert write order globally
### Read Serialization
 - ![[Pasted image 20260212161350.png]]
- Suppose P2 replaces x after write from P1, and P2 asks P3 for the data, but P3 hasn't seen P1's write yet
- P3 will tell P2 that x is 0, because P1 hasn't told it that x is 1 yet
- There needs to be a consistent ordering of reads and writes. 
- Should P2's read be treated as if it happened before or after P1's write?
# Cache Coherence
## Informal definition:
- A cache system is coherent if and only if all processors, at any point in time, have a consistent view of the **last globally written** value to each location
# Cache Coherence Protocol
- A specification of actions taken by memory transactions to ensure write propagation and serialization
- Basic design choices:
	- How is write propagation accomplished?
		- Invalidate copies in other caches
		- Update copies with the new value
	- How are reads and writes serialized?
	- Where are coherence requests sent?
		- All caches (broadcast or snooping)
		- Select caches (directory-based)
# Cache Architectures

![[Pasted image 20260212162605.png]]

## Shared Cache
- No coherence problem
- High interconnect bandwidth
- Not scalable
	- Large physical distance to cache
	- Access latency increases with size
## Symmetric Multiprocessor (SMP)
- Reduced pressure on interconnect: only needed for misses
- Caches are private, requires coherence
- Programming: Mindful of locality and coherence issues (ie false sharing)
- Does interconnect support broadcasting/snooping?
## Non-Uniform Memory Access (NUMA)/ Distributed Shared Memory (DSM)
- Further reduced pressure on interconnect, some misses handled by local mem
- Programming: NUMA – try to keep data close to where it is used
## Private Vs. Shared Cache Example Problems
![[Pasted image 20260212163715.png]]
1. One processor sequentially accesses blocks 0-15 twice in a row. What is the average access time for the private cache organization?
	1. Every single access is a miss: avg = 101
2. Same question but for shared cache
	1. First 16 are misses, next 16 are hits
	2. (16x102 + 16x2)/32=52
3. **Each processor** sequentially accesses blocks 0 through 15, twice in a row. In other words, P0 accesses all 16 lines (twice), then P1 accesses all 16 lines (twice), etc. What is the average access time for the **PRIVATE** cache organization?
	1. Every single access is still a miss: avg = 101
4. Same but shared
	1. First 16 are misses, the rest are all hits
		1. 32x4 accesses. 16 misses, 32x4-16=112
	2. (16x102 +112x2)/128=14.5
- In these cases, the shared cache is better every time
- But this access pattern is unusual, and in real scenarios the private cache is better
- Shared cache suffers from the interconnect not scaling well
# Bus Systems
![[Pasted image 20260212165840.png]]
- Assume a simple interconnect with 
	- Uniform distance
	- Inherent broadcasting
	- Inherent serialization
## What is a bus?
- A generic term for a wired connection between components
- Includes physical wires and a communication protocol
## Terminology
- Synchronous: Common clock for all components
- Arbitration: Decides who gets to place data onto the bus
	- Example. D0 and D1 ask simultaneously
	- Arbiter grants 0 first
	- Grants 1 next, 1 needs to wait until bus is not busy 
## Serialization
- Because caches must arbitrate to get access to the bus, requests are naturally serialized
- Our assumption for now is that the bus is occupied/busy until the transaction is complete

For class #parallel-arch