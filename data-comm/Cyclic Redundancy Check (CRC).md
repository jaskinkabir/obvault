Continues [[Types of Errors and Error Detection Schemes]]
Uses [[Boolean Algebra]]
Chapter 6.5
For class #data-comm

# CRC
- One of the most powerful and most common edc (error-detecting code)
- Given a $k$ bit block of bits, the transmitter generates an $n-k$ bit sequence known as the **FCS (Frame Check Sequence)** such that the resulting $n$-bit long frame is divisible by some predetermined number
- The receiver divides the total $n-$bit long frame and if there is no remainder, no errors are detected
## Variables
- $T=n$-bit frame to be transmitted
- $D=k$-bit block of data or message; the first $k$ bits of $T$
	- $D_{s}=2^{n-k}D$
- $F=(n-k)$-bit FCS; the last $(n-k)$ bits of $T$
- $P=$pattern of $n-k+1$ bits; the predetermined divisor
## Operation
- The objective is to append $F$ to $D$ such that $\frac{T}{P}$ has no remainder. $$T=2^{n-k}D+F$$
	- Left shift D to accommodate the size of F
- The method of finding $F$ involves dividing $2^{n-k}D$ by $P$ and then adding the remainder. Division of this sum will yield no remainder
## Error Detection Power
- If some error affects the transmission, it can be represented by the bitmask $E$, which has ones in the positions of each bit flip
- Thus we can define an error-ed $T_{r}=T \oplus E$
- Since XOR is the same thing as addition/subtraction in mod 2 arithmetic, the error would only be undetected if $E$ is divisible by $P$
## Choosing the Pattern P
- At minimum, the first and last bits of $P$ must be 1
- In polynomial notation, $P$ is typically of one of the following forms:
	- $P(x)=q(x)$
	- $P(x)=(x+1)q(x)$
	- Where $q(x)$ is a primitive polynomial
- An error $E(X)$ will only be undetectable if it is divisible by $P(X)$ from this, we can deduce that all of the following errors are detectable by a suitably chosen $P(X)$
	- All single bit erros, if $P(X)$ has more than one nonzero term
	- All double-bit errors if $P(X)$ is one of the two above forms
	- Any odd number errors, so long as $P(X)$ contains a factor $(X+1)$
	- Any burst error for which the length of the burst is at most $n-k$
	- A fraction of error bursts of length $n-k+1$
		- This fraction is $1-2^{k+1-n}$
	- A fraction of error bursts of length greater than $n-k+1$
		- This fraction is $1-2^{k-n}$
- IF all error patterns are considered equally likely, then for a burst error of length $r+1$, the probability of an undetected error is $(\frac{1}{2})^{r-1}$ and for a longer burst the probability is $\left( \frac{1}{2} \right)^{r}$ where $r$ is the length of the FCS ($n-k$)
- ![[Pasted image 20240801183842.png]]
	- The degree of the polynomial is the bit length of the resulting FCS
	- The CRC-12 system is used for transmission of streams of 6-bit characters and generates a 12-bit FCS. Both CRC-16 and CRC-CCITT are popular for 8-bit characters in the United States and Europe, respectively, and both result in a 16-bit FCS. This would seem adequate for most applications, although CRC-32 is specified as an option in some point-to-point synchronous transmission standards and is used in IEEE 802 LAN standards.
# CRC Methods
## Modulo 2 Arithmetic
- Setup the long division notation 
- Copy $P$ aligned under the leftmost bit of $D_{s}$
- Apply the xor operation to each bit
- Cross out any leading zeros and pull down an equal number of bits from $D_{s}$
- Repeat until no more bits can be pulled down
- ![[Pasted image 20240801182407.png]]
## Polynomial Long Division
- Express all values as polynomials with binary coefficients. 
- Perform polynomial long division to find $F$
## Digital Logic
- CRC can be implemented using a shift register that is $n-k$ bits wide, an SPDT switch, and a number of $n-k$ XOR gates
- ![[Pasted image 20240801184501.png]]