Continues [[Set Operations]]
- Falling Factorial:
	- $(n)_{k}=\frac{n!}{(n-k)!}$
- Permutations:
	- Selecting from a set without duplication and where order matters
	- For selecting k items from an n item set
		- P = $(n)_{k}$
- For a counting problem where any number of repititions are allowed
	- Ie: 5 colors of pens to choose from, must pick 5 pens where order does not matter, and
	- $\large{\left( \frac{(n+k-1)!}{k!} \right)}$
- ## Which Method to Use
 
 -|**Order Matters** | **Order Doesn't Matter**
-|-|-
Repition Allowed | $n^k$: Exponent | $\left( \left( \frac{n}{k} \right) \right)$: Multichoose
Repition Not Allowed | $(n)_{k}$: Permutation | $\left( \frac{n}{k} \right)$: Choose
 
- # Pigeonhole Principle
	- If n pigeons are assigned to m pigeonholes, and m<n, (Fewer holes than pigeons)
		- Housing crisis
		- At least one pigeonhole contains 2 or more pigeons
		- 
	- Suppose 8 pigeons and 7 pigeonholes
		- Many possibilities
			- 6 holes contain 1 pigeon, 1 contains 2
				- Every other case will have empty holes
	- ### If $\large \lceil\frac{n}{m}\rceil>n$
		- $a= \lceil\frac{n}{m}\rceil$
			- Ceiling
		- There are at least $a$ duplicates
			- $a$ holes with more than one pigeon
		- To guarantee $a$ duplicates,
			- $n=(m*a)-a-1$
- # Derangement
	- A permutation where the jth position is not j
		- The permutations of \[3\]= {1,2,3}
			- 123
			- **132**
			- 213
			- **231**
			- **312**
			- **321**
			- 4 derangements of 3 on {1,2,3}
	-  Formula for a derangement on set of length n:
		- $$\large n!-\sum(-1)^{i+1}(n-i)!{{n}\choose{n-i}}$$
			- i is the iterating variable
			- n <=10
	- Calculating number of derangements
		- EXP: Derangements on $[5]=\{ 1,2,3,4,5 \}$
			- Define sets:
				- $B_{1}=\{ 1**** \}$
				- $B_{2}=\{ *2*** \}$
				- $B_{3}=\{ **3** \}$
				- $B_{4}=\{ ***4* \}$
				- $B_{5}=\{ ****5 \}$
			- Cardinality of each set
				- Cardinality of each set is 4! = 24
				- Total cardinality equals 5x4!=5!
				- A lot of overlap between each set
			- Inclusion-Exclusion 
				- \# of permutations - \# of non derangements
				- 1 fixed point: (1,x,x,x,x): $|B_{1}|=\left( \frac{5}{1} \right)*4!$
				- 2 fixed points: (1,2,x,x,x): $|B_{1}\cap B_{2}|=\left( \frac{5}{2} \right) * 3!$
				- 3 fixed points: (1,2,3,x,x): $|B_{1}\cap B_{2}\cap B_{3}|=\left( \frac{5}{3} \right) * 2!$
				- 4 fixed points: (1,2,3,4):  $|B_{1}\cap B_{2}\cap B_{3}\cap B_{4}|=\left( \frac{5}{4} \right) * 1!$
				- 5 fixed points (1,2,3,4,5): $|B_{1}\cap B_{2}\cap B_{3}\cap B_{4}\cap B_{5}|=\left( \frac{5}{5} \right) * 0! = 1$
				- Total number of non-derangements is 
					- $120-(\left( \frac{5}{1} \right)*4! - \left( \frac{5}{2} \right)*3! + \left( \frac{5}{3} \right)*2! - \left( \frac{5}{4} \right)*1! +\left( \frac{5}{5} \right) * 0!) = 120 - 76$
					- Answer is 44

For class #Intro-Discrete-Structures