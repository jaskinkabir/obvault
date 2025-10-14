Continues [[IPv4]]
Continued by [[The IPv6 Address]]
## IPv4 vs IPv6
- IPv6 adds extra functionality to IP, but the driving force behind its development was that the internet grew too large
	- **IPv4 is running out of addresses!**
- IPv4 uses a 32 bit address space which allows for only ~4.3 billion addresses
	- An IPv4 address is written as 
		- 4 bytes in decimal numbers separated by dots
	- Not even enough for half of all humans
- Also, two level addressing (network and host) wastes space
- IPv6 has a whopping 128 bit address space, which takes up 8 total 32 bit words of each IPv6 header, 4 for each address
	- This allows for $3.4\times10^{38}$ addresses
	- We will probably never run out
	- An IPv6 address is written as
		- 8 groups of 2 bytes written in hex
		- Separated by colons
		- Terminating an address with a double colon means it is followed by all 0s
		  
## Other IPv6 Enhancements
- Improved option mechanism
	- Separate optional headers between IPv6 header and transport layer header
	- Most are not examined by intermediate routers
		- Improved speed and simplified router processing
		- Easier to extend options
	- The option headers are extension headers that follow the fixed 40-byte IPv6 header to carry optional info. Routers don't need to read this stuff so it's faster
- Dynamic assignment of addresses
- Increased addressing flexibility
	- Anycast: Delivery to one of a set of nodes (usually nearest)
	- Improved scalability of multicast addresses
- Support for resource allocation
	- Labeling of packets to particular traffic flow
	- Allows special handling of each type
## IPv6 Headers
- ![[Pasted image 20251013190340.png]]
- ![[Pasted image 20240705165400.png]]
- Notice that the IPv6 base header has fewer fields than the IPv4 header. This improves processing speed
- Includes:
	- **Version**:
		- Which IP version
	- **DS**: Differentiated Services
		- **8 Bits**
		- Type of service
	- **ECN: Explicit Congestion Notification**
		- End-to-end notification of network congestion
		- Source provides congestion control
		- **2 bits**
	- **Flow Label**
		- **20 bit** label indicating current packet's position in a group of packets
		- A flow is a sequence of packets with same source and destination
		- It is uniquely identified by the combination of source, destination addresses and a 20-bit flow label
		- Packets of the same flow are assigned the same flow label and handled in the same way
		- The flow label is randomly and uniformlu selected from $[1,\,2^{20}-1]$
			- **Restriction**: Cannot reuse flow label in use
			- Zero flow label: indicates no flow label is in use
	- **Payload Length**
		- **16 bits**
		- Size of payload, including all extension headers plus data
		- Measured in bytes
	- **Next Header**
		- **8 Bits**
		- Identifies type of the next header
		- Either some type of ipv6 extension header or the header for the next layer up
	- **Hop Limit**
		- Called time to live in IPv4 
		- Hop counts to prevent route loop
		- **8 Bits*
	- **Source and Destination Addresses**
		- **128 bits each**.
		- Each address takes up 4 32 bit words for a total of 8
# The IPv6 Address

- 128 bits long, 8 16-bit numbers separated by colons
- Each 16-bit number is represented by 4 hexadecimal numbers
- Eg. 2001:0DB8:0055:0000:CD23:0000:0000:0205
- 1-3 zeros that appear as the leading digits in a group may be dropped
	- 2001:**DB8**:**55**:**0**:CD23:**0**:**0**:**205**
- A group of all zeroes or consecutive groups of all zeroes can be substituted by a double colon, but only once in the address
	- 2001:0DB8:55<u>::</u>CD23:0:0:0205 or
	- 2001:0DB8:55:0:CD23<u>::</u>0205
- Single interface may have multiple unicast addresses
- Three types of addresses
	- Unicast: A single interface
	- Anycast
		- For a set of interfaces (typically different nodes)
		- Delivered to any one interface
		- Usually the "nearest" (according to routing table)
	- Multicast
		- For a set of interfaces 
		- Delivered to all interfaces identified
# IPv6 Extension Headers
![[Pasted image 20251013191957.png]]
## Hop-By-Hop options:
- Every router must process this header extension
- Contains
	- Next header **8 bits**
	- Header extension length (**8 bits**)
		- Given in 64-bit units (8 byte units)
		- Denotes length of this header
	- Options: Option type (8 bits) + Length (8 bits, length of the option data field in bytes) + Option Data (variable length)
		- Jumbo payload (32 bits): Length of packets in bytes excluding the header
			- IPv6 supports sending up to $2^{32}$ bytes
			- Used when sending packets over $2^{16}=65536$ bytes
			- Payload length in IPv6 header = 0, no fragment header
		- Router alert
			- Tells router that the contents of the packet are of interest to the router and it must handle the control data – for traffic control purposes
			- Asks intermediate routers to examine packets
			- PAD1: Insert one byte of padding into the Options area of header
			- PadN 
				- Insert $N \geq 2$ bytes of padding into the options area of the header
				- This is to ensure that the header is a multiple of 8 bytes
## Fragment Header
![[Pasted image 20251014144321.png]]
- Includes
	- Next Header (**8 bits**)
	- Reserved **8 bits** to keep format
	- Fragment offset (**13 bits**)
		- Position in 64-bit units
	- Reserved **2 bits**
	- More flag
	- Identification (**32 bits**)
		- All fragments with the same identifier, source addr, and destination addr are reassembled
## Destination Options
- Same format as Hop-By-Hop options
- Only read by destination node
## Routing 
![[Pasted image 20251014144541.png]]
- Similar to IPv4 source routing
	- List of one or more intermediate nodes to be visited
- Includes
	- Next Header (**8 bits**)
	- Header Extension Length (**8 bits**)
		- In bytes
	- Routing type (**8 bits**) Only Type 0 defined
	- Segments left (**8 Bits**)
		- Number of nodes still to be visited
- The data in the header is a list of addresses
	- ![[Pasted image 20251014144856.png]]
	- If A wants to send a packet to B and knows the route (source routing), it will set the base header's source to its address and the destination address to router 1
	- Then it will list the intermediate nodes in the data of the optional routing header. It will also fill the Segments Left field with the number of nodes in the route
		- The ultimate address (addr of B) is the last address in the routing header
	- Each router along the path will decrement the Segments Left field, and put the next address of the routing header into the destination field of the base header
	- 

For class #data-comm
