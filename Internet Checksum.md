Chapter 6.4
Continues [[Types of Errors and Error Detection Schemes]]
For class #data-comm
- Used in IP, TCP, and UDP
# Internet Checksum Method
- Split frame into words
- Add all words together with wraparound carry
	- If there is a carry bit, add 1 to the sum to keep the number of bits the same
- Invert all bits of this sum (take one's complement)
- Append this sum to the end of the frame
# Notes
- Note that the checksum is the same size as the word size. Thus $n-k$ is the word size
- To verify proper transmission, the receiver takes the sum of all words, including the checksum, with wraparound carry 
	- If this sum results in a word of all 1s, no errors are detected
	- Intuitively, taking the the sum of all words of $D$ results in some value $C$. Taking the ones complement in this case can be seen as negating C, thus the checksum equals $-C$
		- If you were to add these two together on the receiver side, you would get $C+-C=0$. In ones-complement arithmetic, $0$ is all ones
		- Another way to think about it, is that if you flip every bit of $C$ to get $-C$, the only possible value of $C-C$ must be all ones
- This scheme is very simple, just involving simple addition and comparison operations. It takes place at the higher level of the internet layer as an added redundancy on top of the lower data-link level's CRC scheme. 
- 