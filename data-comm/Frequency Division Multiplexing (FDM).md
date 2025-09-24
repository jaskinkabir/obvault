Continues [[Multiplexing (PHYSICAL MUX)]]
Continued by [[Time Division Multiplexing (TDM)]]
Continued by [[Multiple Channel Access (DATA LINK MUX)]]
Chapter 8.1

# Characteristics
- FDM is possible when the useful bandwidth of the medium exceeds the required bandwidth of signals to be transmitted.
- A number of signals can be carried simultaneously if each signal is modulated onto a separate carrier frequency
	- These carrier frequencies should be sufficiently separated such that the bandwidths of the signals do not significantly overlap
	- Each segment of the bandwidth on which data is transmitted is referred to as a **channel**, centered around the carrier frequency
	- Each channel is separate by guard bands, to prevent interference.
## Operation
- $n$ analog or digital signals $[m_{i}(t),i=1,n]$ are to be multiplexed onto the same medium
	- Each signal $m_{i}(t)$ is modulated onto a carrier $f_{i}$. Because multiple carriers are to be used, each is referred to as a **subcarrier**
- The resulting analog, modulated signals are then summed to produce a composite **Baseband** signal $m_{b}(t)$
- This baseband signal may even be modulated to a different carrier frequency to produce $s(t)$
## Image
![[Pasted image 20240804191456.png]]
## Requirements
- Useful bandwidth must exceed the required bandwidth of each signal
	- $B>\Sigma B_{i}$
- Carrier frequencies must be separated by guard bands
## Bandwidth
- The FDM Signal $s(t)$ has total bandwidth $B$ where $B> \sum_{i=1}^nB_{i}$.
- At the receiving end, this signal is demodulated to retrieve $m_{b}(t)$, which is then passed through $n$ band-pass filters
## Problems
- The following image points out two problems: crosstalk and intermodulation noise
- ![[Pasted image 20240804192054.png]]
- Crosstalk:
	- The spectra of adjacent component signals may overlap significantly.
- Intermodulation noise:
	- On a long link, the nonlinear effects of amplifiers on a signal in one channel could produce frequency components in other channels
		- Think about amplifier frequency response curves
- Even if there is no data to be transmitted on a given channel, it must still be allocated to keep the logic consistent
# Analog Carrier Systems
## AT&T Hierarchy
- In the US, AT&T has designated a hierarchy of FDM schemes to accommodate transmission systems of various capacities
	- A similar system has been adopted internationally with the name ITU-T
- In the first level, called a **Group**, 12 voice channels are combined to produce a group signal with $B=12\times4kHz=48kHz$, in the range 60 to 108kHz
- The next basic building block is the 60-channel **supergroup**
	- Formed by applying FDM to 5 group signals
		- At this step, each group is treated as a single signal with a 48kHz bandwidth
		- The subcarriers have frequencies from 420 to 612kHz in increments of 48kHz
		- The resulting signal occupies 312 to 552 kHz
	- There are several variations to supergroup formation
		- Each of the five inputs may be a group of 12 voice channels
		- Additionally, any signal up to 48kHz in bandwidth contained between 60 and 108kHz may be used as an input to the supergroup multiplexer
		- It is also possible to combine 60 voice channels at once which may reduce multiplexing costs
- The next level up is the **mastergroup**
	- This combines 10 super-groups
		- Again, any 240kHz bandwidth signal contained between 312 and 552 kHz can serve as an input
	- The mastergroup has a bandwidth of 2.52 MHz and can support up to 600 voice frequency (VF) channels
- Higher level multiplexing is defined in the table below
- ![[Pasted image 20240804193152.png]]
## Wavelength Division Multiplexing (WDM)
- Used for optical fiber links
### Operation
- Very similar to FDM
- A number of sources generate laser beams at different wavelengths, which are sent to the multiplexer
- The multiplexer consolidates these sources for transmission across a single optical fiber line
- Optical amplifiers, typically spaced tens of kilometers apart, amplify all wavelengths simultaneously
- Finally the composite signal arrives at a demultiplexer, where the component channels are separated and sent to receivers
### Channel Characteristics
- Most WDM system operate in the 1550nm range.
- In early systems, 200GHz was allocated to each channel.
	- Today, most systems use 50GHz spacing
- ![[Pasted image 20240804193814.png]]
- The term **Dense Wavelength Division Multiplexing (DWDM)** is often referred to
	- There is no standard defnition
	- Generally, any WDM scheme that uses channel spacing of 200GHz or less is considered dense

For class #data-comm