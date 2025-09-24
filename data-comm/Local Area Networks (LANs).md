Continues [[LAN and WAN]]
Continued by [[Ethernet and MAC]]
# Topologies
## Bus Topology
![[Pasted image 20250904150235.png]]
- All stations attach, through a tap, directly to a bus
	- 1 common transmission medium
	- Terminator absorbs packets at end of bus
- Full duplex connection
- Transmissions heard by all stations, need to identify target station
- Need to regulate transmission
	- To avoid collisions ensure only one packet is sent at a time 
		- round-robin, contention, reservation
	- To avoid one station hogging the line: send data in small blocks or frames
## Star/Hub and Spoke
- Each station connected to a common central node through 2 simplex links
- This is a physical star, but a logical bus
- Transmission is heard by all stations, and only one station can transmit at a time
- Central node can act as a frame switch
	- Incoming frames are buffered and retransmitted on outgoing link to the destination station
# LAN Protocol Architecture
- LAN is relevant to the lower two layers. Higher layers operate independently of network architecture
	- Physical and data link layers
- IEEE 802 reference model
	- Physical 
	- Logical Link Control (LLC)
	- Media Access Control (MAC)
	- The LLC and MAC protocols are sublayers of the datalink layer
## 802 Layers
![[Pasted image 20250904151612.png]]
### Physical
- Encoding/decoding
- Preamble generation/removal (synchronization)
- Bit transmission/reception
- Transmission medium and topology
### Logical Link Control (LLC)
- Interface to higher levels
- Flow control and error correction
### Media Access Control (MAC)
- On transmit: assemble data into frame with address and error detection fields
- On reception: disassemble frame. address recognition, error detection
- Govern access to transmission medium
	- Not found in traditional layer 2 data link control
	- Only in LAN is MAC found
- For the same LLC implementation, several MAC implementations may be available

#### Where is control?
- Central
	- One central MAC controller that commands all stations on LAN
	- Pros: 
		- Greater control
		- Simple access logic at station
		- Avoids problems of distributed coordination
	- Cons:
		- Single point of failure
		- Potential bottleneck
- Distributed
#### How is Media Access Controlled?
- Synchronous
	- Specific capacity dedicated to each connection (FDM, SyTDM)
- Asynchronous
	- Capacity is dedicated in response to demand (StTDM)
	- Round-Robin
		- Each station takes turns to transmit
		- Good if many stations have data to transmit
	- Reservation
		- Time is divided into slots
		- Good for stream traffic (lengthy continuous transmission)
	- Contention (No control at all)
		- Each station listens to the medium to detect, prevent, and handle collisions
		- Good for bursty traffic
		- All stations contend for time
		- Distributed and simple to implement
		- Efficient under moderate load, but tends to collapse under heavy load
#### MAC Frame Format
![[Pasted image 20250904153318.png]]
- MAC Layer receives data from LLC layer
- MAC Layer detects and discards errored frames
- LLC will retransmit unsuccessful frames
	- This is the extent of error correction

# Bridges and Routers
- How to provide interconnection to other LANs/WANs? Use bridge or router
- Bridge is simpler
	- Connects similar LANs
	- Identical protocols for physical and data link layers
	- Minimal processing
- Router is more general purpose
	- Interconnects various LANs and WANs
## Functions of a Bridge
- Read all frames transmitted on one LAN
- Retransmit each frame to stations on the other LAN (using MAC protocol)
- **No modification** to content or format of the frame; bitwise copy
- Minimal buffering to meet peak demand
- Contains routing and address intelligence (different from repeater)
	- Must be able to tell which frames to pass
		- For example, addresses 0-4 are on current LAN, only send addresses 5+ across bridge
		- May be more than one bridge to cross from source to destination
- Bridging is transparent to stations

## Bridge Protocol Architecture
- IEEE 802.1D defines protocol arch for bridges
- Station address is at MAC level
- Bridge does not need LLC layer because it only relays MAC frames
	- No flow/error ctrl
## Fixed Routing
- The network must be preconfigured with optimal routes between endpoints
	- Fewest hops
	- Only changed when topology changes
- Each bridge has two routing tables, one for each direction
## Spanning Tree
- Bridge automatically develops routing table
	- Automatically updates in response to changes
- Frame forwarding
	- Maintain forwarding database for each port
	- For a frame arriving on port x
		- Search db to see if mac address is listed for any port except X
		- If address not found, forward to all ports except X
		- If address listed for port Y, check for blocking or forwarding state
		- If not blocked, transmit frame through port Y
	- Whenever a frame is received, it notes the source address in its receiving forwarding table (learning)
### Address Learning

### Loop problem
- ![[Pasted image 20250909151546.png]]
- If A sends a packet to B, both bridges will forward this packet onto B's bus
- If one bridge forwards the data before the other, the second bridge will learn that station A is on B's side
- This is a problem because that is not true
### Loop Resolution
- Address learning works for tree layout
- According to graph theory, for any connected graph there is a spanning tree that maintains connectivity but contains no closed loops
# Hubs and Switches
## Hubs
- Active central element of star topology
- Hub acts as a repeater, simply bitwise copies any incoming messages on all output lines
- Line consists of 2 unshielded twisted pairs (limited to about 100m)
- Optical fiber (500m)
- Physical star, logical bus
- Collision caused by simultaneous tx
## Layer 2 Switches
- Central hub acts as switch
- Incoming frame from particular station switched to appropriate output line
- Unused lines can switch other traffic
- More than one station can transmit at a time, which increases capacity of LAN

### Types of Layer 2 Switch
- Store and forward switch
	- Accepts frame on input, buffers, then routes to appropriate output
	- Delay between sender and receiver
- Cut through switch
	- Takes advantage of destination address appearing at beginning of frame
	- Switch begins repeating frame onto output line as soon as it recognizes destination address
	- Has the highest possible throughput, but cannot check crc for error detection
	- Risk of propagating bad frames
### Layer 2 Switch vs. Bridge
- Layer 2 switch can be viewed as a full-duplex hub
- Bridges only analyze and forward one frame at a time, while switches can handle multiple at a time
For class #data-comm


