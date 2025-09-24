Continues [[The DFT]]
- ## Matrix Form
	- ![[Pasted image 20240213105322.png]]
	- How many multiplications?
		- No multiplications, just 3 operations on $x[n]$
			- Multiply by 1, swap real and imaginary registers, swap registers and flip sign bit
	- Notice that this matrix of $W_{N}^{n}$ is constant for all $x[n]$ of length $N$
		- Lookup table 
	- The FFT is so fast because it only requires 3 different operations to generate the summable sequence
	- $$\overline{X}=\overline{\overline{W}}\overline{x}$$
	- 
For class #digital-signal-processing 