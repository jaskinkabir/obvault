Continues [[Protocol Architecture]]
Continued by [[Transport and Internet Layer Data Headers]]
Continued by [[Data Link Flow Control]]
## TCP/IP 
- Developed by DARPA (US Defense Advanced Research Project Agency)
- Used by the global internet
- Generalities
	- Above the physical layer, each prottocol entity sends data down to the next lower layer
	- Each layer can only talk to the ones above and below it
	- Passing information between layers in done in a standard way
	- There is no direct communication between peer layers except at the physical layer
		- Data moves down from the source application, across the physical, and then back up to the destination application
## 5 TCP/IP Layers
![[Pasted image 20240704162650.png]]
### Physical Layer
- Provides a physical interface between computer hardware
- Characteristics of the transmission medium include signal nature, data rate, etc
	- Medium, signal encoding technique, data rate, bandwidth, connector
- The format of the data is **Bit Streams**
- Examples of tasks include 
	- encoding and transmission of data
	- Error detection
	- Basic Error Recovery
- Examples include twisted pair, optical fiber, satellite, and terrestrial microwave
### Network Access/Data Link Layer
- Exchanges data betwen two end systems attached to the same network
- Acts as a logical interface to network hardware
- Format of the data is **Frames**
- Examples of tasks: Access to and routing data across a network
- Network access protocols include WiFi and Ethernet
### Internet Layer
- Shields higher layers from details of physical network configuration
- Implements procedures needed to allow data to travel across multiple interconnected networks
- Uses the Internet Protocol (IP) to provide routing
- Routing functions across multiple networks
- Implemented in routers
- Format of the data is **packets**
- #### Protocols
	- IPv4 and IPv6: broad categories that encompass the following
	- **ICMP:** Internet Control Message Protocol, used on IPv4 networks to indicate error messages
	- **OSPF:** Open Shortest Path First, routing protocol
	- **RSVP:** Resource Reservation Protocol
		- Reserve resources across a network using integrated services model
	- **ARP:** Address Resolution Protocol
		- Used to request the MAC address associated with a given IP, used in IPv4
	- **RARP:** Reverse ARP, used to request IP from MAC
### Transport Layer
- Ensures reliable end-to-end data transfer between end devices
- Tasks:
	- Transport, error control, flow control, congestion control
- Format of the data: **Segment**
- Uses two types of protocols: 
	- UDP: User Datagram Protocol
	- TCP: Transmission Control Protocol
- #### UDP: User Datagram
	- Connectionless protocol
	- Establishes low-latency, loss tolerating connections
	- Enables data transfer before an agreement is provided by the receiver, which allows for rapid transmission
	- Does not guarantee delivery, preservation of sequence, or protection against duplication
	- Faster than TCP, but not reliable
- #### TCP: Transmission Control
	- Connection oriented and reliable protocol
	- Transport layer protocol for most applications
	- A **TCP segment** is the basic protocol unit
	- TCP tracks segments between entities for the duration of each connection
	- Slower than UDP but less reliable. It guarantees delivery.
- #### Differences between TCP and UDP
	- TCP is slower but more reliable
		- It can only handle a connection between two devices (unicast)
	- UDP can cast data from one device to several others:
		- Multicast: To many but not all connected nodes
		- Broadcast: To all nodes
	- ![[Pasted image 20240704165439.png]]
### Application Layer
- Conmtains the logic needed to support user applications
- Provides access to the TCP/IP Environment to applications
- Format of the data: **data**
- A separate module is dedicated to each type of application protocols include 
	- SMTP: Simple Mail Transfer Protocol
	- HTTP, FTP, DNS
## General Guidelines
- Data format from top to bottom:
	- Data: App
	- Segment: Transport
	- Packet: Internet
	- Frame: Data Link
	- Bit Stream: Physical
- End-To-End: Transport and Above
### Example problem
TCP (transport) segment contains 1500 data and 160 header
Internet layer appends 160 more to its packet
Network access appends 24 bit header to its frame
Destination internet layer can receive 800 bits per packet. How many total bits are delivered to the destination internet layer? 

- TCP needs to send 1660 bits of its segment
- IP needs to send 1660+160=1820 bits
- The maximum amount of data that can be transferred at once is 800 bits - (24 bits of network access header)= 776 bits per frame
- 1820/776 = 3 packets
- Total data = 
	- $800 *2 + (24+1820-776*2)=1892$ bits
- The only data that is added several times is each network access header appended to each dataframe. 
	- The TCP segment header and the IP header are added once
	- The data is split at the network access layer, not the internet layer
	- 


For class #data-comm 