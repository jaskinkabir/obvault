Continues [[Reducing Coherence Overhead]]
Continued by [[System Partitioning and Virtualization]]
Continued by [[Memory Model and Coherence Definition]]
# Ordering and Correctness
- There is no global ordering point in a network
- Ordering of transactions is only handled by local directories, on a block by block basis
# Out of Date Info
## Shared block is silently evicted and later invalidated
- ![[Pasted image 20260423204223.png]]
- C0 should send an InvAck to C2
## Shared block is silently evicted, later has read/write miss
![[Pasted image 20260428130254.png]]
- Home node must be designed to handle this case
- It will send ReplyD (data) and inv to other sharers if ReadX
## Exclusive block is silently evicted and later has a r/w miss
![[Pasted image 20260428130441.png]]
- H should send ReplyD to C2, but only if it's certain a Write Back will not arrive
	- C2 could have modified the data and sent it back to the cache before it issued the read
- This cannot be solved by directory alone
- The cache must wait for Ack from WB and delay any Read/ReadX until Ack is received
- Cache must also respond to intervention (due to miss from another cache) with data until WB ack'd
- The cache cannot evict dirty data until it's certain the home node has it
- This means the cache needs some small buffer to hold dirty or exclusive evicted data while it waits for an ack from the directory
# Overlapping Requests
![[Pasted image 20260428165641.png]]
- A cannot know if B's ReadX got to H first or if its Read got there first
- Both situations require different responses
## Home-Centric Approach
- Let H determine when op is complete by receiving acks from the requestor
- ![[Pasted image 20260428170219.png]]
	- Must wait for A's ack before directory can respond to B's readX
	- Must intervene, downgrade owner's permissions
	- Increases latency
## Requester-Assisted Approach
- Each cache must track outstanding requests and only handle conflicting incoming requests after the request is complete
- ![[Pasted image 20260428170451.png]]
- ![[Pasted image 20260428172038.png]]
# Write Propagation and Serialization
![[Pasted image 20260428172228.png]]-
- Write propagation is achieved by sending all requests to H, which will then send invalidations to sharers
- On miss, H provides the most recently written data by retrieving from memory or sending an intervention to the owner of a dirty block
## Home-Centric Serialization
![[Pasted image 20260428172338.png]]
- All requests appear to complete in the order in which they are received and accepted by H
- H must stall (nack or buffer) until the previous request is complete
- Dependency: ![[Pasted image 20260428172955.png]]

For class #parallel-arch