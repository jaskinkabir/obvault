Signaling techniques, digital encoding schemes, modulation rate
Continues [[Transmission Terminology]]
Continued by [[Digital Data, Analog Signals]]

# Digital Signaling
- A data source $g(t)$, which may be either analog or digital, is encoded into a digital signal $x(t)$. The form of this digital signal depends on the encoding technique and is chosen to optimize use of the transmission medium
# Analog Signaling
- The basis for analog signaling is a constant frequency **Carrier Signal**. Its frequency is chosen to be compatible with the medium. Data may be transmitted using a carrier signal by modulation
- **Modulation** Is the mapping of the input signal $m(t)$ onto either the amplitude, frequency, or phase of the carrier signal $f_{c}$
- The input signal $m(t)$ may be either digital or analog, and is called the modulating or **baseband signal**. 
- The modulation of $m(t)$ results in the modulated signal $s(t)$. 
- ![[Pasted image 20240710103346.png]]
# Digital Data, Digital Signals
### Terms:
- If all the signal elements have the same algebraic sign, the signal is **unipolar**
	- Otherwise the signal is **polar**, where one logic level is negative and the other positive
- The **Data Signaling Rate**, or just **Data Rate**, is the number of bits per second that data is transmitted
	- Data Rate is affected by these three statements
		- An increase in data rate increases **Bit Error Ratio**
		- An increase in SNR decreases bit error ratio
		- Increase in bandwidth **allows** an increase in data rate
- The **Bit Duration** is simply $\frac{1}{R}$ seconds, where $R$ is the data rate in bits per second
- The **Modulation Rate** is the rate at which the signal level is changed
	- This will depend on the nature of encoding
	- This is expressed in baud, which refers to signal elements per second
- *Mark* and *Space* are historical terms for 1 and 0
- **Bit Error Rate/Ratio**
	- Most people refer to this term with the stupider name of bit error rate, which implies it is a quantity that refers to time
	- However this is actually the probability that the receiver misinterprets a bit
## Digital Encoding Formats:
### Unipolar Schemes:
- #### Non Return to Zero-Level (NRZL)
	- Voltage is constant during the bit interval, which means there is **no return to zero level between bits**
	- 0 = high
	- 1 = low
	- Most other schemes take NRZL signals and convert them into the proper encoding for transmission
- #### Nonreturn to Zero Inverted (NRZI)
	- 0 = no transition at the beginning of interval
	- 1 = transition at beginning of interval
	- The voltage is also constant during the bit interval
	- **Generating signal**
		- If binary data is $g[n]$, and NRZI signal is $x[n]$
			- $x[n]=x[n-1] \oplus g[n]$
			- Quick shortcut for generating signal using XOR
			- ![[Pasted image 20240717130212.png]]
	- ##### Differential Encoding
		- Information to be transmitted is represented in therms of the changes between successive signal elements rather than the signal elements themselves.
		- Easier to determine a transition than differentiate signal levels in the presence of noise.
		- Also polarity agnostic
- #### Advantages and Disadvantages of NRZ
	- Are the easiest to engineer and make efficient use of bandwidth
		- ![[Pasted image 20240717130345.png]]
		- Most of the energy used by NRZ is between DC and half the bit rate
	- Disadvantage is timing. It is easy to lose track of timing with NRZ schemes, especially across distances
	- Another disadvantage is the presence of a DC component
### Bipolar Schemes
#### Advantages
Since the polarity of the line signal always alternates, this scheme is polarity agnostic and has no net DC component. This can also help with timing in the case of a long string of 1s for BAMI or 0s for PT. However, in the opposite cases, techniques must be used to ensure synchronization. 
#### Disadvantages
When compared to NRZ, the receiver must now distinguish between 3 signal levels instead of just 2, but gains no increase in throughput for it. This means that a multilevel binary signal requires approximately 3 dB more signal power for the same probability of bit error. 
At a given SNR, the bit error rate for NRZ codes is significantly less than multilevel binary
- #### Bipolar AMI (Alternate Mark Inversion)
	- 0 = no line signal
	- 1 = positive or negative level, alternating for successive ones
	- **Opposite of Pseudoternary**
- #### Pseudoternary
	- 0 = positive or negative level, alternative for successive zeros
	- 1 = no line signal
	- **Opposite of Bipolar AMI**
	- ![[Pasted image 20240710105448.png]]
### Biphase Schemes
The problem with NRZ is that successive ones or zeros can lead to a loss of synchronization, as there is no clear bit clock. Another issue is called DC wander, where the signal being passed over several AC coupling lines. Capacitance appears across these lines that charges according to the DC component and messes with the signal.

The two Manchester encoding schemes provide the following advantages:
- Synchronization
	- There is always a transition at the midpoint of each interval, which synchronizes the transmitter and receiver.
- No DC component
	- Still unclear why this matters, AC wander I guess? 
- Error Detection
	- The absence of an expected transition can be used to detect errors.
	- This is robust because noise on the line would have to invert the signal both before and after the transition to cause an undetected error. 
The disadvantage however is that the signal effectively uses two bits of encoded signal to transmit a single bit of data, requiring double the bandwidth and data rate.

- #### Manchester encoding (MAN)
	- Transition in the middle of each bit period determines bit value
		- There is always a transition in the middle of the bit period
	- Used by IEEE 802.3 Ethernet
	- One NRZI interval represents two Manchester Intervals
	- 1 = low to high transition (rising)
	- 0 = high to low transition (falling)
	- In order to be able to make these transitions in the middle of the interval, the voltage level may have to transition at the beginning of the bit period.
	-  Cur bit = 1, cur level = 1:
		- Bitstream = 0,1
	- Cur bit = 1, cur level = 0:
		- Bitstream = 1,0
- #### Differential Manchester (DMAN)
	- Ex:
		-  [0,1,0,0,1,1,0,0,0,1,1] (initial 1)
		- 01 10 10 10 01
		- 
	- There is always a transition in the middle of the interval
	- 0 = transition at the beginning of the interval
	- 1 = no transition at the beginning
	- The rising or falling property of the edge is irrelevant to bit value. Only the presence or absence of the edge at the beginning of the bit period is relevant
	- ![[Pasted image 20240716172215.png]]
### ![[Pasted image 20240710110540.png]]

## Differentiating Between Data and Modulation Rate
The data rate $R$ is expressed in terms of bits per second, or $\frac{1}{T_{b}}$ where $T_{b}$ is the bit duration. However, in schemes like the Manchester schemes, the rate at which the transmitted signal can sometimes be twice the data rate. This calls for the definition of a new unit called Modulation rate, denoted by $D$ and measured in terms of baud. The modulation rate can be found, in general, by using this formula $$D=\frac{R}{L}=\frac{R}{\log_{2}M}=\frac{L}{T_{b}}=\frac{\log_{2}M}{T_{b}}$$here 
- $D=$ Modulation rate in baud
- $R =$ Data rate, bps
- $T_{b}=$ Bit duration, seconds
- $M=$ Number of different signal elements, $2^{L}$
- $L=$ Number of bits per signal element.
Note that this formula is general and does not work for Manchester Encoding.
In the case of Manchester transmitting a string of all 0s or 1s, the transmitter must generate a stream of transitions at each half bit duration. Thus, the modulation rate is twice the data rate. However, according to the formula above, this means that there are $\sqrt{ 2 }$ different signal elements. This is clearly false, so you have to be careful using $\log_{2}M$ and $M=2^{L}$. It only applies when L is an integer!

Trust your intuition here. We know that $L=\frac{1}{2}$ since each signal bit requires two signal elements to be transmitted and that $M=2$ since there are two unique elements: rising and falling transition. $M \neq2^L$ here.

## Normalized Signal Transition Rate of Various Digital Signal Encoding Schemes
![[Pasted image 20240717134559.png]]
- This table relates the modulation rate to the data rate
	- In the case of manchester, the maximum modulation rate is $2R$



![[Pasted image 20240717134650.png]]

## Scrambling Techniques
Although the Biphase (Manchester) schemes have achieved widespread use in LAN applications up to 10Mbps, they are never used in long distance applications. This is because they require up to twice the signaling rate as the data rate, which makes them very inefficient.

Another approach to dealing with the weaknesses of the Unipolar (NRZ) schemes is to use some sort of **Scrambling Scheme**. The idea is simple:
Sequences that would result in a constant voltage are replaced by filling sequences that will provide sufficient transitions for the receiver's clock to maintain synchronization. The filling sequence must be recognized by the receiver and replaced with the original data sequence. The filling sequence is the same length, so there is no change in data rate. The design goals are as follows:
- No DC component
- No long sequences of constant line-level signals
- No reduction in data rate
- Error-Detection capability
There are two scrambling techniques used in LDT (Long Distance Transmission)

### Bipolar With 8 Zeros Substitution (B8ZS)
**This is commonly used in North America**
This scheme is used on a bipolar-AMI (Alternate Mark Inversion). As discussed earlier, Bipolar-AMI has the following rules
- Binary 0 = no line signal
- Binary 1 = positive or negative line signal, alternate of the most recent preceding 1.
B8ZS adds the following rules:
- If an octet of all zeros occurs and the last voltage pulse preceding this octet was positive, then these 8 bits are encoded as:
	- 000+-0-+
- If an octet of zeros occurs and the last voltage pulse was negative, the 8 bits are encoded as:
	- 000-+0+-
Note that this sequence causes two code violations:
- If the last preceding 1 was positive, the first pulse after the three 0s will also be positive, or vice verse.
- Then the pulses before and after the middle zero will be the same polarity
These two successive code violations are unlikely to be caused by noise or other impairments, and can thus be recognized by the receiver and interpreted as a 0 octet.
## High-Density Bipolar-3 Zeros (HDB3)
**Commonly Used in Europe and Japan**
Strings of 4 zeros is replaced with a sequence that results in 1 code violation. In each case, the fourth zero is replaced with a code violation. In addition, a rule is needed to ensure that successive violations are of opposite polarity to ensure that no dc component is introduced. Thus, if the last violation was positive the current violation must be negative and vice versa. 
This condition is tested for by determining (1) whether the number of pulses since the last violation is even or odd and (2) the polarity of the last pulse before the occurrence of the four zeros.

These two parameters can be applied to the following table to generate the proper substitution:


|                             | Number of Pulses Since Last Sub |      |
| :-------------------------: | :-----------------------------: | :--: |
| Polarity Of Preceding Pulse |               Odd               | Even |
|              -              |              000-               | +00+ |
|              +              |              000+               | -00- |

 ![[Pasted image 20240717210609.png]]

For class #data-comm