Continues [[LAN and WAN]]
Continues [[Multiplexing (PHYSICAL MUX)]]
Continues [[Multiple Channel Access (DATA LINK MUX)]]

Continued by [[Packet Switching Networks]]
Continued by [[Circuit Switching Under the Hood]]

Chapter 9.2 (Based on textbook written in 2014)
# Overview
- **THESE TECHNIQUES OCCUR ON THE PHYSICAL LAYER**
- Communication via circuit switching implies that there is a dedicated communication path between two stations,
- That path is a connected sequence of links between network nodes
- On each physical link, a logical channel is dedicated to the connection
## Operation Via Three Phases
Communication via circuit switching involves three phases
- **1. Circuit Establishment**
	- Before any signals can be transmitted, an end-to-end circuit must be established.
	- For example: Consider station A wants to connect to station E
		- 1. Station A sends a request to node 4 requesting a connection to station E
		- 2. Typically, the link from A to 4 is a dedicated line
		- 3. Node 4 must find the next leg in a route leading to E
		- 4. Based on routing information, measures of availability, and perhaps cost, node 4 selects the link to node 5
		- 5. 4 then allocates a free channel (using FDM or TDM) on that link, and sends a message requesting connection to E
			- So far, a dedicated path has been established: $A\to 4 \to 5$
			- Because a number of stations may attach to 4, it must be able to establish internal connections between multiple stations to multiple nodes
			- The remainder of the process proceeds similarly
		- 6. Node 5 allocates a channel to node 6 and internally ties that channel to the channel from node 4.
		- 7. Node 6 completes the connection to station E
		- 8. A test is made to determine if E is busy or prepared to accept the connection
		- A dedicated link has been established with the path: $A\to 4 \to 5 \to 6 \to E$
- **2. Data Transfer**
	- Data can now be transmitted A through the network to E
	- This communication may be analog or digital, but the use of digital transmission for both voice and data is now the dominant method
	- Note that in between each connection between one node and another, or between a station and a node, there is an internal switch through that node to connect the two links that the node is connecting
		- A-4 link, internal switching through 4, 4-5 channel, internal switching through 5, 5-6 channel, internal switching through 6, 6-E link.
	- Generally, **The connection is Full Duplex**
- **3. Circuit Disconnect**
	- After some period of data transfer, the connection must be terminated. Usually, this is through the action of one of the two stations.
	- Signals must be propagated to nodes 4,5, and 6 to deallocate the dedicated resources
### Example Diagram for Public Telephone Network
![[Pasted image 20240805205709.png]]
## Characteristics
- Note that the connection path is established before data transmission begins
- Thus, channel capacity must be reserved between each pair of nodes in the path, and each node must have available internal switching capacity to handle the requested connection
- The switches must have the intelligence to make these allocations and to devise a route through the network
	- How do the nodes communicate their availability to each other?
- Circuit switching can be rather inefficient. 
	- Channel capacity is dedicated for the duration of a connection, even if no data is being transferred. 
	- Voice connections have more utilization than computer connections.
		- Computer connections might keep the channel idle for the majority of the connection
- In terms of performance:
	- There is a delay prior to signal transfer for call establishment
	- However, once the circuit is established, the network is effectively transparent to the users
	- Information is transmitted at a fixed rate with no delay other than $T_{p}$ through the medium
	- **The delay at/through each node is negligible**
# Example Networks
## Public Telephone Network
- Circuit switching was developed to handle voice traffic, but is now also used for digital data
- The best known example of such a network is the Public Telephone Network
	- This is a collection of national networks interconnected to form the international service
	- Although initially designed for analog telephones, it now handles substantial data traffic via modem and is gradually being converted to a digital network
## Private Branch Exchange (PBX)
- Used to interconnect telephones within a building or office
- Circuit switching is also used in private networks, typically set up by a corporation or other large organization to interconnect its various sites
	- Such a network usually consists of PBX systems at each site interconnected by dedicated, leased lines obtained from a carrier such as AT&T
## Data Switch
- Used to interconnect digital devices
# Public Telecommunication Networks
## Architectural Components
### Subscribers
- Devices that attach to the networks
	- Most are still telephones, but percentage of data traffic increases each year
### Subscriber Line
- The link between the subscriber and the network
	- Also called the **subscriber loop** or **local loop**
- Almost all local loop connections use a twisted-pair wire
- The length of a local loop is typically on the order of kilometers to a few tens of kilometers
### Exchanges
- The switching centers in the network
- A switching center that directly supports subscribers is known as an **End Office**
	- Typically, an End Office will support many thousands of subscribers in a localized area
	- There are over 19000 end offices in the US
		- It would be impractical for each end office to have a dedicated link to each other end office, which would require over $2 \times 10^8$ links
		- Rather, intermediate switching nodes are used
### Trunks
- The branches **between exchanges**
- Trunks carry multiple voice frequency circuits **using either FDM or Synchronous TDM**
	- Remember that these are physical layer techniques. We are operating at the physical layer with circuit switching
- These are called Carrier systems in the notes about multiplexing and multiple access
	- These Trunks are what are defined by the hierarchy tables
## Example Diagram
- ![[Pasted image 20240805205849.png]]
	- a,b,c and d are Subscribers, 
	- The links between them and the end offices are Subscriber Lines 
## Features
- Subscribers connect directly to an end office, which switches traffic between subscribers and between a subscriber and other exchanges
- The other exchanges are responsible for routing and switching traffic between end offices.
- Circuit switching technology has been driven by voice traffic applications.
	- The key requirements for voice traffic are that there must be virtually no transmission delay and certainly no variation in delay
	- A constant signal transmission rate must be achieved, because TX and RX occur at the same signal rate
	- These requirements are necessary for natural human conversation
	- Furthermore, the quality of the signal must be sufficiently high to provide, at a minimum, intelligibility
- The main advantage of circuit switching is that it is transparent to the stations
	- The two stations can act as if they are directly linked
	- No special networking logic is required at the stations
- 


For class #data-comm