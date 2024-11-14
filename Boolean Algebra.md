# Boolean Algebra
Related to [[Gate Symbols]]
Related to [[Proofs and Truth Value]]
- Symbols: For 2 booleans a and b:
	- a AND b -> ab, a\*b
	- a OR b -> a + b
	- NOT a ->  $\overline{a}$
- All algebraic rules apply to boolean algebra
	- Commutation:
		- z = ab + ac = a(b+c)
			- z = a AND (b OR C)
			- Same as z = a AND b OR a AND c
- BA Axioms (MUST MEMORIZE THESE)
	1. **Binary Field Axiom**: B = 0 <=> B $\neq 1$
	2. **NOT Axiom**: $\overline{0} = 1 ;  \overline{1} = 0$
	3. **AND/OR Axiom**: 0 * 0 = 0; 1 + 1 = 1
	4. **AND/OR Axiom**: 1 * 1 = 1; 0 + 0 = 0
	5. **AND/OR Axiom:** 1 * 0 = 0 * 1 = 0; 0 + 1 = 1 + 0 = 1;
	- First statement is $A_n$ , second is $A_{n}^{'}$
- BA Theorems:
	1. **Identity**: B * 1 = B ; B + 0 = B
	2. **Null Element**: B * 0 = 0; B + 1 = 1
	3. **Idempotency**: B * B = 1; B + B = B
	4. **Identity:** $\overline{\overline{B}} = B$
	5. **Complement**: $B * \overline{B} = 0$; $B + \overline{B} = 0$
	6. **Commutativity**: A * B = B * A; A + C = C + A
	7. **Associativity**: (A * B) * C = A * (B * C) ; (A + B) + C = A + (B + C)
	8. **Distributivity:** (B * C) + (B * D) =B(C + D) ; (B + C ) * (C + D) = B (C * D)

- Examples:
	- F = $AB + A\overline{B}$
		- F = $A(B + \overline{B})$
		- F = A * 1
		- **F = A**




i|i|i|i|o
-|-|-|-|-
0|0|0|0|0
0|0|0|1|1
0|0|1|0|2
0|0|1|1|12
0|1|0|0|3
0|1|0|1|13
0|1|1|0|23
0|1|1|1|123
1|0|0|0|4
1|0|0|1|14
1|0|1|0|24
1|0|1|1|124
1|1|0|0|34
1|1|0|1|134
1|1|1|0|234
1|1|1|1|1234


Continues [[Boolean Algebra]]
Continued by [[Kmaps]]
Continued by [[Sequential Timing Diagrams]]
For class #Logic-Systems-1