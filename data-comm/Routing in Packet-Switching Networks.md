Continues [[Ethernet and MAC]]
Continued by [[Least Cost Algorithms]]
# Requirements for routing
- Correctness, implicitly, robustness, stability, fairness, optimality, efficiency
- Tradeoffs between requirements:
	- correctness vs simplicity
	- robustness vs stability
	- fairness vs optimality
	- efficiency vs correctness
# Performance Criteria
- Used for selection of route – the definition of "best"
- Minimum hop: select the route that contains the minimum number of nodes
- A generalization of minimum hop and more flexible criterion is least cost
	- A cost is associated with each link
	- Different definitions of cost
		- Data link rate
		- Link load
		- Queue length
		- etc
# Routing Strategies
## Fixed
- Single permanent route for each source to destination pair
- Determine routes using a least cost algorithm
- Route fixed until change in network topology
### Properties
- Simple, but inflexible
	- Does not react to failure or congestion
## Flooding
- No network information required
- Packet sent by node to every neighbor
	- Incoming packets retransmitted on every link except incoming link
- Eventually multiple copies will arrive at destination
- Each packet is uniquely numbered, so duplicate packets are discarded
- Nodes can remember packets already forwarded to keep network load in bounds
	- ![[Pasted image 20250918150359.png]]
	- If station 1 sends a packet for station 2, nodes a and b will both transmit packets to c
	- However c recognizes that it is receiving two identical packets, so it will only transmit once to station 2
- Can include a hop count in packets
### Properties
- All possible routes are tried – very robust (useful for military)
- At least one packet will have taken minimum hop count route. This information can be used to set up a virtual circuit
- All nodes are visited, useful to distribute information
- Many clones of each packet will be created
## Random
- Nodes randomly or round robin selects one outgoing path for retransmission of incoming packet
### Properties
- No network info needed
- Route is typically lot least-cost nor min-hop
## Adaptive
- Used by almost all packet switching networks
- Routing decisions change as conditions on the network change (failure/congestion)
	- Dynamically update cost values and routing table
### Properties
- Requires info about network
- Tradeoff between quality of network info and overhead
- Reacting too quickly can cause oscillation, too slowly not reactive enough

For class #data-comm