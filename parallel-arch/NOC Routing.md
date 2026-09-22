Continues [[Chip Interconnection Networks]]
# Routing Options
- **Minimal vs. Non-Minimal:** Least hops or allow longer routes? (ie to avoid congestion)
- **Non-minimal**: 
- **Deterministic vs Non-Deterministic:** Always choose the same path?
- **Oblivious Vs Adaptive:** Path choice based on state of network?
- **Per-Hop Vs Source Routing:** Does the source choose full path, or is it determined at each router?
- **Deadlock-free** Guaranteed to avoid deadlock
	- May rely on physical characteristics of network, flow control mechanisms, etc
- **Path Diversity:** Number of alternative paths available
## Source Routed Example: Butterfly Network
- ![[Pasted image 20260503211739.png]]
# Dimension-Order Routing
- Used in mesh/torus networks
- Choose a fixed order of traversing the dimensions
- For example
	- Move as far as necessary in X
	- Then move far as necessary in Y
- Like moving a ladder to get to a certain height or like plotting coordinates
- Cannot switch back and forth between X and Y
	- This is to create determinism
# Routing Deadlock
- ![[Pasted image 20260503213255.png]]
	- Cyclic dependency
	- If all parties decided the order of dimensions to hop through, this cycle wouldn't have happened
		- A decided X then Y
		- B decided Y then X
		- C decided X then Y
		- D decided Y then X
		- Should have enforced one order
## Turn-based Deadlock Avoidance
![[Pasted image 20260503213657.png]]
- By restricting the allowed turns, DOR (X-Y) avoids deadlock
- There are no cycles in the link dependencies
- Disadvantage: No path diversity, no adaptivity
## Oblivious Routing
- Provide path diversity by first routing to a randomized node $d'$
	- ![[Pasted image 20260503213901.png]]
	- Send entire packet to d' not just flits
	- d' realizes it's not his packet, he forwards it to d
	- This is **Oblivious** because the choice is random, not based on network congestion
- ![[Pasted image 20260503213954.png]]
	- Pick a random node along the minimal path to be d'
## Adaptive Routing
- ![[Pasted image 20260503214119.png]]
- If the packet encounters congestion, it can use other dimensions
- Minimal if it always moves towards destination
- Not deadlock-free if **fully** adaptive routing is allowed
	- Still allows cyclic dependency
### Turn-Based Adaptive Routing
- West First Turns
- Odd-even Routing
- Eliminate some turns
- ![[Pasted image 20260503214233.png]]
# DOR Implementations
## Source Routing Table
- ![[Pasted image 20260503214701.png]]
- Each source has lookup table, one entry per destination
- May include alternate routes, chosen by source
- Packet header must be large enough to carry complete route
## Per-Hop LUT
- Small LUT per router with choices for next hop
- Flexible, programmable
- ![[Pasted image 20260503215021.png]]
## Logic
![[Pasted image 20260503215233.png]]
- Calculate outgoing port for next hop
- Good for fast, deterministic routing and regular topologies
- Hard-wired routing algorithm, no flexibility
# Flow Control Deadlock
## Partition Resources to Avoid Cycles
- Can resolve deadlock by providing a second set of channels for any message that wraps around in each dimension
	- The only way to switch between sets of channels is by crossing an established 'dateline'
- ![[Pasted image 20260503215646.png]]
- Extra wires that are mostly unused
## Virtual Channels
- ![[Pasted image 20260503215728.png]]
- Create multiple sets of buffers that can send/receive messages across the same physical channel
- The deadlock is actually caused by lack of buffers so we can just add more
- Swiss army knife of system-are networks
- Can be used for
	- Deadlock-free routing in wormhole networks
	- Avoiding deadlock in adaptive routing
		- Provides a deterministic escape channel
	- Implement separate logical networks
		- Can have different priorities, buffer sizes, routing
		- Ex: Coherence requests (in-order) vs responses (out-of-order)
# Protocol Deadlock
![[Pasted image 20260503220020.png]]
- Scenario
	- Let's say a request comes in that needs a reply to be satisfied
	- But reply queue is all backed up
	- the request queue cannot be cleared because the reply queue is full and vice versa
- Separate messages into classes, eg request and reply, and create a set of virtual channels for each class
- But is a flush request from the owner of dirty data a response or request? It is a response to a BusRd, but a request for a flush
- Design protocol such that each message can only trigger messages on a "higher" VC number
# Router Implementation
![[Pasted image 20260503220302.png]]
## Buffer
![[Pasted image 20260503220329.png]]
- Input buffering
	- Separate buffer for each VC
	- Size depends on flow control
- Output buffering
	- May or may not be needed
	- Flow control signal could flow through the switch
## Crossbar Switching
![[Pasted image 20260503220455.png]]
- Scales quadratically with number of nodes
## Dimension Slicing
![[Pasted image 20260503220528.png]]
- Replace one 5x5 crossbar with two 3x3 crossbars
- Well suited for DOR
## Router Pipeline
![[Pasted image 20260503220749.png]]
### Traditional Vs. Lookahead Routing
![[Pasted image 20260503220827.png]]
- Do virtual channel allocation and route calculation at the same time
- ![[Pasted image 20260503221107.png]]


For class #parallel-arch