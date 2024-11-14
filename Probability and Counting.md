Continues [[The Sample Space and Events]]
Using [[Boolean Algebra]]
- ## Axioms and Properties of Probability
	- ### Axioms:
		- For any event $A, \space P(A) \geq 0$
		- $P(\mathcal{S})=1$
		- If $A_{1}, A_{2},A_{3}\dots$ is an infinite collection of **disjoint** events, then:
			- $P(A_{1} \cup A_{2}\cup A_{3}\cup\dots)=\sum_{i=1}^{\infty}P(A_{i})$
				- Sets $A$ and $B$ are **disjoint** if $A\cap B=\emptyset$
	- ### Properties
		- $P(\emptyset)=0$
		- For any event $A$, $P(A)+P(A')=1$, from which $P(A)=1-P(A')$
		- For any two events $A$ and $B$
			- $P(A \cup B) = P(A) + P(B) - P(A\cap B)$
		- For any three events $A$, $B$, and $C$
			- $P(A \cup B\cup C) = P(A) + P(B) + P(C) - P(A\cap B) - P(A\cap C) - P(B\cap C) + P(A\cap B\cap C)$
				- For 4 events: add the following: $+P(D)-P(A\cap D)-P(B\cap D)-P(C\cap D)+P(A\cap B\cap D)+P(A\cap C\cap D)+P(B\cap D\cap D)-P(A\cap B \cap C\cap D)$
					- Subtract even length combinations and subtract odd lengths
			- Inclusion exclusion
- ## Counting Techniques
	- ### 'Classical' Probability
		- $N$: The number of outcomes in a sample space
		- $N(A)$: The number of outcomes contained in an event $A$
		- $P(A)=\frac{N(A)}{N}$
			- Notice that probability and relative frequency of events are the same
			- Also called 'classical probability'
	- ### The Product Rule for Ordered Pairs
		- If the first element or object of an ordered pair can be selected in $n_{1}$ ways, and for each of these $n_{1}$ ways the second element of the pair can be selected in $n_{2}$ ways, then the number of possible pairs is $n_{1}n_{2}$

For class #statistics 