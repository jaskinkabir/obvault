Chapter 6.1-6.2
Related to [[TCP-IP Protocol Architecture]]\
Continued by [[Parity Checking]]
Continued by [[Internet Checksum]]
Continued by [[Cyclic Redundancy Check (CRC)]]
Continued by [[Forward Error Correction]]

# Error Types
![[Pasted image 20240731191633.png]]
## Single Bit Error
- Just one bit is flipped, and does not fall within the Burst Error criteria
- Can occur in the presence of white noise, when a slight random deterioration of the SNR is enough to confuse the receiver's detection of a single bit
## Burst Error
- A group of transmitted bits that follows the two criteria, and is specified by the integer parameter $x$ that is referred to as the *guard band*
	- The first and last bits of the burst are in error
	- There is no contiguous correctly transmitted stream of length $x$ or greater
	- There are at least two bit errors within the burst
- Can be caused by impulse noise
- More common and more difficult to deal with than single bit error
- The effects of burst errors are greater at higher data rates
# Error Detection
## Probabilities
- $F$: # of Bits in a frame
- $P_{b}$: The probability that any bit in a frame is received in error; aka BER
- $P_{1}$: Probability that the entire frame arrives with no bit-errors
	- Probability that there are no errors at all, detected or not thus $$P_{1}=(1-P_{b})^{F}$$
- $P_{2}$ Probability that, with some error detection algorithm in use, a frame arrives with one or more undetected errors
	- Probability that there are (1) errors where some or all of them pass (2) undetected
- $P_{3}$: The probability that, with some error detection algorithm in use, a frame arrives with one or more detected errors but no undetected bit-errors
	- Probability that there are (1) errors that are (2) all detected
- Assume that there is no error detection scheme
	- The probability of detected errors is $P_{3}=0$
	- The probability that the entire frame is error free is $P_{1}=(1-P_{b})^{F}$
		- Decreases as BER increases
		- Also decreases as $F$ increases; More bits, more opportunities for bit errors
	- The probability that there are undetected errors is therefore then the opposite $P_{2}=1-P_{1}$
## Error Detection Process
- Transmitter is to transmit data packet $D$ of length $k$
- The transmitter generates an $n-k$ bit error detection code  $E=f(D)$, 
	- Where $n$ is the total length of the transmitted frame in bits
	- Typically $(n-k)<k$
	- Where $f$ is some error detection function $f:n\to n-k$
	- $E$ is referred to as the **error-detecting code** or the **check bits**
- The transmitter sends a frame of $n$ bits that comprises $D*2^{n-k}+E$
- The receiver passes the received data $D'$ through the same function to generate $E'=f(D')$
- If $E'==E$, no errors have been detected

For class #data-comm