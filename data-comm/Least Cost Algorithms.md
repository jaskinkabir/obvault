Continues [[Routing in Packet-Switching Networks]]
# Dijkstra's Algorithm
## Definitions
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
1. Initialization
	1. $T=\{ s \}$ The set of nodes so far incorporated consists of only source node
	2. $L(n)=w(s,\,n),\,s \neq n$
2. Get Next Node
	1. Find neighboring node not in T with the least-cost path from s
	2. Incorporate node into T
3. Update Least-Cost Paths
	1. Figure out if there are any lower cost paths by summing link costs
	2. $$L(n)=\min[L(n),\,L(x)+w(x,\,n)] \ \forall n \notin T,\,x \in T$$
	3. Algorithm terminates when all nodes have been added to T
	4. At termination, $L(x)$ is the cost of the least-cost path from $s \to x$
### Example
- $s=N_{1}$

![[Pasted image 20250923145837.png]]


| **Iteration** | **T**     | **L(2)** | **Path** | **L(3)** | **Path**  | **L(4)** | **Path** | **L(5)** | **Path**  | **L(6)** |     |
| ------------- | :-------- | :------- | :------- | :------- | :-------- | :------- | :------- | :------- | :-------- | :------- | :-- |
| 1             | {1}       | 2        | 1-2      | 5        | 1-3       | 1        | 1-4      | $\infty$ |           | $\infty$ |     |
| 2             | {1, 4}    | 2        | 1-2      | **4**    | **1-4-3** | 1        | 1-4      | 2        | **1-4-5** | $\infty$ |     |
| 3             | {1, 4, 2} | 2        | 1-2      |          |           |          |          |          |           |          |     |
|               |           |          |          |          |           |          |          |          |           |          |     |

### Example 2
- $s=2$
![[Pasted image 20250923145837.png]]

| **Iteration** | **T**             | **L(1)** | **Path** | **L(3)** | **Path** | **L(4)** | **Path** | **L(5)** | **Path**  | **L(6)** | **Path**      |
| ------------- | :---------------- | :------- | :------- | :------- | :------- | :------- | :------- | :------- | :-------- | :------- | :------------ |
| 1             | {2}               | 3        | 2-1      | 3        | 2-3      | 2        | 2-4      | $\infty$ |           | $\infty$ |               |
| 2             | {2, 4}            | 3        | 2-1      | 3        | 2-3      | 2        | 2-4      | **3**    | **2-4-5** | $\infty$ |               |
| 3             | {2, 4, 1}         | 3        | 2-1      | 3        | 2-3      | 2        | 2-4      | 3        | 2-4-5     | $\infty$ |               |
| 4             | {2, 4, 1, 3}      | 3        | 2-1      | 3        | 2-3      | 2        | 2-4      | 3        | 2-4-5     | **8**    | **2-3-6<br>** |
| 5             | {2, 4, 1, 3, 5}   | 3        | 2-1      | 3        | 2-3      | 2        | 2-4      | 3        | 2-4-5     | **5**    | **2-4-5-6**   |
| 6             | {2, 4, 1, 3, 5,6} | 3        | 2-1      | 3        | 2-3      | 2        | 2-4      | 3        | 2-4-5     | **5**    | **2-4-5-6**   |

# Bellman-Ford Algorithm
## Definitions
- $s$ is source node
- $w(i, j) =$ link cost from node $i$ to node $j$
	- $w(i,\,i)=0$
	- $w(i,\,j)=\infty$ if two nodes are not directly connected
		- $w$ function only deals with neighbors
	- $w(i,\,j) \geq 0$ if two nodes are directly connected
- $h$ = maximum number of links in the path at the current stage of the algorithm  
 $L_{h}(n)$ = cost of the least-cost path from s to n under constraint of no more than h links
![[sheets/sheet2025-09-23 15.50.02.univer.md#Sheet1|A1:L6<300>]]

| **Iteration** | **T** | **Lh(1)** | **Path** | **L(3)** | **Path** | **L(4)** | **Path** | **L(5)** | **Path** | **L(6)** | **Path** |
| ------------- | :---- | :-------- | :------- | :------- | :------- | :------- | :------- | :------- | :------- | :------- | :------- |
|               |       |           |          |          |          |          |          |          |          |          |          |
|               |       |           |          |          |          |          |          |          |          |          |          |
|               |       |           |          |          |          |          |          |          |          |          |          |
|               |       |           |          |          |          |          |          |          |          |          |          |
|               |       |           |          |          |          |          |          |          |          |          |          |

# Comparison
- Results from both algorithms agree
- Information gathered
	- Bellman-Ford
- 
For class #data-comm