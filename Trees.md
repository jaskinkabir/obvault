![[Pasted image 20240605181522.png]]

## Terminology
- Node: Fundamental unit, containing data and pointers to all child nodes
- Root: Topmost node, from which all others descend. Only one per tree
- Siblings: Share the same parent
- Leaf: Has no children
- Internal: Has at least one child and is not the root
- Subtree: A tree consisting of a node and all descendants
	- Most tree-based algorithms are recursive, so this is a useful concept
- Height: The longest path from the root to a leaf
	- The height of a 1 node tree (root node) is 0
- Depth: The length of the path from the root to any given node
	- Each node has some depth, the height is the maximum depth
- Level: All nodes with the same depth are on the same level
- Degree: The number of children a node has
## Types of Trees
- ### Binary Tree
	- Each node has at most two children
- ### Balanced Tree
	- The height difference between the left and right subtrees of any node is at most one
- ### Complete Tree
	- All levels are fully filled except for possibly the left level, which is filled left to right
## Tree Algorithms
- ### Determine Number of Nodes
	- Perform this recursively
	- Number of nodes in tree is 1 + sum of nodes of each subtree
	- Base Case: 
		- Node has no children, return 1;
	- Recursive Case:
		- Call function on each child node and sum results +1
		- ![[Pasted image 20240605191355.png]]
- ### Determine Height
	- Base Case:
		- Null Tree has height zero
- ![[Pasted image 20240605193305.png]]
For class #data-structures 