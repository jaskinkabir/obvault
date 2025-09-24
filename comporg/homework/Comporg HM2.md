Jaskin Kabir
801186717
Uses [[Binary Integer Division]]
1. Convert 5ED4 into a binary number. What makes base 16 (hexadecimal) an attractive numbering system for representing values in computers? (20 points)
	1. Hexadecimal is easily converted into binary by simply converting each individual digit into its binary representation $5ED4_{16} = 1001 1110 1101 100_{2}$
	2. Hexadecimal is an attractive numbering system because each hex digit represents half a byte of data, and an entire byte can be represented by just two digits. A 32 bit LEGv8 instruction can be represented by just eight hex digits.
2. Write down the binary representation of the decimal number 63.25 assuming the IEEE 754 single precision format. (20 points)
	1. $63_{10}=0011\ 1111_{2}$
	2. $0.25_{10}=0.01_{2}$
	3. $63.25_{10}=00111111.0100_{2}$
	4. $=1.1111101 \times 2^{5}$
	5. $S=0,\, F=11111010000000000000000$
	6. $E_{T}=5,\,E_{R}=132,\,E=10000100$
	7. $63.25_{10}=01000010011111010000000000000000_{FP}$
3. Using a table shown, calculate 60 divided by 17. You should show the contents of each register on each step. Assume A and B are unsigned 6-bit integers. The hardware that does the division is shown in the figure below for reference. (30 points) 
	1. ![[Pasted image 20241018125434.png]]

| Step | Action                                   | Remainder Register | Divisor Register | Quotient | Remainder |
| ---- | ---------------------------------------- | ------------------ | ---------------- | -------- | --------- |
| 0    | Init                                     | 000000 111100      | 010001           | 111100   | 000000    |
| 1    | $R=R-D,\,R=R < 0 ?\ R+D:\, R+1,\,R\ll=1$ | 000000 111100      | 010001           | 111100   | 000000    |
| 2    | $R=R-D,\,R=R < 0 ?\ R+D:\, R+1,\,R\ll=1$ | 000001 111000      | 010001           | 111000   | 000001    |
| 3    | $R=R-D,\,R=R < 0 ?\ R+D:\, R+1,\,R\ll=1$ | 000011 110000      | 010001           | 110000   | 000011    |
| 4    | $R=R-D,\,R=R < 0 ?\ R+D:\, R+1,\,R\ll=1$ | 000111 100000      | 010001           | 100000   | 000111    |
| 5    | $R=R-D,\,R=R < 0 ?\ R+D:\, R+1,\,R\ll=1$ | 001111 000000      | 010001           | 000000   | 001111    |
| 6    | $R=R-D,\,R=R < 0 ?\ R+D:\, R+1,\,R\ll=1$ | 001101 000001      | 010001           | 000001   | 001101    |
| 7    | $R=R-D,\,R=R < 0 ?\ R+D:\, R+1,\,R\ll=1$ | 001001 000011      | 010001           | 000011   | 001001    |
	This shows that the result of the division is $60 / 17 = 3r9$

1. Write down the binary representation of the decimal number 63.25 assuming the IEEE 754 double precision format. Show the double precision format and also indicate the mantissa, exponent and the sign bit in it. (20 + 10 points)
	1. To convert between single and double precision, simply extend the mantissa with 29 0s on the right. To convert the exponent field, the bias is now 1023 rather than 127.
	2. $63.25_{10}=$
	3. $0\| 100000\ 00100\| 1111\ 10100000\ 00000000\ 00000000\ 00000000\ 00000000\ 00000000|$
		1. Format is Sign||Exponent||Mantissa||
	4. =0X404FA00000000000

For class #comporg/homework