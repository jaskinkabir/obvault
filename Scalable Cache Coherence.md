NOT ON EXAM 1
Continues [[Snoopy Coherence Protocols]]
Continues [[Chip Interconnection Networks]]
Continued by [[Reducing Overhead]]

# Scalability
## Bus Does Not Scale
- Fixed bandwidth, per core b/w decreases with size
- Bus wires get longer, affects clock rate
- Independent memory transactions compete for arbitration
## Indirect Networks
- Number of switches scales superlinearly with # of nodes
- Latency increases with system size
- Can make all memories equally distant, but not equally close
# cc-NUMA/NUCA
- ![[Pasted image 20260224170533.png]]
- Distributed memory, direct network
- **cc-NUMA:** **cache coherent-Non Uniform Memory Access**
	- Processors access local memory faster than remote memory
	- Different memories have different latencies
## Pros and Cons
- + Scalable interconnect: b/w/ grows with # processors
- + Locality of memory accesses: latency grows slower than # processors
- - Coherence protocol is more complex
- - Programmer/OS must care about locality
	- Latency is not uniform
	- 
# Directory-Based Coherence
- The bus is the ordering point AND the medium
	- Write propagation is easy
	- Everyone is listening, snooping is easy
- Point-to-point networks have no implicit broadcast
	- How to snoop?
	- How are writes propagated?
- You could possibly use an explicit broadcast to propagate writes
	- ![[Pasted image 20260224172549.png]]
	  
	- Wastes bandwidth
- Or keep a directory of shared cache lines at the ordering point
	- ![[Pasted image 20260224173003.png]]
## Design Decisions
- Protocol: states, messages, actions, etc
- Placement of directory (memory controller, LLC)
	- For now assume it is with the memory
- Format of sharing info
- Some decisions will be related to the properties of the interconnect network
## Base Protocol
![[Pasted image 20260224173203.png]]
- Cache is MSI
- Directory: For each memory block, track:
	- Clean/dirty
	- Bit vector to track sharing status of each cache
		- Presence Flag Vector
- A block's **physical address** determines its location in memory
	- Which bank
- This is known as the **home** node
### Example Scenarios
#### Read Miss (Clean)
1. Requester (L) sends read request to home (H)–BusRd
2. H updates directory (adds L to sharers) and sends data–Flush
- L = local cache, H = home memory, R = remote cache
#### Read Miss (Dirty)
![[Pasted image 20260224173634.png]]
1. Requester (L) sends read request to Home (L)–BusRd
2. Directory forwards read to owner (R)–RemRd
3. R sends data to memory–Flush
4. H updates directory (two sharers) and sends data to requestor–Flush
#### Upgrade Request, One Sharer (Clean)
![[Pasted image 20260224174142.png]]
1. Requester (L) sends upgrade – BusUpgr
2. H finds that L is the only sharer, sends ack – UpgrAck
	1. Sets the line's dirty flag
- L must wait for UpgrAck to change its state to M and perform write
#### Upgrade Request, Multiple Sharers (Clean)
![[Pasted image 20260224174350.png]]
1. Requester sends upgrade – BusUpgr
2. H sends invalidate requests to all shareers – InvRq
3. H collects acks from all sharers – InvAck
4. H updates directory and sends ack to L – UpgAck
- L must wait for all InvAcks and the UpgrAck to change to M and perform the Write
#### Write Miss, No Sharers, Clean
1. L to H – ReadX
2. H to L – FlushX
#### Write Miss, At Least One Sharer, Clean
![[Pasted image 20260224174900.png]]
1. L to H – ReadX
2. H sends invalidate requests to sharers – InvRq
3. H waits for acks – InvAck
4. H to L – FlushX
#### Write Miss (Dirty)
1. L to H ReadX
2. H to R RemRdX
3. R to H FlushX
4. H to L FlushX

### Location of H in On-Chip Memory
- H is a directory, L and R are caches
- L and H could be in the same node, or H is in one of the R nodes
- If true, this reduces the number of messages on the network
### Ordering of Memory Transactions
- Home is the ordering point
	- Asserts the order
	- Not for all blocks, just for the ones it owns based on physical address
- ![[Pasted image 20260224181603.png]]
- H sets a busy bit for a cache line when it handles a request
- Blocks/NACKs any other requests until the request is complete
- Order of memory ops is determined by order in which H handles the requests
### When is the operation complete?
![[Pasted image 20260224182016.png]]
A1: A sends upgrade to H. H sets Busy
A2: H clears busy, sets dirty, sends UpgrAck to A
B1: Read arrives at H from B. H sets Busy
B2: H forwards read request to A
- What if B2 arrives at A before A2?
	- A cannot satisfy request
- Solutions:
	- May enforce point-to-point ordering, which prevents B2 from arriving before A2
		- Acks/Responses will be sent in the order in which requests are received
	- A must send an ACK for A2, H does not clear busy until UpgrAck is acknowledged
	- A sends NACK to H, which forces H to retry
For class #parallel-arch