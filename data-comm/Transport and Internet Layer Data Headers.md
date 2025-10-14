Continues [[TCP-IP Protocol Architecture]]
Continued by [[IPv4]]
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

For class #data-comm