Uses [[Discrete Structure Notations]]
Related to [[Proofs and Truth Value]]
Related to [[Proof By Induction]]
Related to [[Trees]]
# Structural Representations
## Grammars
- A useful model when designing software that processes data with a recursive structure
	- For example, a parser that traverses a syntax tree
- A grammatical rule like $E \to E + E$ states that any expression can be formed by connecting two expressions with a plus sign.
# Automata and Complexity 
- Automata are essential for the study of the limits of computation. There are two important issues
	- What can a computer do? This is called "decidability". Any problem that can be solved by a computer are called decidable
	- What can a computer do efficiently? This is called "intractability". Problems that can be efficiently solved by a computer are called "tractable"
# 1.2 Introduction to Formal Proof
## 1.2.1 Deductive Proofs
- Consists of a sequence of statements whose truth leads from some initial statement, called the *hypothesis* or the *given statement(s)*, to a *conclusion statement*
	- Each step in the proof must follow, by some logic, from either the given facts some of the previous statements, or a combination of the two
### Deductive Proof Example
**Theorem 1.3**: $\forall x \geq 4, 2^{x} \geq x^{2}$
**Theorem 1.4: If $x$ is the sum of the squares of four positive integers, then $2^{x} \geq x^{2}$**
1. $x=a^{2} + b^{2} + c^{2} + d^{2}$: given
2. $a,b,c,d \in \mathcal{Z}$: given
3. $a\geq_{1},b\geq_{1},c\geq_{1},d\geq_{1},$ given
4. $a^{2} \geq 1, b^{2} \geq 1,c^{2} \geq 1,d^{2} \geq 1$ from arithmetic
5. $x \geq 4$ from (1) and (3) and arithmetic
6. $2^{x}\geq x^{2}$ from theorem 1.3
## 1.2.2 Reduction to Definitions
- If it is unclear how to start a proof, reduce all terms in the hypothesis to their basic definitions
- Example:
### Example:
- Use these rules:
	- A set $S$ is finite if there exists some integer $n$ such that $S$ contains exactly $n$ elements; $||S|| = n$
	- If $S$ and $T$ are both subsets of some set $U$, then $T$ is the complement of $S$ with respect to $U$ if $S \cup T = U$ and $S \cap T = \emptyset$
	- $S \subset U, T \subset U, S \cup T = U, S \cap T = \emptyset, \to T=\overline{S}$

**Theorem 1.5: Let S be a finite subset of some infinite set $U$. Let $T$ be the complement of $S$ with respect to U. $T$ is then infinite**
- Begin by restating each fact of the theorem using definitions
	- $\exists  n \in Z, ||S||=n$ '$S$ is finite'
	- $!\exists p \in Z, ||U||=p$ 'U is infinite'
	- $S \subset U, T \subset U$ 'S and T are subsets of U'
	- $S \cup T = U, S \cap T = \emptyset$ 'T is the complement of S'
### Proof By Contradiction
- Still stuck. Try using **Proof By Contradiction**
	- Assume that the conclusion of the hypothesis is false, that $T$ is finite
	- Prove that the conclusion cannot be false from the given statements
- Let's assume the opposite of Theorem 1.5's conclusion statement is true: $T$ is finite
	- $\exists m \in Z, ||T||=m$
- Now prove that this cannot be true alongside the given statements
1. $S \cup T = U, S \cap T = \emptyset$ given
2. $\exists  n \in Z, ||S||=n$ given
3. $\exists! p \in Z, ||U||=p$ given
4. $\exists m \in Z, ||T||=m$ Assumption
5. $n+m \in z$ From (2), (4) and arithmetic
6. $||U||= n+m$: from (1), (2), (4) and arithmetic
7. (6) contradicts (3), therefore (4) must be false
## 1.2.3 Other Theorem Forms
### If-Then
- There are different ways of saying "if-then"
	- $H$ implies $C$
	- $H$ only if $C$
	- $C$ if $H$
	- Whenever $H$ holds, $C$ follows
### If-And-Only-If Statements
- A statement may sometimes be of these forms:
	- 'A iff B'
	- A if and only if B
	- A is equivalent to B
	- A exactly when B
- This statement is actually two if-then statements ANDed together
	- If A then B
	- If B then A
### Theorems That Appear Not to Be If-Then
**Theorem 1.8: $sin^{2}\theta + \cos^{2}\theta = 1$**
- This theorem appears to not have a hypothesis, but it actually does
- It assumes that $\theta$ is an angle
- Therefore, this statement can be rewritten as:
	- If $\theta$ is an angle, $sin^{2}\theta + \cos^{2}\theta = 1$
# 1.3 Additional Forms of Proof
1. Proofs about sets
2. Proof by contradiction
3. Proof by counterexample
## 1.3.1 Proving Equivalences about sets
- In automata theory, it is a frequent problem to determine whether two sets constructed in two different ways are the same set. 
	- If $E$ and $F$ are expressions representing sets, the statement $E = F$ means the two sets represented are equivalent
	- $\forall x \in E, \ x \in F\  \land \ \forall x \in F, \, x \in E$
- Therefore, the proof that $E = F$ can be shown using the form of an if-and-only-if proof: $x$ is in $E$ if and only if $x$ is in $F$
- This requires proving two statements:
	- $\forall x \in E, \ x \in F$
	- $\ \forall x \in F, \, x \in E$
### Example: Distributive law of unions over intersections
**Theorem 1.10: $\large R \cup (S \cap T) = (R \cup S)\cap(R \cup T)$**
**Proof**
- $E = R \cup (S \cap T)$
- $F = (R \cup S)\cap(R \cup T)$
- Prove $E = F$
First it must be proven that $\forall x \in R \cup (S \cap T), \ x \in (R \cup S)\cap(R \cup T)$:
1. $x \in R \cup (S \cap T)$: given
2. $x \in R\, \lor\,x \in S \cap T$: From (1) and union definition
3. $x \in R\, \lor\,(x \in S \land x \in T)$ From (2) and intersection definition
4. $x \in R \cup S$ From (3) and union definition
5. $x \in R \cup T$ From (3) and union definition
6. $x \in (R \cup S)\cap(R \cup T)$ From (4), (5), and intersection def

Next it must be proven that 
$\forall x \in  (R \cup S)\cap(R \cup T), \ x \in R \cup (S \cap T)$
1. $x \in  (R \cup S)\cap(R \cup T)$: given
2. $x \in R \cup S$: (1) and intersection def
3. $x \in R \cup T$ (1) and intersection def
4. $x$ is either in $R$ or in both $S$ and $T$: (2), (3) and union definition
5. $x \in R \cup (S \cap T)$ (4), (5), intersection/union def

## 1.3.2 The Contrapositive
- Every if-then statement has an equivalent form that may be easier to prove. The *Contrapositive* of the statement "if H then C" is "If not C then not H"
- Consider the following table

| H   | C   | $H\to C$ holds? | $\overline{C} \to \overline{H}$ holds? |
| --- | --- | --------------- | -------------------------------------- |
| 0   | 0   | 1               | 1                                      |
| 0   | 1   | 1               | 1                                      |
| 1   | 0   | 0               | 0                                      |
| 1   | 1   | 1               | 1                                      |
- 
	- Note that the only time $H \to C$ does not hold is if H but not C. 
		- H=1;C=0 is invalid. 
	- This means H=0 is the only valid state given C=0. 
	- The only way to make an if-then statement false is for the hypothesis to be true but the conclusion false
		-  This condition is satisfied for the case where H is true but not C for both the given statement and its contrapositive
		- These two statements have the same truth table and are therefore equivalent
### Prove IFF Using Contrapositive
- Suppose we want to prove $E = F$
- This can be done by proving these statements: 
	- $\forall x \in E, \ x \in F$
	- $\forall x \in F, \, x \in E$
- By putting one of these directions into the contrapositive, we have
	- $\forall x \in E, \ x \in F$
	- $\forall x \notin E, \ x \notin F$
- This gives us more options
## 1.3.3 Proof By Contradiction
- Another way to prove "if *H* then *C*" is to prove the statement:
	- "H and not C implies falsehood"
	- "H and not C cannot be true"
- That is, start by assuming both the hypothesis *H* and the negation of the conclusion *C*
	- $H \land \overline{C}$
- Complete the proof by showing that something known to be false follows logically from "H and not C"

Prove **Theorem 1.5 $U$ is an infinite set, $S$ is a finite subset of $U$ and T is the complement of $S$ with respect to $U$, $T$ is infinite**
1. $\exists! p \in Z, ||U||=p$ given
2. $\exists  n \in Z, ||S||=n$ given
3. $S \subset U$: given
4. $S \cup T = U, S \cap T = \emptyset$ given
5. $\exists  m \in Z, ||T||=m$ assume
6. $||S \cup T||=m+n$: (4) and arithmetic/union def
7. $m+n \in Z$: arithmetic
8. $||U|| = m+n$ (4),(6)
9. $||U|| \in Z$ (7),(8)
10. (9) contradicts (1) therefore (5) is false
11. $T$ is infinite (1),(2),(3),(4),(10)

## 1.3.4 Counterexamples
### Theorem Vs. Observation
- A Theorem must hold true for an infinite number of cases, perhaps all values of its parameters
- A statement is a theorem if it has an infinite number of cases
- A statement is an *Observation* however if it has no parameters or only applies to a finite number of values of its parameters
- It is sufficient to show that a theorem is false in any one case in order to show that it is not a theorem
### Example:
**Alleged Theorem 1.14: There is no pair of integers *a* and *b* such that $a \% b = b \% a$**
**Disproof:** if $a=b$, $a\ mod\ b = b\ mod\ a = 0$

'**Theorem 1.15: a mod b = b mod a if and only if a = b**
**Proof:**
- If part: if a=b a%b = b%a
	1. $a = b$ given
	2. $x\ mod\ x = 0\ \forall x \in Z$
	3. $a\ mod\ b = b\ mod\ a$
- Only if part: if a%b=b%a a=b
	1. $a\ mod\ b = b\ mod\ a$ given
	2. $a \neq b$ assumption
	3. $a < b$ assumption that meets (2)
	4. $a\  mod\ b = a$: rules of mod
	5. $b\ mod\ a < a$: rules of mod
	6. $b\ mod\ a < a = a\ mod\ b$ (4), (5), and arithmetic
	7. (6) contradicts (2) therefore if $a\ mod\ b = b\ mod\ a$ then $a=b$
# 1.4 Inductive Proofs
- The inductive proof is essential when dealing with recursively defined objects
## 1.4.1 Inductions on Integers
- Suppose there is some statement $S(n)$, about an integer $n$, to prove. The common approach is to prove two things:
	1. The *basis*, where we show $S(i)$ for a particular integer $i$, typically with $i=1$ or $i = 0$
	2. The *Inductive step*, where we assume $n \geq i$ and show that if $S(n)$ then $S(n+1)$
- By proving these two statements, we can prove that $S(n)$ is true for all integers $n \geq i$
	- This is called **The Induction Principle**
### Example:
**Theorem 1.16:** $$\forall n \geq 0; \ \sum_{i=1}^{n}i^{2}= \frac{n(n+1)(2n+1)}{6}$$
**Basis:**
1. Assume $n=0$
2. $\sum_{i=1}^{n}i^{2}=0$
3. $\frac{n(n+1)(2n+1)}{6}=0$
4. Thus, $S(0)$ is true
**Induction**:
1. Assume $n \geq 0$
2. Assume $S(n)$ is true
3. Assume $k=n+1$
4. From sum rules: $$\sum_{i=1}^{n+1}i^{2}= (n+1)^{2} + \sum_{i=1}^{n}i^{2}$$
5. From the inductive step: $$\sum_{i=1}^{n+1}i^{2}= (n+1)^{2} + \frac{n(n+1)(2n+1)}{6}$$
6. $$\sum_{i=1}^{n+1}i^{2} = n^{2}+ 2n + 1 + \frac{2n^{3}+3n^{2}+n}{6}$$
7.  $$\sum_{i=1}^{n+1}i^{2} = \frac{6n^{2}+ 12n + 6}{6} + \frac{2n^{3}+3n^{2}+n}{6}$$
8.  $$\sum_{i=1}^{n+1}i^{2} = \frac{2n^{3}+9n^{2}+13n+6}{6}$$
9. Using simple polynomial algebra, this inductive step is proven

## 1.4.2 More General Forms of Integer Inductions
- Sometimes an inductive proof is only possible when using a more general scheme than:
	- Prove that $S(i)$ and "If $S(n)$, then $S(n+1)$" thus $\forall n\geq i\,, S(n)$
- There are two important generalizations
	- **1.** We can use several base cases. We prove $S(i), S(i+1),\dots,S(j)$ for some $j \geq i$
	- **2.** We can use the truth of all statements $S(i),S(i+1),\dots,S(n)$ to prove $S(n+1)$, rather than just using S(n)
### Sum of 3's and 5's Example
**Theorem 1.18: if $n \geq 8$, n can be expressed as the sum of 3's and 8's**
$\forall n \geq 8,\,n=3a+5b,\, a,b,n\in Z$
**Basis:**
1. $8=5+3\therefore S(8)$
2. $9=3*3 + 0*5 \therefore S(9)$
3. $10 = 0*3 +2*5 \therefore S(10)$
**Induction**
1. Assume $n \geq 10$ and $S(8),S(9),S(10)\dots S(n)$
2. $n-2 \geq 8 \therefore S(n-2)$
3. $n-2=5a+3b$ 
4. $n+1=5a+3b+3=5a+3(b+1)$
5. $b+1 \in Z$
6. if $S(n-2)$ then $S(n+1)$
Thus $S(n)$ if $n \geq 8$
- Note that in this case, the hypothesis holds for all $n \geq 8$
- However, proving the inductive step from $n \geq 8$ would not be possible
- This is because the inductive step makes statements about values below the starting point of n, for which $S(n)$ does not hold when $n \geq 8$
- Thus, we needed to use the generalizations discussed above to prove this theorem
## 1.4.3 Structural Inductions
- In automata theory, there are many recursively defined structures. For example, trees and expressions.
-  It's important to note that inductive proofs are like recursive functions
- Like inductions, recursive definitions have a base case, where one or more elementary structures are defined, and an inductive step, where more complex structures are defined in terms of these elementary structures
### Example: Defining Trees
**Basis:**
1. A single node is a tree
2. That node is the root of the tree
**Induction:** If $T_{1},T_{2},\dots,T_{k}$ are trees, then a new tree can be formed as follows
1. Begin with a new node $N$, which is the root of the tree
2. Add copies of all trees $T_{1},T_{2},\dots,T_{k}$
3. Add edges from node $N$ to the roots of each of the trees $T_{1},T_{2},\dots,T_{k}$
### Example: Defining expressions using + and *
**Basis: Any number or letter (var) is an expression** 
**Induction: if $E$ and $F$ are expressions, then so are $E+F,\,$*

$\forall x \in \mathbb{Z},1|x$
From textbook #Intro-Automata-Theory 