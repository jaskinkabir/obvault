Continues [[TCP-IP Protocol Architecture]]
Continued by [[The IPv4 Address]]
Continued by [[IPv6]]
## Headers
- A set number of bits appended to whatever data that must be transmitted
- Contains information about the message, how it should be transmitted, source, destination, etc
- Each layer except for the top level appends its header to the message
	- The final message transmitted by the bottom (physical) layer contains its header and those of all layers above it
	- This allows for full abstraction at each layer
## TCP Headers (Transmission Control Protocol)
- Include the following information
	- **Destination Port**
		- Each port is **16 bits**
		- Application port at destination that message should be delivered to
	- **Sequence Number**
		- Contains the number of bytes already sent; **32 bits**
		- TCP will break the application data into several segments according to the maximum PDU length of the IP Layer
		- Each segment must be numbered so that the TCP entity at the destination can reorder the segments if they arrive out of order
	- **Acknowledgement Number**
		- Number of bytes received; **32 bits**
	- **Flags**
		- Indicate a particular state of connection
		- "SYN", "ACK", "FIN"
		- **8 bits**
	- **Header Length**
		- **8 bits** when options are not used.
		- If options are used, this field can be up to **40 bits**
			- Open/close connection, receive request, send ack...
	- **Window**
		- Receiver window size; **16 bits**
	- **Checksum**
		- **16 Bits**
		- The result of a hash function of the contents of the remainder of the segment for error detection
	- **Urgent pointer**
		- **16 bits**; unused
		- Points to the last byte of the urgent dat a if present
	- **Options**
		- Variable length, usually 0 at the end of the header
	- **Data**
		- Variable length between 0-1500
	- **Padding**
		- If data length is less than the minimum, padding is added
- Each segment is handed over to the IP, with instructions to transmit to B. IP appends a header of control info to each segment to form an **IP Datagram** aka packet
- Each TCP header is a minimum of 20 octets, or 160 bits
- It includes the following sections for flow control
	- Seq Number
	- Ack number
	- Window
	- These sections are called fields
## UDP Headers (User Datagram Protocol)
- Because UDP does not guarantee delivery, reservation of sequence, or protection against duplication, UDP headers are much shorter
- UDP headers are a minimum of 8 octets broken up into 4 16 bit fields
	- Source port (**16 bits**)
	- Destination Port (**16 bits**)
	- Segment Length (**16 bits**)
	- Checksum (**16 bits**)
- ***In essence, all UDP does is add a port addressing capability to the IP layer***
	- Also adds an optional checksum
- ![[Pasted image 20240705164422.png]]
## IPv4 Headers
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

For class #data-comm