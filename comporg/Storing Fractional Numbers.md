Continues [[Binary Integer Division]]
Continued by [[Floating Point Arithmetic]]
# Fixed Point
- For an $N$-bit fixed point number, choose some number $M<N$ where the representation will be split into the integer and fractional components
	- For example, an 8 bit fixed point number could be split into two 4-bit numbers where the final 4 represent a fractional component
- Convert the integer component into an $M$-bit binary integer
- The fractional component is more complicated
- Recall that each digit of an unsigned integer represents the coefficient of $2^{n}$
	- $11_{10}=1011_{2}$
		- $=1\times2^{3}+0 \times 2^{2} + 1 \times 2^{1} + 1 \times 2^{0}$
- Simply expand that below $n=0$
	- $11.6875_{10}=1011.1011_{2}$
		- =$1\times2^{3}+0 \times 2^{2} + 1 \times 2^{1} + 1 \times 2^{0}$
		- $+1 \times 2^{-1}+ 0 \times 2^{-2}+ 1 \times 2^{-3} + 1 \times 2^{-4}$
## Unrepresentable Numbers
- In decimal, the fraction $\frac{1}{3}$ is not representable with a fixed number of digits
	- This is because no linear combination of the negative powers of 10 can precisely add up to $\frac{1}{3}$
	- But adding more and more digits to the number gets closer and closer to the true value of $\frac{1}{3}$
- Any representation of a fraction has a finite **Precision**
- In binary, the fraction $\frac{3}{10}$ is unrepresentable
	- No linear combination of negative powers of two can add up to 0.3
	- This is where floating point errors come from
	- Adding more bits adds more precision
# Floating Point
- Store these bits
	- 1 sign bit $S$
	- 8 bit exponent $E$
	- 23 bit fraction $F$ (Mantissa)
	- $(-1)^{S} \times F \times 2^{E}$
## Biasing the Exponent
- The exponent field is unsigned
- The values 0 and 255 are excluded from the range
- Let $E_{T}$ represent the true exponent $E_{R}$ represent the value represented by the $E$ field described above
	- Biasing the $E$ field creates the following relation
	- $E_{R}=E_{T}+127$
	- $E_{T}=E_{R}-127$
- The first 127 values are negative, the next 127 are positive
	- $[-126,-1\,]_{T}=[1,\,126]_{R}$
	- $[0,\,127]_{T}=[127,\,254]_{R}$
	- The range of representable exponents is $[-126,\,127]_{T}$
		- An exponent below $-126_{T}$ results in underflow
		- An exponent above $254_{T}$ results in overflow
- Example: Store the value $3 \times 10^{-9}$
	- $S=0$
	- $F=0011_{2}$
	- $E_{T}=-9_{10}$
	- $E_{r}=127-9=118$
	- $E=011 0110_{2}$
	- $R=0\ |0011\ 0110|\ 000\ 0000\ 0000\ 0000\ 0000\ 0011$
# IEEE 754 Floating Point Representation
- Assume that the significand is 1.something
	- Because the significand will always be greater than 1
## Conversion Steps
1. Convert significand and decimal component into binary separately
2. Move decimal point to the left until there is only 1 value to the left of the point
	1. This is the significand
3. Note down the number of shifts happened to the point
	1. This is the exponent
## Single Precision Format:
- 32 bit number
- - Exponent bias is 127
	- $[-126,-1\,]_{T}=[1,\,126]_{R}$
	- $[0,\,127]_{T}=[127,\,254]_{R}$
- Fields:
	- 1 bit Sign
	- 8 Bit Exponent
	- 23 Bit Mantissa
## Double Precision Format
- 64 Bit Number
- Exponent bias is 1023
	- $[-1022,-1\,]_{T}=[1,\,1022]_{R}$
	- $[0,\,1023]_{T}=[1023,\,2047]_{R}$
- Fields
	- 1 bit Sign
	- 11 bit Exponent
	- 52 bit Mantissa
- The exponent does have a larger range but the main precision increase comes from the much larger fraction field

|          | Single Precision | Double Precision |
| :------- | :--------------- | :--------------- |
| Sign     | 1                | 1                |
| Exponent | 8                | 11               |
| Mantissa | 23               | 52               |
| Bias     | 127              | 1023             |


## IEEE 754 Exceptions
- Overflow: A situation in which positive exponent becomes too large to fit into the exponent field
- Underflow: Exponent too small
### Normalization and de/subnorms
- Normalized floating point numbers have the first bit of the significand implicitly set to 1
	- In the number $1.1101 \times 2^{-3}$, the mantissa field would hold $1101$, because the $1.$ is implicit
	- The number is called the significand when this implicit 1 is included, and the fraction when it is not
	- Since the number $0$ has no leading one, it has the reserved exponent value of $0_{R}$ so that hardware does not attach a leading 1 to it for calculations
- However, if some operation results in a number just barely below $1 \times 2^{-126}$, underflow will occur
- In order to gradually allow for smaller values before underflow occurs, the IEE 754 standard includes **Denormalized** numbers, also called denorms or subnorms
	- In these numbers, the exponent field is 0, but the represented exponent is -126
	- The implicit 1 is changed to an implicit 0
	- The smallest normalized single precision number is $2^{-126}$. The smallest denormalized number is $2^{-149}$
### NaN and Infinity
- For invalid operations like 0/0 or $\infty - \infty$, the standard includes a symbol for NaN or Not a Number
- For division by 0, the standard includes a symbol for positive and negative infinity
- Based on the exponent and mantissa values, the different exceptions can be represented as follows:
- ![[Pasted image 20241017230411.png]]
## Why Bias The Exponent?
- The sign bit is the MSB, which makes sorting easier
	- A quick check for <0 or >0
- Placing the exponent before the fraction is also a sorting optimization
	- Simply compare the exponents if the signs are the same. 
	- **This is why two's complement is not used** 
		- 2's complement would require more complex hardware for exponent comparison
For class #comporg