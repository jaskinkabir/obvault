Continues [[Split Transaction Bus]]
Continued by [[Scalable Cache Coherence]]
Related to [[Circuit Vs. Packet Switching]]
Related to [[Data Link Flow Control]]

# Overview
- How to send messages between caches, memories, etc?
- Requests: ReadX, Inv
- Responses: Flush, ReplyD, InvAck
- Desire for scalability leads to switched networks
# Communication Protocol
- Only need first 3 layers of OSI model
## Packet Format
- Header flit: First flit of packet contains routing and other info
- Payload can be any number of flits
- Tail flit indicates last flit in packet
	- May also contain data
	- May be combined with final payload flit
## Terminology
- **Phit**: Physical unit
	- Can be transmitted across a physical link in one "cycle"
	- Related to width of link
- **Flit:** Flow control unit
	- Unit of data accepted by RX
	- Typically link-layer flow control
	- Size of 1 buffer slot, minimum size of message
- **Packet:** Unit of routing, contains routing info and data to be delivered
	- Aka a message
## Reliability
- Failure to deliver a packet is treated as a **system error**, not something to be tolerated
- There may be some link-level/flit-level error correction, but these standard network-level techniques are not used
	- Dropping packets due to congestion
	- Ack of packet delivery
	- ReTX of lost packets
	- Reordering of packets at the RX to match TX order
## Flow Control
- Link-level, not end-to-end
- Sender must ensure receiver has space to store messages
	- Once sender sends message, the message is gone
- Stop signal it sent upstream when buffer reaches a threshold (compensate for in-flight flits)
- Go signal is sent upstream when space becomes available
- ![[Pasted image 20260224144047.png]]
- Credit-based flow control is also available
	- TX is allocated some number of 'credits' by RX
	- Every time TX sends a flit, decrement counter
	- When counter reaches 0, wait for RX to send credits before resuming TX
# Routing Vs Switching
- Routing: Choosing a path from TX to RX
- Switching: Method by which data is transmitted from TX to RX across multiple links
	- Implementation of routing decision
	- When is routing decision made?
	- How is data transferred between links?
	- How is data buffered?
## Circuit vs. Packet Switching
### Circuit Switching
- Connection reserved
- Entire message sent over connection
	- Can send multiple packets
- Connection is closed

### Packet Switching
- TX sends to RX without establishing connection
- Packets are individually routed and may take different paths
	- Do not enforce or guarantee packet ordering
- Styles of buffering:
	- Store and forward
	- Wormhole/cut-through
	- See bottom of [[Local Area Networks (LANs)]] for difference
#### Wormhole Buffering
- Pipeline individual flits of a packet across the link before the entire packet is received for retransmission
- Wormhole because head of worm enters the link and moves separately from the tail of the worm
# Latency
- Assuming no other packets in the network, latency is determined by number of routers along path (hops) and
- **Serialization Latency:** Number of cycles required to transmit packet across a link
- $$T=H \times T_{r} + \frac{L}{B}$$
	- $H$ # of Hops
	- $T_{r}$ Routing Latency
	- $L$ Length of packet in bits
	- $B$ Bandwidth of link in bits/cycle
	- Equation assumes wormhole switching
		- Sending flits as soon as they are received.
		- It takes one cycle to send a flit from TX to RX
- For store and forward: $T=H \times T_{r} \times \frac{L}{B}$
	- Because the full packet must be received at each hop before forwarding
- $$(R\times T_{r})+(H \times T_{L})+\left( \frac{L}{B}-1 \right)$$
	- More realistic formula (wormhole)
	- $R$ # of routers
	- $T_{r}$ Routing delay
	- $H$ # of links (hops)
	- $T_{L}$ Link delay
	- $L$ Length of packet
	- $B$ Bandwidth of link
# Topology
![[Pasted image 20260224150528.png]]
- Torus means connecting edges together, like a donut
## Topology Metrics
- **Degree:** Number of links per node
	- Related: Radix = number of ports per router
- **Bisection Bandwidth:** Bandwidth across a cut that partitions network
	- How many links to you have to break to cut the network in half
	- Multiply that number by the bandwidth of each link
	- How much bandwidth do you lose if you split the network in half?
	- If all communication is between these two halves, what bandwidth can be sustained?
- **Diameter**: Max distance between any two nodes
- **Hop Count** Distance between nodes
	- Avg hop count is a proxy for latency
	- Max hop count is diameter
- **Max Channel Load:** Traffic across busiest channel/link
	- Can be relative to injection rate – assume uniform traffic, etc
- **Path Diversity** Number of shortest paths between two points
	- High diversity gives more flexibility in routing
## Direct Network Topologies
- Each terminal node (core or cache) is associated with a router
- Router is source and sink of traffic, as well as switch for en route traffic
## K-ary n-cube
- Class of topologies defined by $N=k^{n}$
	- $N$ Number of nodes
	- $n$ Number of dimensions
	- $k$ Nodes per dimension
- A ring is an N-ary 1-cube
	- Also called a 1D torus
	- There is one dimension to travel in: ccw or cw
- Toruses and Meshes are both $\sqrt{ N }$-ary 2-cubes
## Calculating Avg Hops
- Mesh $$H_{avg}= \begin{cases}
 \frac{nk}{3} & k\text{ is even} \\
n\left( \frac{k}{3}-\frac{1}{3k} \right) & k\text{ is odd}
\end{cases}$$
- Torus 
- $$H_{avg}= \begin{cases}
 \frac{nk}{4} & k\text{ is even} \\
n\left( \frac{k}{4}-\frac{1}{4k} \right) & k\text{ is odd}
\end{cases}$$

- The loop connections across the mesh have long wires that result in long latency
- This is why meshes are more common than tori
## Hypercube 
- Binary n-cube - N=$2^{n}$
- Low diameter ($\log N$), high radix
- Bisection bandwidth = N/2
- ![[Pasted image 20260224153812.png]]
- Also has long wire problem
## Topology Tradeoff
- ![[Pasted image 20260224154125.png]]
- Mesh networks' diameter scaling is fast
- Bisection bandwidth equally unscalable
- Suppose bisection bandwidth is constant
	- Bisection bandwidth represents number of wires
	- How many wires cross the bisection
- ![[Pasted image 20260224154250.png]]
- Number of hops is not all that must be optimized
- Having many different links for better hop count optimization results in those links being narrower to meet resource constraints
- The latency benefit is cancelled out by the narrowing of links
- Low dimension networks with wormhole routing outperforms high dimension networks
# Indirect Networks
- Also called dance hall architecture
	- Boys would line up on one wall, girls on the other
	- Processors on one side, memories on the other
- Terminal nodes are the source/sink, Intermediate nodes do the switching
- eg: Crossbar, butterfly
	- ![[Pasted image 20260224170022.png]]
	- Crossbar:
		- Scalability is low with respect to cost
		- Better scalability in terms of bandwidth
		- Number of switches grows as $N^2$
		- Long wire problem
	- Butterfly
		- 
For class #parallel-arch 