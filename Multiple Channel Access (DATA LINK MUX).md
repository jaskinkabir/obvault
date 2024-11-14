Continues [[Multiplexing (PHYSICAL MUX)]]
Continues [[Frequency Division Multiplexing (FDM)]]
Continues [[Time Division Multiplexing (TDM)]]
Continued by [[Circuit Switching Networks]]

# Multiple Channel Access Overview
- Multiplexing techniques used for sharing a single channel's capacity among multiple TX/RX stations
	- These channels can be muxed across one medium using FDM or TDM 
- **THESE TECHNIQUES ARE USED AT THE DATA LINK LAYER**
- These techniques differ from the FDM and TDM techniques, because no physical multiplexer is involved
- Rather, individual stations are assigned a frequency band or sequence of time slots and transmit directly onto the channel and not through a multiplexer
- These techniques are used as building blocks in a number of wireless schemes such as wireless LANs such as Wi-Fi, cellular networks, satellite networks, and wireless broadband such as WiMAX
# Frequency-Division Duplex (FDD)
## Characteristics and Operation
- FDD simply means that two stations have a full duplex connection in which each station transmits on a separate frequency band
	- These frequency bands are separated from other bands on the network by guard bands to prevent interference/crosstalk
- The combination of these two frequency bands is called a **subchannel**
	- The combination of this subchannel and the guard bands is viewed as a single full-duplex channel between the stations
## Channel Diagram
![[Pasted image 20240805161543.png]]
# Time-Division Duplex (TDD)
## Characteristics and Operation
- Also known as **Time-Compression Multiplexing (TCM)**
- Used in cordless telephones and is a building block for a number of wireless network systems
- Data is transmitted in one direction at a time (half-duplex)
	- Transmission alternates between directions
- To achieve the desired data rate with simple TDD, the TX bit stream is divided into equal segments, compressed in time to a higher transmission rate and transmitted in bursts
	- The bursts are expanded at the other end to the original rate
- A short quiescent period is used between bursts going in opposite directions to allow the channel to settle down
- Thus the data rate on the channel must be greater than twice the data rate required by the two end systems
## Channel Diagram
![[Pasted image 20240805161654.png]]
## Timing and Data Rates
- Each side sends blocks of some fixed length, which take time $T_{b}$ to transmit
	- This time is a linear function of the number of bits in a block
- Time $T_{p}$ is required for the propagation of a signal from TX to RX
	- Linear function of the distance between transmitter and receiver
- Guard time $T_{g}$ is introduced tot turn the channel around
- Thus, the time to send one block is $T_{p}+T_{b}+T_{g}$
	- But since the sides must alternate transmissions, data can only be transmitted by one side every $2(T_{p}+T_{b}+T_{p})$ time steps
- If we let $B$ be the size of a block in bits, we can find the effective data rate $R$ as seen by the two endpoints as $$R=\frac{B}{2(T_{p}+T_{b}+T_{p})}$$
	- The actual data rate, $A$, on the medium can easily be seen to be $A=B/T_{b}$
	- Combining the two, we have $$A=2R\left( 1+ \frac{T_{p}+T_{g}}{T_{b}} \right)$$
- The choice of block size $B$ is a compromise between two competing requirements:
	- For a larger block size, the value of $T_{b}$ becomes larger compared to the values of $T_{p}$ and $T_{g}$
	- Consider there is a fixed value of $R$, which is the data rate required for the link, and we need to determine the true data rate $A$
		- If $B$ is increased, there is a decrease in $A$
			- This makes implementation easier
			- But it also increases the signal delay due to buffering, which is undesirable for voice traffic
# Frequency-Division Multiple Access (FDMA)
## Characteristics and Operation
- A technique to share the spectrum among multiple stations.
- Typically, the configuration is as follows:
	- There is one base station that communicates with a number of subscriber stations
		- Such a configuration is found in satellite and cellular networks, WiFi, and WiMAX
	- Typically, the base station assigns bandwidths to stations within the overall bandwidth available. 
### Example Network With Diagram
- Example:
	- ![[Pasted image 20240805194545.png]]
	- Three stations are assigned separate frequency bands (subchannels) for transmission to the base station (uplink direction), with guardbands between the transmission bands
	- Another frequency band, typically wider, is reserved for transmission from the base station to the other stations (downlink direction)
		- The base station typically uses TDMA to transmit data to all of its subscriber stations across the same subchannel
## Key Features of FDMA
- Each subchannel is dedicated to a single station; it is not shared
- If a subchannel is not in use, it is idle; the capacity is wasted
- FDMA is relatively less complex than TDMA and requires fewer overhead bits because each subchannel is dedicated
- Individual subchannels must be separated by guard bands to minimize interference
# Time-Division Multiple Access (TDMA)
## Characteristics and Operation
- As with FDMA, TDMA is typically used in a configuration that consists of a base station and several subscriber stations
- With TDMA, there is a single, relatively large, uplink frequency band that is used to transmit a sequence of time slots.
- Repetitive time slots are assigned to an individual subscriber station to form a logical subchannel
### Example Network With Diagram
- ![[Pasted image 20240805200026.png]]
- Each station gets an equal amount of the overall capacity of the uplink channel, thus each channel is assigned every third slot
- Similarly, each subscriber station listens during its assigned time slot on the downlink channel
	- The downlink channel may have the same slot assignment or a different one
	- In this example, the downlink band is equally divided
## Key Features of TDMA
- Each subchannel is dedicated to single station; it is not shared
- For an individual station, data transmission occurs in bursts rather than continuously
- Guard times are needed between time slots, to account for lack of perfect synchronization
- The downlink channel may be on a separate frequency band as in the example shown above.
	- This is referred to as **TDMA/FDD**
	- With TDMA/FDD, time slots assigned for subscriber station reception are typically non-overlapping with that station's transmit time slots
		- Ensure no subscriber station must transmit and receive at the same time
- The uplink and downlink transmission may be on the same frequency band, which is referred to as **TDMA/TDD**

For class #data-comm