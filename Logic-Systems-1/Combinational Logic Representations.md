Continues [[Boolean Algebra]]
Continued by [[Kmaps]]
Continued by [[Sequential Timing Diagrams]]
- ## Sum of Products Form
	- A canonical standard for boolean expressions
		- z = a + (a+b)c
			- z = a + ac + bc
			- a = a(1+c) +bc 
			-   **z = a + bc**
				- This is a sum of 2 products:
					- a and 1 + b and c
- ## Sum of Minterms
	- A minterm is an product containing all of the input variables
	- Consider: z = a + bc
		- z = a(b+b') + bc
		- z = ab + ab' + bc
		- ab(c+c')+ab'(c+c') + (a+a')bc
		- abc + abc' + ab'c + ab'c' + abc + a'bc
		- **abc + abc' + ab'c + ab'c + a'bc'**
			- An expression made up only of minterms
		- Easy to see if an expression is equal to another if they are in the same form
		- Each term of the minterm expression represents one of the possible rows of the truth table
			- Set those rows to 1 and the rest to 0
	- If you assign each row a variable $m_n$, the expression can be represented as
		- $\sum(m_{3}, m_{4}, m_{5}, m_{6}, m_{7})$
		- If this summation is the same as another function, equality can be easily be determined by comparing these expressions
		- 

a | b | c | z
-|-|-|-
0|0|0|0
0|0|1|0
0|1|0|0
0|1|1|1
1|0|0|1
1|0|1|1
1|1|0|1
1|1|1|1
-  Consider: $z = (A+B)(\overline{A}+AC)B$
	- $z = (AB + BB)(\overline{A} + AC)$ Dist
	- $z = (AB + B)(\overline{A} +AC)$ Idemp
	- $z = (B(1+A))(\overline{A} + AC)$ T8
	- $z = B(1)(\overline{A} + AC)$ null
	- $z = B(\overline{A} + AC)$
	- $z = \overline{A}B + ABC$ dist
	- $z = \overline{A}B(C+\overline{C})+ABC$ T5
	- $z = \overline{A}BC + \overline{A}B\overline{C} + ABC$
	- $$z = \Sigma (m_{2}, m_{3}, m{7})$$
### Product of Maxterms
- Maxterm: A sum of all the literals of the experession
- Consider: $z = a\overline{b}+ab$
	- $z = (\overline{a}+\overline{b})(\overline{a}+b)$
	- $z = \Pi(m_{3}, m_{2})$
- Same as minterms, where each row of the truth table corresponds to a value $m_{n}$
	- Going from truth table to either of these forms is very simple and vice versa
-  Can be found by inverting the sum of minterms
- ![[Pasted image 20221005113952.png]]
For class #Logic-Systems-1 

i|i|i|o|o|o
-|-|-|-|-|-
0|0|0|||
0|0|1|||
0|1|0|||
0|1|1|||
1|0|0|||
1|0|1|||
1|1|0|||
1|1|1|||
