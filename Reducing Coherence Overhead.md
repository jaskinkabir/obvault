Continues [[Scalable Cache Coherence]]
Continued by [[Directory Coherence Ordering and Correctness]]
# Reducing Bus Latency
![[Pasted image 20260416200157.png]]
- A BusRd is a 4 hop transaction
## Direct Remote Connection
- ![[Pasted image 20260416200352.png]]
- Connect remote cache directly to local cache so data doesn't have to go through home node
- The InvAcks can go directly to the local cache, which eliminates a bus transaction before writing is permitted 
# Directory Memory Overhead
- Overhead = $\frac{P}{8B}$
	- Percentage of total memory that you must additionally spend on directory bit field
	- P is number of processors
	- B is bytes per block/cache line
- For 1024 processors with block size 8, the overhead is 200% more memory per cache line
## We don't need to keep track of P sharers
- Rarely is a cache line shared by every single processor
- Or even more than 3 or 4
- ![[Pasted image 20260416202053.png]]
## Pointer based directory
- Assign each processor an ID
- Each directory entry contains  $i$ pointers, can only keep track of $i$ sharers
- Overhead = $\frac{i\log P}{8B}$
- For i=4, 1024 cores has 7.8% overhead
### What happens when a 5th sharer requests?
- Remove one pointer and invalidate that block
	- Non Broadcast option (NB)
- Set a flag that forces the directory to broadcast invalidations to all caches
	- Broadcast option
- Coarse Bit Vector
	- Each bit in the vector corresponds to a cluster of processors
	- Send inval to all processors in cluster if bit is set
- Hybrid
	- Limited pointer
	- Convert to full/coarse vector when exceeding sharing limit
- Software
	- Overflow pointers to memory
- Linked list
	- One pointer in directory, each cache block also has a pointer to next sharer
	- ![[Pasted image 20260421123059.png]]
	- Too expensive/complicated to implement
- ![[Pasted image 20260421122544.png]]
-  ![[Pasted image 20260421122646.png]]
- While the broadcast option sends more invalidations, the overall latency overhead is not significant because having more than 3 sharers is rare
- The Non broadcast option however forces a lot of bus requests while the processors take turns sharing the cache line
# Sparse Directory
- Size directory accoding to number of cached blocks
- Requires lookup of block address
- Associativity helps avoid conflicts
- If directory entry needs to be replaced, invalidate cache block
For class #parallel-arch