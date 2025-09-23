Continues [[Routing in Packet-Switching Networks]]
# Dijkstra's Algorithm
## Definition
- Find shortest paths from given source node to all other nodes, developing paths in the order of increasing path length
- $N =$ set of nodes
- $s =$ source node
- $T =$ set of nodes so far incorporated by the algorithm
- $w(i, j) =$ link cost from node $i$ to node $j$
	- $w(i,\,i)=0$
	- $w(i,\,j)=\infty$ if two nodes are not directly connected
		- $w$ function only deals with neighbors
	- $w(i,\,j) \geq 0$ if two nodes are directly connected
- $L(n)=$ cost of the least-cost path from node $s$ to node $n$ currently known
## Method


For class #data-comm