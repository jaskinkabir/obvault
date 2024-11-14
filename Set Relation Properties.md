Continues [[Set Relations]]
Continued by [[Set Relation Digraph Representation]]
# WORKS ONLY FOR AxA
- ## **Reflexive**:
	- $(a,a) \in R,  \forall a \in R$
	- All loops exist in digraph
- ## Irreflexive
	- $(a,a) \notin R,  \forall a \in R$
	- No loops in digraph
- ## Symmetric
	- $(a,b) \in  R \iff (b,a) \in R$
	- Only 2 way digraph links
- ## Antisymmetric
	- $(a,b) \in  R \iff (b,a) \notin R$
	- Only 1 way links
- ## Asymmetric
	- $(a,b) \in  R \iff (b,a) \notin R \land (a,a) \notin R,  \forall a \in R$
	- Irreflexive + Antisymmetric
	- Only 1 way links and no loops
	- Square to Antisymmetric's rectangle
- ## Transitive
	- $\forall a,b,c \in X, ((a,b)\in R \land (b,c)\in R) \Rightarrow (a,c)\in R$
- ## Equivalence
	- Reflexive, Symmetric, and Transitive
- ## Partial Order
	- Reflexive, Antisymmetric, and Transitive
- ## The Equivalence Class
	- For an equivalence relation R based on building set A={a,b,c,d}
		- The equivalence class of a, notated \[a\], is the set of elements connected to A
			- The set of connections of a
	- The operation A/R creates the set of all equivalence classes of R
		- Some of them can be repeated, and so the cardinality \[A/R\] is not simply the number of elements of A
- ## Relation's Square
	- $$(a,b) \in R^{2} \iff \exists c,\ (a,c)\in R\land (c,b)\in R$$
		- For a transitive relation, $R^2=R$
	- Remove all pairs from R to make it transitive

For class #Intro-Discrete-Structures 