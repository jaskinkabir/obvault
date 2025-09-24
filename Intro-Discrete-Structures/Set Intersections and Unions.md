# Set Intersections and Unions
Continues [[Set Operations]]
Using [[DIscrete Structure Notations]]
- ### Union: $A\cup B$
		- The set of all elements in A OR
- ### Intersection: $A \cap B$
	- The set of all elements in A AND B
	- If $A \cap B = \emptyset$, then A and B are **DISJOINT**
		- Share no elements
- ### Properties of U/I
	- Associative, distributive, commutative, etc
	- $\cap$ and $\cup$ are linear operations
	- ![[Pasted image 20220830130028.png]] 
- ## Inclusion-Exclusion:
	- $|A\cup B| = |A| + |B| - |A\cap B|$
	- $|A \cup B \cup C| = |A| + |B| + |C| - |A\cap B| - |A\cap C| - |B\cap C| + |A\cap B \cap C|$
		- Must add the total intersection, since it's been subrated from each two way intersection
- ### De Morgan's Laws
	- $\overline{A\cup B} == \overline{A} \cap \overline{B}$
		- Complement of union is the intersection of complements
	- - $\overline{A\cap B} == \overline{A} \cup \overline{B}$
		- Complement of intersection is the union of complements


For class #Intro-Discrete-Structures