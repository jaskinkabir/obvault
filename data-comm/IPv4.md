Continues [[TCP-IP Protocol Architecture]]
Continued by [[IPv6]]

# IPv4 Headers
- An IPv4 header is a minimum of 20 octets. The header, together with the segment from the transport layer, forms an **IP-level PDU** aka an **IP Datagram/Packet**
- ![[Pasted image 20240705164929.png]]
- Includes:
	- **Version**:
		- Which IP version
	- **IHL**: Internet Header Length
		- Size of the header, **4 bits**
		- Measured in 32-bit words (4 bytes)
		- Minimum of 5 (header is minimum 20 bytes)
	- **DS**: Differentiated Services
		- **8 Bits**
		- Type of service
	- **ECN: Explicit Congestion Notification**
		- End-to-end notification of network congestion
		- Source provides congestion control
		- **2 bits**
			- 0: No ECN
			- 1 or 2: set by sender, indicate ECN capable
			- 3: set by router, indicate congestion has been encountered
	- **Total Length**
		- **16 bits** indicates total packet size in bytes
		- header+data
	- Identification
		- **16 Bits**
		- Sequence number
	- Flags
		- **3 bits**
		- Only 2 are defined
			- More
			- Don't fragment (datagram discarded if exceeds max size)
			- 
	- Fragment Offset
		- **13 bits**
		- In 64 bit units
		- Data field must be a multiple of 64 bits (except for the last fragment)
			- 8 bytes
	- **Time To Live**
		- Lifetime of packet to prevent network failure in the event of a routing loop
		- Called Hop Limit in IPv6
		- Decremented
	- **Protocol
		- Field indicates whether this packet is part of a TCP or UDP segment
			- TCP = 6
			- UDP = 17
			- ICMP = 1
			- 
		- Next higher layer to receive data field at destination
	- **Header checksum**
		- Separate from the Transport Layer checksum
		- Only hashes the header itself
		- Verified at each router
	- **32 bit** source and destination addresses
	- Padding will fill header to a multiple of 32 bits / 4 bytes
## IHL Examples
In IPv4, what is the length of the data field given an IHL  
value of 12 and total length value of 40,000?
- Header length is $4*12 = 48$ bytes
- Total length is $40000$ bytes
- Data length is $40000 - 48 = 39952$ bytes
In an IPv4 packets, the value of the IHL is 5, the value of  
the total length field is 40. How many bytes of data are  
carried by this packet?
- Header length is $4 * 5 = 20$ bytes
- Total length is $40$ bytes
- Data length is $40 - 20 = 20$ bytes
## Offset Example
An IPv4 packet header has the offset value 100, IHL=5,  
total length=100 (all in decimal). What are the number of  
the first byte and the last byte?
- Header is $4*5=20$ bytes
- Total length is $100$ bytes
- Data length is $80$ bytes
- Offset is $64 * 100 = 6400$ bits
- Byte offset is $\frac{6400}{8}=800$ bytes
- **First byte is Byte #800**
- **Second byte is Byte #879**
# The IPv4 Address

![[Pasted image 20251008180902.png]]

## Format
- 32 bit global internet address
- Dotted decimal notation: a decimal # representing each of the 4 octets
	- 192.228.17.57 = 
	- 11000000 11100100 00010001 00111001
- Has a network part and host part
- Different classes allow for different sized network and host fields
## Classed Addressing
### Class A
- Addresses start with binary 0
- Range from 1.x.x.x to 126.x.x.x
	- There are 126 Class A network numbers
- All allocated
- 7 bits for network
- 24 bits for host
- Few networks, many hosts
### Class B
- Addresses start with binary 10
- Range 128.x.x.x to 191.x.x.x
- 14 bits for network 
- 16 bits for host
- All allocated
- Medium # of networks, medium # of hosts
### Class C
- Addresses start with binary 110
- Range 192.x.x.x to 223.x.x.x
- 21 bits for network, 8 bits for hosts
- Many networks, fewer hosts
- Nearly all allocated
## Addressing Mode
- Usually, addresses refer to a single system or port
	- This is called individual or unicast addressing
- However, addresses can refer to more than one entity or port
	- Multiple simultaneous recipients of data
	- Broadcast for all entities within a domain
	- Multicast for specific subset of entities
- ![[Pasted image 20251009134721.png]]
## Subnets and Subnet Masks
- Host portion of address partitioned into subnet number and host number
- Each subnet assigned a subnet number
- 
- Use subnet mask to figure out how many bits are for the subnet number
	- Mask is a 32 bit number in which the $n$ leftmost bits are 1s and the $32-n$ rightmost bits are 0s
	- Erase the portion of the host field and get subnet ID through bitwise AND
- The bits in the mask that are 0s represent the host portion of the host address within the IP address
![[Pasted image 20251009190231.png]]
![[Pasted image 20251009190458.png]]
### Mask Example Problem
Subnet mask: 255.255.240.0  
What is the max # of hosts in each subnet?
- Mask in binary:
	- 11111111 11111111 11110000 00000000
- 12 bits for host
- Max number of hosts = $2^{12} = 4096$
![[Pasted image 20251009191213.png]]

## Classless Addressing
- No classes, but addresses are granted in blocks
	- This is done to overcome address depletion and give more organization access to the internet
- **Restriction**
	- 1. Addresses in a block must be contiguous
	- 2. Number of addresses in a block must be a power of 2
	- 3. First address must be evenly divisible by the # of addresses
- The Mask: In IPv4 addressing, a block of addresses **x.y.z.t/n**, /n defines the mask for the address x.y.z.t
	- The mask denotes how many bits are used to denote the subnet/organization
	- Thus, the last $32-n$ bits are used for the host
	- Each subnet can have $2^{32-n}$ hosts
- The first address in a block is not assigned to any device, it is used as the network address representing the organization to the world
- ![[Pasted image 20251013184032.png]]
### Example problem
- In a block of addresses, the IP address of one host is 25.34.12.56/16
	- What is the first address in the block
		- Address of host is 
		- 00011001 00100010 00001100 00111000
		- 0 out last 16 bits to get first address
		- 00011001 00100010 00000000 00000000
		- **25.34.0.0**
	- What is the last address in the block
		- **25.34.255.255**
	- How many IPs are in the block?
		- 32-16 = 16 bits for hosts
		- $2^{16}=65536$ addresses
For class #data-comm