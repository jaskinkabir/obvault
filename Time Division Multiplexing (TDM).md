Continues [[Multiplexing (PHYSICAL MUX)]]
Continues [[Frequency Division Multiplexing (FDM)]]
Continued by [[Multiple Channel Access (DATA LINK MUX)]]
Chapter 8.2
# Characteristics
- This kind of multiplexing is possible when the achievable data rate of the medium exceeds the data rate of signals to be transmitted
- Multiple digital signals can be carried on a single transmission line by interleaving portions of each signal in time
	- The interleaving can be at the bit level or in blocks of bytes
## Operation
### Block Diagram
![[Pasted image 20240805144729.png]]
### Basic Overview
- $n$ signals $m_{i}(t)$ are to be muxed
- The incoming data from each source are briefly buffered
	- Each buffer is typically one bit or character in length
- The buffers are scanned sequentially to form a composite digital data stream $m_{c}(t)$
	- The scan operation is sufficiently rapid such that each buffer is emptied before more data can arrive
- Thus the data rate of $m_{c}(t)$ must be at least the sum of the data rates of the $m_{i}(t)$ signals
- The transmitted signal may have a format something like figure 8.6b
	- The data is organized into **frames** where each frame contains a cycle of time slots
	- In each frame one or more slots are dedicated to each data source
- The sequence of slots dedicated to one source, from frame to frame, is called a **Channel**
	- The slot length equals the transmitter buffer length
### Interleaving
- The byte interleaving technique is used with asynchronous and synchronous sources.
	- Each time slot contains one character of data
	- Typically the start and stop vits of each character are eliminated before TX and reinserted by RX, thus improving efficiency
- The bit interleaving technique is used with synchronous sources and may also be used with asynchronous sources
	- Each time slot contains just one bit
- At the RX, the interleaved data is demuxed and routed to the destination buffers
- **Synchronous TDM is called Synchronous because the time slots are preassigned and fixed**
	- The time slots for each source are transmitted whether the source has data to send
	- This is also the case for FDM
	- Even when fixed assignment is used, TDM can handle sources of different data rates
		- Slower data sources are assigned one time slot, faster ones are assigned more
### Procedure
1. Time slots pre-assigned to different sources
2. Multiple digital signals are interleaved in time
3. Interleaving can be at bit level or in blocks
4. Data rate of the link is $n$ times faster, and the unit duration is $n$ times shorter
	1. Input bit rate = output frame rate
5. A complete cycle of data units from each input is collected into a frame
	1. Each frame is $n$ slots, each slot duration is $\frac{1}{n}$ shorter
### Requirements
1. Data rate of medium must exceed data rate of each signal to be transmitted
	1. Output data rate must be at least $n$ times the input data rate
### Example Problem
![[Pasted image 20250828153155.png]]
1. Bit duration = $\frac{1}{bps_{i}} = 1\mu s$
2. Output bit duration = $\frac{1}{n*bps_{i}}=250ns$
3. Output bit rate = $\frac{1}{bps_{o}}=4Mbps$
4. Output frame rate = 1 mega frame per second
## Statistical TDM
- Synchronous TDM has the problem of wasting slots when that input channel has no data
- The statistical TDM dynamically allocates time slots on demand
- There are $n$ I/O lines, but only $k$, where $k<n$, time slots available on the TDM frame.
- For input, the multiplexer scans the input buffers, collecting data until a frame is filled. It then sends this frame
- The receiver will receive this frame and distribute the slots to the appropriate destinations
- Packet switching is a form of Statistical TDM
### Why?
- Statistical TDM allows for a slower output bit rate for the same input bit rate
- This is possible because not all input lines are used at once
### Problems
- Address bits must be appended to each input
	- $n$ bit address field inside each slot: $2^{n}$ output lines
	- Ratio of data size to address size must be large enough to justify this overhead
	- Cannot be used for bit-level interleaving
- During peak periods, capacity may not be enough
	- MUX buffers inputs to hold temporary excess input
	- Tradeoff: buffer size (delay) vs. data rate of the line
### Example Problem
For 4 bits in a frame
```

__11|\
0000| \  [0010][0001][1101]
0101| /
__01|/
```
3 bits per frame
```

__11|\
0000| \  [001][000][011][101]
0101| /
__01|/
```
# TDM Link Control
- The transmitted data stream in figure 8.6b does not contain headers and trailers typically associated with synchronous transmission
- This is because control mechanisms provided by data link protocol are not needed
- This can be explained by considering the two key data link control mechanisms: flow and error control
- What if one of the output lines attached to a device is temporarily unavailable to receive data?
	- The remaining output lines expect to receive data at predetermined times
	- The solution is for the saturated output device to cause the flow of data from the input device to cease
	- Thus, the channel will carry empty slots, but the frames as a whole will maintain the same transmission rate
	- Thus, flow control techniques are unnecessary
- The reasoning for error control is the same 
	- It would be undesirable to request the retransmission of an entire TDM frame because of an error on one channel.
	- The solution is to apply error control on a per-channel basis
## Framing
- Since there are no flag or SYNC characters to bracket TDM frames, some means is needed to ensure frame synchronization
- The most common mechanism for framing is called **added-digit framing**
	- One control bit is added to each TDM frame.
	- An identifiable pattern of bits, from frame to frame, is used as a control channel
	- A typical example is the alternating bit pattern 1010...
		- Unlikely to be sustained on a data channel
	- The receiver can search for this bit pattern and synchronize based on its position
## Pulse Stuffing
- The most difficult problem of Synchronous TDM design is the synchronization of various data sources
	- If each source has a separate clock, any variation among clocks could cause loss of synchronization
	- Also, in some cases, the data rates of the input streams are not related by a simple rational number
- For both of these problems, a technique known as **Pulse Stuffing** is an effective remedy
	- The outgoing data rate of the MUX, including framing bits, is higher than the sum of the input channels' data rates
	- The extra capacity is used by stuffing dummy bits or pulses into each incoming signal until its rate is raised to that of a locally generated clock signal
	- The stuffed pulses are inserted at fixed locations in the frame format so that they may be identified and removed at the demux
# Digital Carrier Systems
## NA (AT&T) and International (IUT-T) TDM Carrier Standards
- In the US, AT&T developed a hierarchy of TDM structures, which is used in the US Canada and Japan.
![[Pasted image 20240805152356.png]]
### DS-1 Transmission Format
![[Pasted image 20240805152932.png]]
- The basis of the TDM hierarchy is this DS-1 format, which multiplexes 24 channels
	- Each frame contains 8 bits per channel, plus a framing bit for $24 \times 8 + 1 = 193 \text{ bits}$ 
- For voice transmission, the following rules apply
	- Each channel contains one word of digitized voice data
	- The original analog voice signal is digitized using PCM at a rate of 8000 samples/sec
	- Therefore, each channel slot and hence each frame must repeat 8000 times per second
		- With a frame length of 193 bits, the data rate for one DS-1 system is $8000 \times 193 = 1.544 \text{ Mbps}$
	- For five of every 6 frames, 8-bit PCM samples are used
	- For every sixth frame, each channel contains a 7-bit PCM word plus a *signaling bit*
		- These signaling bits form a stream for each voice channel that contains network control and routing information
		- For example, these control signals could be used to establish a connection or terminate a call
- This same format is used to provide digital data service
	- For compatibility with voice, the same 1.544 Mbps data rate is used
	- In this case, 23 channels of data are provided, with the 24th reserved for a special sync byte
		- This allows faster and more reliable reframing following a framing error
	- Within each channel 7 bits per frame are used for data, with the eighth used to indicate whether the channel, for that frame, contains user data or system control data
	- With 7 bits per channel, and because each frame is repeated 8000 times per second, each channel can be provided with a 56Kbps link
	- Lower data rates are provided using a technique called **Subrate Multiplexing**
		- For this technique, an additional bit is robbed from each channel to indicate which subrate multiplexing rate is being provided
			- This leaves a total capacity per channel of 48 Kbps
		- This robbed capacity is used to multiplex five 9.6 Kbps channels, ten 4.8 Kbps channels, or twenty 2.4 Kbps channels
		- For example, if channel 2 is used to provide 9.6 Kbps service:
			- Up to five channels can share this channel
			- the data for each sub-channel appears as 6 bits in channel two every fifth frame
-  Finally, the DS-1 Format can be used to carry a mixture of voice and data channels
	- In this case, all 24 channels are utilized; no sync byte is provided
- Above the DS-1 Data rate of 1.544 Mbps, higher-level multiplexing is achieved by interleaving bits from DS-1 bitstreams
	- For example, The DS-2 TX system combines four DS-1 inputs into a 6.312 Mbps datastream
	- Data from the four sources are interleaved 12 bits at a time
	- Note that $1.544 \times 4 = 6.176 \text{ Mbps}$; the remaining capacity is used for framing and control bits
## SONET/SDH
- **Synchronous Optical NETwork**
	- Proposed by BellCore and standardized by ANSI
- **Synchronous Digital Hierarchy**
	- Published by ITU-T and is compatible with SONET
### Signal Hierarchy
- The SONET specification defines a hierarchy of standardized digital data rates
- The lowest level, referred to as **(STS-1, or Synchronous Transport Signal level 1)** or **OC-1 (Optical Carrier level 1)**, is 51.84 Mpbs
	- This rate can ebe used to carry a single Ds-3 signal or a group of lower rate signals, such as DS1, DS1C, plus IUT-T rates
- Multiple STS-1 Signals can be combined to form an STS-N signal
	- Created by interleaving bytes from N STS-1 signals that are mutually synchronized
- For the ITU-T SDM, the lowest rate is 155.52 Mbps, which is designated as STM-1
	- This corresponds to SONET STS-3
- ![[Pasted image 20240805160143.png]]
### Frame Format
- The basic SONET building block is the STS-1 Frame
	- Which consists of 810 octets and is transmitted once every $125 \mu \text{s}$, for an overall data rate of 51.84 Mbps
	- The frame can be logically viewed as a matrix of 9 rows of 90 octets each
	- Transmission occurs one row at a time, from left to right and top to bottom
	- ![[Pasted image 20240805160440.png]]
- The first three columns ($3 \text{ octets } \times 9 \text{ rows } = 27 \text{ octets}$) of the frame are devoted to overhead octets
	- 9 octets are devoted to section-related overhead and 18 octets are devoted to line overhead
	- ![[Pasted image 20240805160619.png]]
	- ![[Pasted image 20240805160654.png]]
- The remainder of the frame is payload
	- The payload includes a single column of **path overhead** which is not necessarily in the first available column position
		- The line overhead contains a pointer that indicates where the path overhead starts

For class #data-comm