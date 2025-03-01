Continues [[Data Communication Basics]]
Continued by [[Transmission Impairments]]
Related to [[Fourier Series]]
- ## Transmission Medium
	- Guided Media:
		- Physical wires
	- Unguided media
		- Wireless
		- Microwaves, infared, radio
- ## Directions
	- Simplex
		- One sender one receiver
	- Half-Duplex
		- Both can send, but one at a time
		- Like walkie talkies
	- Full-Duplex
		- Both can send simultaneously
		- Telephone, USB
- ## Transmission Links
	- Direct Link
		- Path between two devices with no intermediate devices 
			- **Except for Amplifiers**
	- Point-to-point Transmission
		- Direct link between two devices
		- No other devices share this link
	- Multi-point:
		- More than two devices share the link
- ## Repeaters Vs. Amplifiers
	- Repeaters are digital, amplifiers are analog
	- Since repeaters interpret the received signal into bits and then recreate the digital signal on the other end, there is no accumulation of noise/error that is present with amplifier systems.
- ## Finding Characteristics of a Signal
	- Take the Fourier series and rewrite the signal as a linear combination of sine waves
- ## Spectrum and Bandwidth
	- ### Spectrum
		- Range of frequencies in a signal
	- ### Bandwidth
		- Absolute: width of spectrum
		- Effective: (BW)
			- Signals have infinite bandwidth
			- A range must be defined in which a signal can be transmitted
			- This is the range where the most energy is concentrated
	- Any signal has infinite bandwidth, but a transmission system must limit this band of frequencies
		- Doing so creates distortions
		- For example: Take a square wave that encodes bits as high or low. A square wave has infinite harmonics, but real systems must limit this, which has the following effect:
		- ![[Pasted image 20240708223313.png]]
	- Increasing bandwidth allows for reduction of distortion at the receiver, which results in the following rule:
		- The more limited the bandwidth, the greater the distortion.
		- Thus, a higher data rate requires a larger bandwidth
- ## Synchronous and Asynchronous Transmission
	- ### Asynchronous Transmission:
		- Send one word at a time with some set length
		- The receiver can resynchronize at the beginning of each character
	- ###  Synchronous Transmission:
		- A separate clock line can be used over short distances
		- But over long distances, the clock line experiences the same impairments as the data line
		- The other alternative is to embed clocking info into the data signal
		- #### Frames:
			- A preamble bit pattern begins a block
			- Followed by data
			- Ended by postamble
			- This whole sequence of three parts is called a **Frame**
				- Note this is the same terminology as the data link layer
	- 

For class #data-comm