Jaskin Kabir 801186717
Uses [[Internet Checksum]]

1.  For P = 110011, D = 11100011, Use CRC to find FCS
	1. If using Modulo 2
		1. $k=8$
		2. $n-k+1=6=n-8+1,n=13$
		3. ![[Pasted image 20240729023852.png]]$$FCS=11010$$
	2. If using polynomial division
		1. $2^{n-k}D=1110001100000$
			1. $D=5,6,10,11,12 x^{12}+x^{11}+x^{10}+x^{6}+x^{5}$
			2. $P=x^{5}+x^{4}+x+1$
		2. ![[Pasted image 20240729022906.png]]$$FCS=11010$$
		3. 
2. Suppose that the following block of 16 bits is to be sent using a checksum of 8 bits: 01011101 00110110.
	1. Find the transmitted bit sequence with checksum.
		1. $01011101+00110110=10010011$
		2. $~10010011=01101100$
		3. $$T=01011101\ 00110110\ 01101100$$
	2. Now bits are numbered from #1 to #16, counting from the left of the block. Assume that there is an error burst of 4 bits in the channel that affects the received bits #6 through #9. Determine if the receiver will be able to detect the errors by performing the checksum computation at the receiver on the corresponding received sequence. Clearly show the transmitted, received, and checksum obtained at the receiver. (Hint: bit 6, 7, 8, and 9 are received with error: send 1, received 0; send 0, received 1)
		1. $01011101\ 00110110 \oplus {00000001\ 11100000}= 01011100\ 11010110$
		2. $01011100+11010110=00110011$
		3. $~00110011=11001100$
		4. Received Checksum = $11001100$
		5. ![[Pasted image 20240729031819.png]]
		6. **The checksums are different, so the error will be detected.**
3. Two stations A and B ate communicating with error detection function. A want to send the data bits of D =1000 0110 1010 1100 1101. What is the data bits to send to B? 
	1. If using the odd parity check technique. 
		1. Assuming 4 bit data blocks:
		2. **10000 01101 10101 11001**
	2. If using the even parity check technique. 
		1. Assuming 4 bit data blocks:
		2. **10001 01100 10100 11000**
	3. If using the two-dimensional odd parity check technique 
		1. **1000 1011 0010 1011 0011 0011 011**
	4. If using the two-dimensional even parity check technique
		1. **1000 0011 0110 1011 0011 0010 100**
For class #data-comm/homework