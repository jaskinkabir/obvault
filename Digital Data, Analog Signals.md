Continues [[Transmission Terminology]]
Continues [[Digital Data, Digital Signals]]
Continued by [[Analog Data, Digital Signals]]
CLOSELY Related to [[Digital Radio#Quadrature Amplitude Modulation]]
Uses [[Channel Capacity, Nyquist, Shannon, and EbN0]]
![[Pasted image 20240717210855.png]]

 Transmitting data across analog signals involves **Modulation** of a carrier signal, whereas transmitting data across digital signals involves **Encoding** data onto a series of discrete signal levels, or pulses
# Amplitude Shift Keying
In Binary Amplitude Shift keying, the binary values are represented by two amplitudes of the carrier frequency. Commonly, one is 0 aka DC
$$
s(t)= 
\begin{cases}
A\cos(2\pi f_{c}t) & \text{Binary 1}\\  \\
0 &\text{Binary 0}
\end{cases}
$$
ASK is susceptible to sudden gain changes, and is a rather inefficient modulation technique. On voice-grade lines it is typically only used up to 1200 bps, 1.2Kbps

Used to transmit digital data over optical fiber. For LED transmitters, the above equation is valid. Laser transmitters normally have a fixed bias current that emits a low light level, which represents one signal element. The high light level represents the other.

## QAM
This is used in ADSL (Asymmetric Digital Subscriber Line)
Trig identity for QAM
![[Pasted image 20240718000550.png]]
# Frequency Shift Keying
## BFSK
The most common form of FSK is Binary FSK (BFSK). The two binary values are represented by two different frequencies near the carrier frequency $$
s(t)=
\begin{cases}
A\cos(2\pi f_{1}t) & \text{Binary 1} \\
A\cos(2\pi f_{2}t) & \text{Binary 0}
\end{cases}
$$
$f_{1} \text{ and } f_{2}$ are typically an equal and opposite offset away from $f_{c}$ 
By having multiple carrier frequencies, full-duplex transmission can be achieved on the same line. The two carrier frequencies and their respective offsets must be chosen such that there is minimal overlap between the two bandwidths, for example in Figure 5.8:
![[Pasted image 20240717212102.png]]

BFSK is less susceptible to error than ASK, and is still only used up to 1.2Kbps on voice lines. But it is used for high frequency (3 to 30MHz) radio and even higher frequencies on LAN networks that use coax.

## MFSK
Multiple FSK, or MSFK, is more bandwidth efficient but more susceptible to error. More than two frequencies are used in this scheme, and each signaling element represents more than one bit. 
$$s_{i}(t)=A\cos(2\pi f_{i}t),\, 1 \leq i \leq M$$
Where
- $f_{i}=f_{c}+(2i-1-M)f_{d}$
	- This creates a range of frequencies centered around $f_{c}$. Proven by [desmos](https://www.desmos.com/calculator/czeo4d04n5)
- $f_{d}=$ Difference Frequency
	- The difference between each frequency $f_{i}$ is always $2f_{d}$
- $M=$ Number of signal elements = $2^{L}$
	- This number is a horizontal shift of the line that forms when plotting $f_{i}$ against $i$
	- Ensures that $f_{1}=-f_{M}$
- $L=$ Number of bits per signal element. $=\log_{2}M$
\
To match the data rate of the input bit stream, each output signal element is held for a period of $T_{s}=LT$ seconds, where $T$ is the bit period, and $\frac{1}{T}$ is the data rate.
Thus, one signal element, which is a constant frequency tone lasting $T_{s}$ seconds, encodes $L$ bits.  The textbook says the total bandwidth required for MFSK is $2Mf_{d}$
- My intuition said this is actually $2(M-1)f_{d}$, since the distance in frequency between the top and bottom frequencies is given by this formula
- But orthogonality must be achieved between the different signal elements so that they do not interfere with each other. This is achieved by fixing $f_{d}=\frac{1}{2T_{s}}$, where $T_{s}$ is the duration of each signal element.
- This means $B=2(M-1)\left( \frac{1}{2T_{s}} \right) =\frac{M}{T_{s}}-\frac{1}{T_{s}}$
- In most cases, though, $\frac{1}{T_{s}} \ll \frac{M}{T_{s}}$. Thus $$B=\frac{M}{T_{s}}=2Mf_{d}$$
# Phase Shift Keying

## Two-Level PSK
Two-Level Phase Shift Keying uses two phases to represent two binary digits.

$$
s(t)=
\begin{cases}
A\cos(2\pi f_{c}t) & \text{Binary 1} \\
A\cos(2\pi f_{c}t+\phi) &\text{Binary 0}
\end{cases}
$$
### Binary Phase Shift Keying (BPSK)
If we choose $\phi=\pi$, then this has the effect of flipping the carrier signal, since $\cos(\omega+\pi)=-\cos(\omega)$
Thus, we can define some discrete function $d(t)$ that takes a value of +1 if the corresponding bit is 1 and -1 if the corresponding bit is 0. $d(t)$ is a NRZL representation of the data. Then we can define $$s(t)=A\ d(t)\cos(2\pi f_{c}t)$$
### Differential Phase Shift Keying (DPSK)
Much like NRZI, DPSK encodes the data in the transition between phase shifts at each signal interval. This scheme eliminates the need for the receiver to be synchronized with the transmitter, since the receiver need only interpret the phase shift between any two signal intervals.

If we define $d_{NRZI}(t)$ as a similar signal to $d(t)$, but where $d_{NRZI}(t)$ is the NRZI processed version of $d(t)$, then we can define s(t) in much the same way as BPSK: $$s(t)=d_{NRZI}(t)*A\cos(2\pi f_{c}t)$$
## Four-Level PSK
More efficient use of bandwidth can be achieved if each signal element represents multiple bits.
### Quadrature Phase Shift Keying (QPSK)
A common way to achieve this is through Quadrature Phase Shift Keying (QPSK)

$$
s(t)=
\begin{cases}
A\cos\left(2\pi f_{c}t + \frac{\pi}{4}\right)& 11 \\
A\cos\left(2\pi f_{c}t + \frac{3\pi}{4}\right)&01 \\
A\cos\left(2\pi f_{c}t - \frac{3\pi}{4}\right)& 00 \\
A\cos(2\pi f_{c}t - \frac{\pi}{4})& 10

\end{cases}
$$
The input is a stream of bits with data rate $R=\frac{1}{T_{b}}$ where $T_{b}$ is the width of each bit. This stream is converted into two separate bit streams of $\frac{R}{2}$ bps each. These two bit streams are referred to as I (In-Phase) and Q (Quadrature). The amplitudes are mapped onto $\pm \frac{1}{\sqrt{ 2 }}$ for convenience of modulator structure. Thus, $$s(t)=\frac{1}{\sqrt{ 2 }}I(t)\cos(2\pi f_{c}t)-\frac{1}{\sqrt{ 2 }}Q(t)\sin(2\pi f_{c}t)$$
This can be achieved through the following block diagram:
![[Pasted image 20240717231006.png]]
Since the two modulated streams of QPSK are BPSK signals at half the data rate of the original stream, the symbol/baud rate is half the input bit rate. From one symbol to the next, phase shift of $\frac{\pi}{2}$ is possible.

### OQPSK
Another version of this scheme is called Offset Quadrature Phase Shift Keying or (OQPSK) A delay of one bit time is introduced into the Q stream resulting in $$s(t)=\frac{1}{\sqrt{ 2 }}I(t)\cos(2\pi f_{c}t)-\frac{1}{\sqrt{ 2 }}Q(t-T_{b})\sin(2\pi f_{c}t)$$
Since this scheme varies only in the 1 bit delay applied to the Q signal, its spectral characteristics and bit error rate are the same as QPSK. However, by delaying the Q signal, OQPSK ensures that only one signal, either I or Q, can change value at any given symbol. From the definition of QPSK's phase shifts, changing just one bit at a time has a maximum phase shift change of $\pi$. This limits the maximum change in phase shift between any two symbols to $\pi$. This is good because physical limitations on PSK modulators make large phase shifts at high transition rates difficult to perform.
OQPSK also provides superior performance when the transmission channel has significant nonlinear components. The effect of nonlinearities is a spreading of the signal bandwidth, which may cause interference/crosstalk. If the phase shift changes are smaller, this is easier to control.
- Thus OQPSK only provides advantages in the practicality of its implementation
- No theoretical benefits at all (at least from this level of abstraction)
## Multilevel PSK
By using a different number of phase angles, more than 2 bits can be transmitted at a time. For example, a standard 9600 bps modem uses 12 phase angles, four of which have two amplitude values, for a total of 16 different signal elements. (Transmits 4 bits at a time). This is called 16-PSK
![[Pasted image 20240717233714.png]]
This points out the difference between the data rate. In this case, $R=\frac{1}{T_{b}}$ bits per second as usual, but each signal element contains 4 bits of data since there are 16 unique signal elements. $L=4=\log_{2}16=\log_{2}M$ $M=16=2^{4}=2^{L}$
Thus the modulation rate in baud, given by $D=\frac{R}{L}=\frac{R}{4}$
This standard modem uses a data rate $R=9600$bps, but a modulation rate of $\frac{R}{4}=2400$ baud. 

# Performance
## Bandwidth
### ASK, PSK, and Sometimes FSK
For ASK, $$B=(1+r)R$$where $R$ is the bit rate and $r$ is related to the technique by which the signal is filtered to establish a transmission bandwidth. Typically $0<r<1$. This is also valid for PSK and sometimes for FSK
### MPSK
Significant improvements can be achieved using these schemes. In general: $$B=\left( \frac{1+r}{L} \right)R=B=\left( \frac{1+r}{\log_{2}M} \right)R=D(1+r)$$ Improvement here means a narrowing of the bandwidth, thus resulting in greater efficiency. As L (and therefore M) increases, B decreases.

### FSK
$$B=2\Delta F+(1+r)R$$
- $\Delta F=f_{2}-f_{c}$
	- Total offset
### MFSK
$$B=\left(  \frac{(1+r)M}{\log_{2}M} \right)R=(1+r)DM$$
This is actually worse than MPSK. The bandwidth increases with M faster than it does with L, as the denominator is in terms of the log of M. Thus the bandwidth is typically greater with MFSK for the same baud rate $D$
![[Pasted image 20240717235232.png]]
## Bit Error Rate
![[Pasted image 20240717235346.png]]
![[Pasted image 20240717235541.png]]
Figure 5.13 shows that, while MPSK allows for greater spectral efficiency than MFSK, the bit error rate is magnitudes greater for a given value of $M$. 
For MPSK, $M$ increases error rate, and increases bandwidth efficiency. 
- MPSK has direct correlation between M, error and spectral efficiency
For MFSK, $M$ decreases error rate, and decreases bandwidth efficiency 
- MFSK has an inverse correlation between $M$, error, and spectral efficiency
Thus, in both cases there is a tradeoff between bandwidth efficiency and error rate. Also, worth noting is that error rate and bandwidth efficiency are directly correlated.





For class #data-comm 