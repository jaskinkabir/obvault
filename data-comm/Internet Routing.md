Continues [[Routing in Packet-Switching Networks]]
# Routing Info vs Routing Alg
- Routing info: about topology and cost in the internet (input to the algorithm)
- Routing algorithm: Used to make routing decisions based on the information
# Autonomous Systems (AS)
- A set of routers and networks (nodes) managed by one organization
- The nodes exchange info via 1 common routing protocol
- An AS is a connected network, meaning there is at least one route between any two nodes
# Approaches to Routing
## Distance-Vector Routing
- First generation routing alg for ARPANET
- Each node maintains a table (vector) giving the best known distance/time to each destination, and the preferred outgoing line to get to that destination
	- Metrics: # of hops, time delay, etc
Example:

| Dest | Distance | Next |
| :--- | :------- | :--- |
| B    | 1        | B    |
| C    | 1        | C    |
| D    | 2        | B    |
| E    | 2        | C    |
### Count To Infinity Problem
- ![[Pasted image 20251014150040.png]]
- Let's say A appears on this network
	- Once A appears on the network, B will recognize that its distance to A is 1 hop
	- Then it will broadcast this info to its neighbors
	- C hears from B that A is 1 hops away from it, so it realizes that it is 2 hops from A(C-B-A)
	- It will transmit this to D, who transmits to E
	- Finally, each node knows how many hops to A
- Now let's say A becomes unreachable
	- B knows that it can no longer see A
	- But it hears from C that it can get to A through 2 hops, so it thinks it can get to A within 3 hops (B-C-B-A)
		- This is wrong because B-A no longer exists
	- Then C hears from B that it is now 3 hops from A, so it updates itself to be 4 hops from A
	- This results in a loop of infinite feedback where each node thinks its hop count to A is increasing to infinity
- This happens because B does not know that C's 2 hop route to A uses B itself.
- The summary of this problem is
	- Good news propagates quickly, but bad news propagates slowly
		- The # of exchanges required to know when a node is unreachable depends on the numerical value used to define infinity (when the nodes should consider a node uncreachable)
			- Wise to set this to the longest possible path plus 1
	- The core problem is that when X tells Y it has a path somewhere, Y has no way of knowing 
#### Solution: Route Poisoning
- When a route fails, the nodes spread the bad news by poisoning the route
- This means it advertises the route to the unreachable node with a special metric value called infinity
- The value chosen for infinity should be the longest possible path plus one
## Link-State Routing
- Examples are Dijkstra and Bellman-Ford
- Designed to overcome drawbacks of distance-vector
- When router initialized, it determines link cost on each interface
	- First determine its neighbors: send HELLO pkt
	- Estimate delay to each neighbor: time to ECHO pkt received
- Floods link costs to all nodes in topology recursively
	- Link costs are sent to all routers, not just the neighbors
- From then on, routers monitor link costs
	- If there is a significant change, routers advertise new link costs
- Each router can then construct a toplogy of the entire network
	- Because each routeer receives link costs of all routers in the configuration
	- The routers can calculate the shortest path to each destination in the network using any algorithm (dijkstra, bellman-ford, etc)
- The router constructs a routing table, listing the first hop to each destination
- This is the second generation routing algorithm for ARPANET
# IRP vs. ERP
- Interior Router/Gateway Protocol (IRP): Routing algorithm within an AS
	- The goal is moving packets efficiently from source to destination
- Routing algorithms and tables may differ in different AS
- Exterior router/gateway protocol (ERP): Routing algorithm between ASs
	- Concern politics 
		- Ex: Any packet from Google's AS should never be routed using Microsoft's AS
	- Policies are typically manually configured into each Border gateway Protocol (BGP) router
	- Not distance-vector
		- Distance-vector assumes routers share common distance metric
		- Gives no info about ASs visited on route
	- Not link-state
		- Different ASs may use different metrics and have different restrictions
		- Flooding of link state information to all routers is unmanageable on such a scale
	- Path-Vector routing
		- Each block information exchanged lists all ASs visited on the route
		- Because a path vector lists the ASs that a datagram must traverse, the path info enables a router to perform policy routing
![[Pasted image 20251014151830.png]]
- R1 and R5 are BGP routers (border gateway)
# Open Shortest Path First (OSPF)
- IGP (Interior Gateway Protocol) of the internet
	- Most router vendors support it
- Uses Link-State routing alg
	- Each router keeps a list of state of local links
	- Transmits state update info
	- Little traffic as messages are small and not sent often
- Network topology is abstracted into a directed graph
# Border Gateway Protocol (BGP)
- Preferred EGP of the TCP/IP Internet
- BGP routers exchange info with other routers in other ASes
	- Instead of periodically giving each neighbor its estimated cost to each destination, each BGP router tells its neighbors the exact path it is using
![[Pasted image 20251014152104.png]]
- BGP Routers decide best routes
- Procedures
	- Neighbor acquisition: two neighboring routers in different ASs agree to exchange routing info regularly
		- One router sends request OPEN
		- Receiver ACK **Keepalive**
	- Neighbor reachability: maintain neighbor relationship
		- Periodically confirm with Keepalive
	- Network reachability: each BGP router maintains the networks it can reach and the preferred route for reaching each network
		- Whenever info changes, issue an update
- Messages are sent over TCP connections
	- Open
	- Update
	- Keep alive
	- Notification: error info
For class #data-comm