Continues [[Snoopy Coherence Protocols]]
# Sharing Patterns
## Producer Consumer Sharing
- Occurs when one processor writes to a block, and one or more caches read that data
- ![[Pasted image 20260223195455.png]]
- Issue for MSI/MESI/MOESI (Invalidate)
- Each reader has to do a bus read request
### Optimization: Read-Snarfing / Read Broadacsting
- ![[Pasted image 20260223195858.png]]
- Allows a cache with an invalid copy of the block to grab the data during another cache's BusRd request
- Advantage: Reduces bus transactions and read latency
- Disadvantages: 
	- Can pollute cache with unneeded data
	- Increases conflicts with processor r/w
## Migratory Sharing 
- Each cache reads and then writes a block
- Global sum is a good example
- Issue for Invalidate protocols
- ![[Pasted image 20260223200147.png]]
### Optimization: FlushX
- M state yields its ownership in response to BusRd
- The BusUpgr transactions can then be avoided.
- Reader sees FlushX response instead of Flush, and goes to M state
- ![[Pasted image 20260223200532.png]]
- Do not want to do this all the time. 
- If this optimization is used during a producer consumer pattern:
- ![[Pasted image 20260223200659.png]]
- **Need to detect when line enters and exits migratory pattern**

# Detection of Sharing Pattern
## Modify State Machine
- Include an M signal to know when in migratory state
![[Pasted image 20260223201035.png]]
- The S2 state above allows the modified state to detect if a BusRd is directly followed by a BusUpgr, which indicates migratory sharing
- The Shared state will now transfer to MD state when a prwr occurs in a migratory pattern
- In the MD state, a BusRd will issue a FlushX state to migrate ownership
- If an invalid line is issued a PrRd
	- If responded to by a FlushX, go to Migratory Clean
	- If responded to by a normal flush, producer-consumer
- Migratory Clean determines if the line is still in migratory state
	- The data was given in the migratory state, next transaction will determine if the cache line should still be migratory
	- A PrWr/PrRd will keep the line in migratory state
	- Only another processor 
- S2 is the only state that can assert the M signal
- The problem with the S2 optimization is that it is **incompatible with read broadcasting**
	- If caches bring data into their cache upon a BusRd, there is no longer a way to guarantee there are only two copies of the data
	- Moving into the S state does not mean the processor has just issued a read request
	- No longer useful for establishing sharing pattern
## Sharing Predictor
- Implement a separate sharing predictor at each cache with its own state
- If an M line sees a BusRd followed by a BusUpgr by the same processor, add it to the predictor table
- May be harder to detect when the pattern ends
# Update Protocol Optimization
- When is invalidating better than updating?
- Consider the *write run* concept: Multiple writes by the same processor ending with a read or write by another processor
- For a long write-run pattern, an update/dragon protocol would be wasteful
	- The cache does not need to update itself upon every update
	- ![[Pasted image 20260223203532.png]]
## Bandwidth Requirements
- Consider the bandwidth requirements for invalidate vs update for a write run length of N
	- $B_{inv}=B_{upgr}+B_{rd}$
	- $B_{update}=N \times B_{upd}$
- Assuming that BusUpd and BusUpgr require the same bandwidth, then dragon/update requires more bandwidth than invalidate when
	- $$N > 1 + \frac{B_{rd}}{B_{upd}}$$
	- Bus Update is one word, but Bus Read is a line, so the ratio is actually just the cache line size in words
	- For line size = 8 words, break-even point is N=9
		- This can happen if the entire cache line must be written more than once
- Dragon works for low write run situations
## Competitive Snooping: Detecting Long Cache Runs
- Create a counter for each cache line
- Initialize counter to threshold (N=10) when line is loaded into cache
- Decrement counter on each BusUpd received by the cache
- Reinitialize counter on each access by local processor
- If counter reaches zero, invalidate
- If updates are received, but the local processor is not using the data, then invalidate to stop acting on updates

For class #parallel-arch 