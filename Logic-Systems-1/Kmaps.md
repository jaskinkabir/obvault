# Kmaps
Continues [[Boolean Algebra]]
Continued by [[Sequential Timing Diagrams]]
- A method for creating a function based on a truth table
- Also for simplifying a boolean expression
- METHOD
	- Create kmap grid
		- For multivar function, group variables into same column
		- For adjacent cells, only one variable can change value at a time
	- Circle groups of one with size that is a power of 2
		- Can also group pacman style from ends of table
	- Determine which variables play into the result of that group
	- Write expression based on these groups
	- ![[Pasted image 20221002210857.png]]
	- Each group/circle is a **Prime Implicant**
		- The **Essential Prime Implicants** contain at least one minterm that is not circled by any other group
		- **Reduntant Prime Implicants** Are made redundant when every minterm is circled by other essential prime implicants
		- **Selective Prime Implicants** Are neither essential nor redundant
	- 
For class #Logic-Systems-1 