Chapter 6.3
Continues [[Types of Errors and Error Detection Schemes]]
### One-Dimensional Parity Check
- Add a single parity bit to the end of a block of data that ensures the number of ones in the frame is either even or odd
- If any even number of bits are inverted, the error goes undetected. 
	- You can do some funny combinatorics to figure out $P_{2}$ here, but it is not 0
- Even parity is used for synchronous transmission, odd for asynchronous
### Two-Dimensional Parity Check
- The string of data to be checked is arranged into a two-dimensional array.
- Appended to each row $i$ is an even parity bit $r_{i}$ for that row
- Appended to each row $j$ is an even parity bit $c_{j}$ for that column
- An overall even parity bit $p$ completes the matrix. Thus the error detecting code consists of $i+j+1$ parity bits, and 
	- $n-k=i+j+1$
- If any even number of bits in a row are flipped, the errors are detected by the column parity bits. However, if any pattern of four error bits forms a rectangle, the error is undetectable.
- ![[Pasted image 20240731194242.png]]

For class #data-comm