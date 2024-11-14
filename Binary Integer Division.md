Continues [[Binary Integer Multiplication]]
Continued by [[Storing Fractional Numbers]]
# Notation
- $$\frac{\text{Dividend}}{\text{Divisor}}=\text{Quotient}$$
- $\text{Dividend}=\lfloor\text{Quotient}\rfloor \times \text{Divisor}+\text{Remainder}$
# Binary Long Division On Paper
1. Check if the divisor can divide the first digit of the dividend
	1. If yes, subtract and make this the new first section of the dividend. Add a 1 to the quotient
	2. If no, add a 0 to the quotient
2. Pull the next bit down from the dividend and repeat
3. ![[Pasted image 20241017194558.png]]
# Restoring Division Algorithm
- Instead of pulling bits down left to right from the dividend (shifting left), we can instead shift the divisor to the right across the dividend for the same effect
## Hardware Implementation
![[Pasted image 20241017182514.png]]
- For $n$ bit numbers, the Divisor and Remainder registers must be $2n$ bits wide, the quotient will be $n$ bits wide
- Initialize the system by placing the divisor in the left half of the divisor register
	- $D = \text{Divisor} \ll n$
- Place the dividend in the remainder register
	- $R=\text{Remainder}$
- Set the quotient to 0
	- $Q=0$
- Set the iteration counter to 0
	- $i=0$
- The following steps will then repeat $n+1$ times:
1. Increment the counter
	1. $i=i+1$
2. Subtract the divisor from the remainder and place it in the remainder register
	1. $R=R-D$
3. Check if the Remainder Register is positive: $R \geq 0?$
	1. If it is, shift the quotient left and add 1
		1. $Q=Q\ll 1 + 1$
	2. If not, restore the remainder value by adding the divisor to the register. Shift the quotient left
		1. $R=R+D,\,Q = Q \ll 1$
4. Shift the divisor register right
	1. $D= D \gg 1$
5. Check if the counter is $n+1$
	1. If it is, end execution
	2. Otherwise repeat

- Divisor = $D$ Remainder = $R$ Quotient = $Q$

| Step                      | Divisor  | Remainder | Quotient |
| ------------------------- | -------- | --------- | -------- |
| Init                      | 01010000 | 00001110  | 00000000 |
| $R=R-D$                   | 01010000 | -01000010 | 00000000 |
| $R=R+D,\,Q = Q \ll 1 + 0$ | 01010000 | 00001110  | 00000000 |
| $D=D\gg 1$                | 00101000 | 00001110  | 00000000 |
| $R=R-D$                   | 00101000 | -00011010 | 00000000 |
| $R=R+D,\,Q = Q \ll 1 + 0$ | 00101000 | 00001110  | 00000000 |
| $D=D\gg 1$                | 00010100 | 00001110  | 00000000 |
| $R=R-D$                   | 00010100 | -00000110 | 00000000 |
| $R=R+D,\,Q = Q \ll 1 + 0$ | 00010100 | 00001110  | 00000000 |
| $D=D\gg 1$                | 00001010 | 00001110  | 00000000 |
| $R=R-D$                   | 00001010 | 00000100  | 00000000 |
| $Q=Q\ll 1+1$              | 00001010 | 00000100  | 00000001 |
| $D=D\gg 1$                | 00000101 | 00000100  | 00000001 |
| $R=R-D$                   | 00000101 | -00000001 | 00000001 |
| $R=R+D,\,Q = Q \ll 1 + 0$ | 00000101 | 00000100  | 00000010 |
| $D=D\gg 1$                | 00000010 | 00000100  | 00000010 |
| Done                      | 00000010 | 00000100  | 00000010 |
Result is $14 / 5=2r4$

## Improved Division Hardware
![[Pasted image 20241017201014.png]]
- This design combines the quotient and remainder registers and halves the width of the divisor register and ALU
	- Note that this is the same hardware required by the improved multiplier
- It speeds up the application by shifting the quotient and operands simultaneously
- The new steps are as follows
- Initialization:
	- $R=\text{dividend}$
	- $D=\text{Divisor}$ 
	- $i=0$
1. $R=R\ll 1$
2. $R=R-D\ll n$
3. $R=R\geq 0?\ R+1 : R+D\ll n$
4. $i=i+1$
5. $i==n?$
	1. Stop
	2. Else Repeat
- The quotient is now the right half of $R$, and the remainder is the left half
	- $\text{Quotient} = R\ \&\ !(2^{n-1}\ll n)$
	- $\text{Remainder}=R\gg n$
### Python Version
```python
def bin_div(divid, divis, n):

    R=divid

    D=divis<<n

    for i in range(0,n):
        R <<= 1
        R -= D
        
        if R >= 0:
            R = R + 1
        else:
            R += D
            
    quotient = R & ~((2**n-1)<<n)

    remainder = R>>n
```
# Signed Division
- Simply remember the signs of the divisor and dividend and then perform division on the absolute values. Determine whether the quotient or remainder should be negated with the following rules
	- $S_{\text{Result}} = S_{\text{Divisor}} \oplus S_{\text{Dividend}}$
	- $S_{\text{Remainder}}=S_{\text{Dividend}}$
- This second rule is in place to resolve ambiguity
	- $7r2=11r-2$

# LEGv8 Division Instructions
- SDIV
	- Signed
- UDIV
	- Unsigned
For class #comporg