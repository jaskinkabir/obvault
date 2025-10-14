Continues [[LAN and WAN]]
Continued by [[TCP-IP Protocol Architecture]]
Continued by [[Standardization Within a Protocol Architecture]]
Continued by [[Connectionless Internetworking]]
Continued by [[Fragmentation and Reassembly]]
## Protocol
- Defined as a set of rules or conventions that allow peer layers to communicate (A common language)
- For example: The tasks that must be performed to transfer a file between two PCs
	- Source must either activate direct data comm path or inform the comm network of the destination's identity
	- It must then ascertain that the destination is prepared to receive the data
	- The file transfer application on the source system must ascertain that the file management system on the destination is prepared to accept and store the file
	- If the file formats are different, one system must perform a format translation
- Protocols define network characteristics
	- Access method
	- Allowed physical topologies
		- Mesh, Star, Ring, etc
	- Types of cabling
	- Speed of data transfer
	- Data format
- All nodes in the network must obey the protocol
## Basic Functions of a Protocol
### Encapsulation
- Defined as addition of control info to data
- Data transferred in blocks: PDUs (Protocol Data Units)
		- Each PDU contains data and ctrl info
		- Some PDUs only have ctrl info. Called control packets
	- Three categories of control
		- Address: of tx/rx
		- Error-detecting code
		- Protocol control: Additional info to implement protocol functions
- Data needs to be encapsulated with control info at each layer
	- ![[Pasted image 20240704161212.png]]
- Protocol Data Unit
	- A PDU contains user data + control information from the next higher layer
	- Has different names depending on the layer
	- **Data Link:** Frame
	- **Network:** Packet
	- **Transport:** Segment
	- Segment goes in a packet which goes into a frame
		- The lowest layer has the longest messages
	- ![[Pasted image 20240704161439.png]]
		-  FCS: Frame Check Sequence (error detection code)

### Fragmentation and Reassembly
#### Fragmentation
- Breaks up data into smaller blocks
- Why?
- Networks may only accept blocks of up to a certain size
- More efficient error control: smaller retransmissions
- Fairer: prevents a station from monopolizing the medium
#### Reassembly
- Segmented data must be reassembled into messages
- More complex if PDUs are out of order
##### Where to do Reassembly?
- At destination
	- Packets may get smaller as data traverses the internet
- Intermediate re-assembly
	- All fragments must go through same router, which inhibits dynamic routing
		- This is typically the last router before the terminal station
### Connection Control
- Connectionless data transfer: no connection setup before data transfer
	- Each PDU treated independently, datagram
- Connection-oriented data transfer
	- Logical connection established between entities
	- Virtual circuit
	- 3 phases: setup transfer teardown
### Ordered Delivery
- PDUs may arrive out of order
	- Different paths through network
- Number PDUs sequentially to easily reorder received packets
- Finite sequence number field
	- Numbers repeat modulo max number
	- Maximum sequence number must be greater than max number of outstanding PDUs
		- Outstanding meaning in transit or have not received ACKs
### Addressing
- Addressing level: Level in communications architecture at which entity is named
	- Network level:
		- Globally unique IP address
		- Used to route PDU through network
	- At destination, data must be routed to a certain app/process
		- Each process assigned an identifier
		- In TCP/IP these are called ports
		- One station may have many of these processes and associated ports
	- Need unique addresses for each device interface on the network (MAC addresses)
- Addressing Scope
	- Global address: IP
	- Port above the network level is unique within a system, but need not be globally unique
## Layered structure
- Networking protocols are broken up into layers:
	- Starting with the physical medium of transportation, working up in abstraction to the application layer or even higher (presentation)
	- Most broad layers are network access, transport, application
- Network Access layers:
	- Concerned with the exchange of data between the computer and its network
- Transport layers:
	- Converts application layer's data into the format necessary for transport across the network
- Application layers:
	- Concerned with interpreting the data received from the network access layer into a usable format
	- Each application has a unique address within the computer, so the transport layer can support multiple applications
		- Ex: port 25565 for Minecraft

For class #data-comm 
