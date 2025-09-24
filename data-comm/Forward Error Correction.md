Chapter 6.6 
Continues [[Types of Errors and Error Detection Schemes]]
# Need for Error Correction
- Error detection can be used to detect error and request retransmission of a frame when there is an error. However this is inadequate with wireless networks
	- The BER on a wireless link can be quite high, which would result in too many retransmissions
	- The propagation delay in some cases, like in satellite links, can be much longer than the transmission time of a single frame. In this case, it is impractical to retransmit so many frames
# FEC Operation
![[Pasted image 20240801185746.png]]
- On the transmission end, each $k$-bit block of data is mapped onto an $n$-bit block ($n>k$) called a **codeword**, using an FEC encoder
- The receiver then decodes this codeword with four possible outcomes
	- **No errors**: The input to the FEC decoder is identical to the original codeword, and the decoder produces the original data block
	- **Detectable, correctable errors:** The FEC decoder can map the incorrectly transmitted codeword onto the original data block
	- **Detectable uncorrectable errors:** The decoder will simply report an uncorrectable error
	- **Undetectable errors:** The decoder will map the codeword onto a data block that differs from the original data block
# Hamming Codes/ Block Error-Correcting Codes
- The hamming distance $d(v_{1},v_{2})$ between two $n$-bit binary sequences $v_{1}$ and $v_{2}$ is the number of bits in which they disagree![[Pasted image 20240801190009.png]]
- The Hamming scheme involves defining $2^{k}$ unique $n$-length codewords that correspond to each data block that can be transmitted
- If the received $n$-bit data block does not match any of these codewords, we can assume that the original data block corresponds to the codeword with the smallest hamming distance to the received block. 
	- ![[Pasted image 20240801190255.png]]
	- If the received codeword is 00100, we can see that the hamming distance between this received codeword and the codeword for the data block 00 is only 1. Thus, the original data block was probably 00
- However, this method only works if each invalid codeword has only one valid codeword at a minimum hamming distance away.
	- If there are multiple valid codewords each at an equal minimum distance away from the invalid codeword, this is a detectable, uncorrectable error.
- Using the codeword scheme listed above, the following table can be constructed with invalid codewords and the minimum distance between it and valid codewords
	- ![[Pasted image 20240804153140.png]]
	- Note that all single bit errors point to a single valid codeword
		- This code can correct all single bit errors
	- All double bit errors point to two different valid codewords
		- All double bit errors are detectable but uncorrectable
		- 
## Code Characteristics
- An ($n,\ k$) block code encodes $k$ data bits into $n$ bit codewords. Typically, each valid codeword reproduces the original $k$ data bits and appends $n-k$ check bits to the overall codeword. 
- Thus, an $(n,k)$ block code has $2^{k}$ valid codewords out of $2^{n}$ possible codewords
	- The ratio of redundant bits to data bits $\frac{n-k}{k}$ is called the **redundancy** of the code
	- The ratio of data bits to total bits, $\frac{k}{n}$ is called the **code rate**
- Code rate is a measure of how much additional bandwidth is required to carry data at the same rate as without the code
- For example, a code rate of 1/2 requires double the bandwidth
- Our example above has $n=5,k=2,\ \frac{k}{n}=\frac{2}{5}$
	- Thus the block code above requires 2.5x the capacity of an uncoded system
### Code Capabilities
- If we define a metric $d_{min}$ as the minimum hamming distance between valid codewords, we can derive the following characteristics of the code
- For a given integer $t$, the code can correct all bit errors up to and including errors of $t$ bits if $$d_{min}\geq (2t+1)$$
- All errors $\leq t-1$ bits can be corrected and errors of $t$ bits can be detected but not, in general, corrected if $$d_{min}\geq 2t$$
- In general, the maximum number of guaranteed correctable errors per codeword is given by the following equation $$t=\lfloor \frac{d_{min}-1}{2}\rfloor$$
	-  floor operation
- The number of errors $t$ that can be detected but not necessarily corrected is given by $$t=d_{min}-1$$
	- This can be intuitively seen by considering that, if $d_{min}$ errors occur, one codeword can be changed into another. Thus, $d_{min}-1$ is the maximum amount of errors that can occur to one codeword without transforming it into another valid codeword
## Designing a Block Code
- For given values $n,k$ we want the largest possible value of $d_{min}$
- The code should be relatively easy to encode and decode, requiring minimal memory and processing time
- The number of extra bits $n-k$ should be small enough to control bandwidth requirements
- $n-k$ should be large enough to significantly reduce error rate
## System Performance Improvement
![[Pasted image 20240804155516.png]]
- In the region of coding gain, the encoding system achieves a lower Bit Error Rate for the same EbN0 as the unencoded system.
	- Note that below a certain threshold, the energy per data bit is so low that the additional overhead required by the coding system actually degrades performance when compared to the coding system
- The reduction in EbN0 achieved by coding for the same Bit Error Rate, in dB, is referred to as **Coding Gain**

For class #data-comm