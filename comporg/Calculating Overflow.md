010001100
-01000110 70 
-01000110 70
-10011000 -104

101110100
-10111010 -70
-10111010 -70
-01110100 116

000111100
–01000110 70
–00011110 30
–01100100 100


111000100
–10111010 -70
–11100010 -30
–10011100 -100

111000000
–01100000 96
–10100000 -96
–00000000 0


- Overflow happens during sign corruption
	- The addition causes two negative numbers to result in a positive sum or vice versa
- Add 2 positive numbers, $Co_{n-1}=0$
	- Where $n=$# of bits
	- This is because $a_{n-1}$ and $b_{n-1}$ are both 0
		- Thus $S_{n-1}=0$ before carry evaluation
	- In order for $S_{n-1}$ to remain 0, there cannot be a carry from $Co_{n-2}$
		- Changing a 0 to a 1 adds a positive number to the value. For positive numbers, this pushes the value further away from 0
	- The corruption condition is when 
- Add 2 negative numbers, $C_{n-1}=1$
	- This is because $a_{n-1}$ and $b_{n-1}$ are both 1
		- Thus $S_{n-1}=0$ before carry evaluation
	- In order for $S_{n-1}$ to remain 1 to preserve sign, there must be a carry from $Co_{n-2}$
		- Changing a 0 to a 1 adds a positive number to the value. For negative numbers, this brings the value closer to zero
- So the condition $O=C_{n-1}  \oplus C_{n-2}$ implements the following condition

```C++
bool compute_overflow(int a[8], int b[8], int Cout[8]) {
	if a[7] != b[7] return 0; // Positive and negative addition cannot overflow
	return a[7] == 1 ? ()
}
```

For class #comporg