Continues [[Circuit Switching Networks]]
Continued by [[Packet Switching Networks]]
Chapter 9.3 (From 2014)

# Context
- Once again, these techniques occur at the **PHYSICAL LAYER**
- The technology behind circuit switching is best approached by examining the operation of a single circuit switching node
- A network built around one exchange consists of a collection of stations attached to a central switching unit.
## Example Network Diagram
![[Pasted image 20240805210646.png]]
# Circuit-Switch Anatomy
- The heart of a modern system is a **Digital Switch**
	- It provides a transparent signal path between any pair of attached devices
	- Typically, this connection must allow full-duplex transmission
	- It contains the following components:
- The **Network Interface** represents the functions and hardware required to connect digital devices to the network
	- Analog telephones can also be attached if the network interface contains the logic (sampling, etc.) for converting to digital signals
	- Trunks to other digital switches carry TDM signals and provide links for constructing multiple-node detworks
- The **Control Unit** performs three general tasks
	- 1. The control unit must establish connections.
		- This is generally done on demand
		- The control unit must handle and acknowledge the request, determine if the indented destination is free and construct a path through the switch.
	- 2. The control unit must maintain these connections
		- Because the digital switch uses time-division principles, this may require ongoing manipulation of the switching elements
		- However, the bits of the communication are transferred transparently (from the perspective of the attached devices)
	- 3. The control unit must tear down these connections
		- This will be done either in response to a request from one of the parties or for its own reasons (ie inactivity)
- In general, the **Digital Switch** contains switching hardware that is controlled by the **Control Unit** to connect the devices connected to the **Network Interface**. These are all part of a **Circuit-Switch Node** or exchange
# Blocking Vs. Non-Blocking
- Blocking occurs when the network is unable to connect two stations because all possible paths between them are already in use.
- A blocking network is one in which blocking is possible 
- Hence a non-blocking network permits all stations to be connected (in pairs) at once and grants all possible connection requests as long as the called party is free
	- This requires $N \choose 2$ dedicated connections within the switch, where $N$ is the number of devices connected to the network interface
- For voice traffic, a blocking configuration is generally acceptable. Phone calls are mostly of a short duration and therefore only a fraction of telephones will be engaged at any time
- However, when data processing devices are involved these assumptions may be invalid. For example, a data entry application:
	- A terminal may be continuously connected to a computer for hours at a time
	- Hence, for data applications, there is a requirement for a nonblocking–or "nearly nonblocking" (very low probability of blocking)–configuration
# Circuit Switching Techniques
- These techniques are internal to a single circuit-switching node
## Space Division Switching
- Developed originally for analog and has been carried over to digital
- Each signal path occupies a physical link that is separated in space from other paths
- The basic building block is a metallic crosspoint (mechanical relay) or transistor gate
### Crossbar
- Space Division switching typically uses a crossbar configuration
	- Each of the $N$ stations connection to the switch is given a full duplex I/O line
	- The Input and output of each station is connected to an $N \times N$ matrix of crosspoints
	- Connecting one station to another involves enabling that crosspoint
- Crossbar switches have a number of limitations
	- The number of crosspoints grows with $N^{2}$ which can be very costly
	- The loss of a single crosspoint prevents connection between the two devices who are connected by that crosspoint; no redundancy
	- The crosspoints are inefficiently utilized; only a small fraction are engaged even when all devices are active
		- A maximum of $N$ crosspoints will ever be in use at a time
		- In the case of a 10 point station:
		- Station 1 connects to station 2, which requires one crosspoint
		- Station 1 is given 10 crosspoints on its  side where 9 of them are now disabled
		- Station 2 also has 9 disabled crosspoints
		- Each connection results in 9 disabled crosspoints
		- If each station is connected to another station, which is 5 connections, the
#### Example Diagram
![[Pasted image 20240806184736.png]]
### Multi-Stage Switch (Multiple-Stage Switch)
- Has two advantages over crossbar
	- The number of crosspoints is reduced
		- For the 10 station switch shown in the diagrams, the number of switches is reduced from 100 to 48
	- There is more than one path to connect two stations, increasing reliability
- Multistage switches are more complex
	- To establish a connection, a free path through the stages must be determined and the appropriate gates enabled
- Multistage switches may also be blocking
	- A single-stage crossbar matrix is nonblocking; there will always be a path to connect an input to an output
	- This may not always be the case with a multiple stage switch
	- ![[Pasted image 20240806185036.png]]
		- In the example above, the heavier lines indicate lines that are in use
		- In this state, input line 10 cannot be connected to output lines 3, 4, or 5 even though these output lines are available
		- Note that dimensions of a switch are $in \times out$
## Time-Division Switching
- All modern circuit switches use digital time-division techniques for establishing and maintaining "circuits"
- Involves the partitioning of a lower-speed bitstream into pieces that share a higher-speed stream with other bit streams
### Time-Slot Interchange
#### Basic Overview
- The basic building block is the time-slot interchange (TSI) mechanism
- A TSI unit operates on a synchronous TDM stream of time slots, or channels, by interchanging pairs of slots to achieve a full-duplex operation
	- MUX the inputs onto a TDM stream
	- Read the input TDM stream into a buffer
	- Rearrange the buffer onto an output TDM stream
	- Demux the output TDM stream onto the outputs
#### Characteristics
- Because each channel is provided a time slot in each TDM frame, the size of the TSI unit must be chosen for the capacity of the line, not for the actual data rate.
- TSI is simple and effective
- But the size of a switch, in terms of the number of connections, is limited by the amount of latency that can be tolerated
	- The greater the number of I/O lines, the more delay there must be to account for reading the TDM frame into the buffer and the logic for rearranging
	- Also there is latency from the TDM mux/demux processes that scales with I/O size
#### Operation
- The TSI Unit consists of three parts
	- Data Store:
		- A RAM module that may have random write but must have random read capability
		- It stores the input TDM frame and is used to output the output TDM frame
	- Address Store:
		- Contains a mapping from output TDM time slot/frame number to input time slot number
		- Essentially a mapping from each output line to its connected input line 
		- This is used to rearrange the TDM frame
	- Time Slot Counter
		- A counter that asks the address store which input slot corresponds to the current output slot
- The timeline of sending data from input to output is as follows:
- **1. The** input lines provide their data into a TDM multiplexer to produce a TDM frame
- **2.** This TDM frame is read sequentially into the data store which acts like a shift register in this context
	- For some reason the diagram below allows for random write operations
- **3.** The time slot counter starts counting up from 0. 
- **4.** At each time slot, the address store will output the input time slot number that corresponds to the proper output slot number
	- The address store will receive the time slot currently being read out to the output TDM frame and output the proper input time slot that must be read from the data store. 
- **5.** The data store outputs the data requested by the address store onto the output TDM frame
- **6.** The TDM demultiplexer routes the data to the output lines
##### Example
- Consider a scenario where Station D must send the character '!' to Station A
	- The address store maps output time slot 0, which is station A's input slot, to input time slot 3, which is station D's output slot
		- Address mapping $0 \to 3$
	- **1.** Station D's output of char '!' is placed on slot 3 of the input TDM frame
	- **2.** The entire TDM frame populates the Data store
		- Note that this introduces delay
	- **3.** The time slot counter outputs 0 to the address store's address line
	- **4.** The address store outputs address 3, indicating that output TDM slot 0 corresponds to input TDM slot 3
	- **5.** The data store outputs char '!' to the 0th time slot of the output TDM slot
		- All the other TDM slots are populated
	- **6.** The TDM demux routes char '!' to A's input line
#### Diagram
![[Pasted image 20240806185549.png]]
- Note the write address is typically unused and generally unnecessary

## Time-Multiplexed Switching
- **AKA Time-Space-Time (TST)**
- To overcome the latency problems of TSI, contemporary time-division switches use multiple TSI units that each carry a portion of the total traffic
- To connect two channels entering a single TSI unit, their time slots can be interchanged as described above
- However, to connect a channel on one TDM stream to a channel on another TDM stream, some sort of space division switching is needed
- We do not wish to switch all time slots from one TDM stream to another; it is preferrable to do it one slot at a time.
- This is known as TMS
- 