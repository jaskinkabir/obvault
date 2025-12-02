[[TCP-IP Protocol Architecture]]
[[Transport Protocols]]
[[UDP]]
[[TCP Congestion Control]]
# Overview
- Connection oriented, provides a reliable end-to-end byte stream over an unreliable internetwork
- TCP service is obtained by both tx and rx creating endpoints (sockets)
	- The socket is a combination of the IP address and the port number (typically 16 bits)
	- Port # below 1024: well known ports, reserved for standard services
		- 21-FTP
		- 23-Telnet
		- 25-SMTP
		- 80-HTTP
- Every data byte on a TCP connection has its own 32-bit sequence number
# The TCP Segment
- 20-byte header + optional extensions + data bytes
- Max data segment length: 65535 bytes
	- Data length = 65535 - 20 - 20 = 65495
		- Max IP packet length = 65535
		- Subtract IP header length (20)
		- Subtract TCP header length (20)
	- Data byte can be 0 for ACK and control messages
	- Segment size ≤ MTU of each network
## The TCP Header  (>=20 Bytes)
![[Pasted image 20251030145114.png]]
- **Source and Destination Ports**: 16 bits eac
### Sequence Number (32 bits):
- Works on the byte level
- The sequence number in the segment header is the byte number **of the first byte of the payload**
- SYN flag affects the meaning of this number
	- SYN=0: seq # of first data byte in the segment
	- SYN=1: ISN, first data byte is ISN+1, for connection request
### ACK (32 bits)
- Indicate next byte expected
- Only valid if ACK flag is set
### Data Offset (4 bits)
- Header length in 32-bit words
- Multiples of 4 bytes
- Equivalent of IHL in IPv4
### Reserved (6 bits)
- 2 bits proposed for ECN
### Flags (6 bits)
- **Flags (6 bits):**
#### URG
- Urgent pointer field is in use
#### ACK
- Acknowledge field is in use (ACK field is valid)
#### PSH
- Request receiver to immediately deliver data to the application upon arrival and not buffer it until a full buffer has been received
#### RST
- Reset a connection, reject a segment, or reject a connection request
#### SYN
- Establish connections
- SYN=1, ACK=0: connection request
- SYN=1, ACK=1: connection accepted (ACK field valid)
#### FIN
- Release a connection
### Window Size (16 bits)
- How many bytes may be sent starting at the byte acknowledged that the sender is willing to accept
- Window management and ACK are decoupled
- If WIN=0, TX cannot send packets except for these two cases:
	- Urgent data may be sent (kill remote process)
	- TX may send 1 byte segment to make receiver re-announce ACK and WIN
		- To prevent deadlock if window announcement lost
#### Window Management Diagram
![[Pasted image 20251030151729.png]]
### Checksum (16 Bits)
- Checksum of the entire TCP segment plus a pseudoheader
- The pseudoheader includes TX IP, RX IP, Protocol (TCP=6), and TCP segment length
- Hashing this pseudoheader alongside the segment protects against misdelivery by IP
- If IP delivers a packet to the wrong host, this error can be recognized by the RX through the checksum
### Urgent Pointer (16 bits)
- Urgent pointer + sequence # = sequence # of the last byte in a sequence of urgent data
- Indicates the first UP bytes of the message are urgent
### Options (variable)
- A potential way to use this field is to allow each host to specify the max TCP payload it is willing to accept
# TCP Mechanisms
## Connection Establishment
- All TCP connections are full-duplex and point-to-point
	- Each connection has two end points. TCP does not support multicasting or broadcasting
- Three-way handshake
- Uniquely determined by tx and rx (host, port)
- One port can connect to multiple destination ports
## Data Transfer
- Bytes are numbered modulo $2^{32}$
- Data buffered at tx and rx
	- Each entity decides when to construct a segment for tx and when to release data to the application
## Connection Termination
- Graceful close
- Transport entity sets FIN flag on last segment sent
# TCP Implementation Policy Options
## Send
- Data buffered at tx buffer
- TCP entity transmits at its own convenience
- May construct segment per data batch
- May wait for a certain amount of data
## Deliver
- In absence of push, deliver data to application at own convenience
- May deliver as each in order segment received
- May buffer data from more than one segment
## Accept
- Segments may arrive out of order
- In order option
	- Only accept segments in order
	- Discard out of order segments
	- Most TCP implementations use this scheme
- In window option
	- Accept all segments within the receive window
	- More complex data storage scheme
	- 
## Retransmission
- TCP maintains a queue of segments tx'd but not ack'd
- TCP retx's if not ACK'd in a given time
### First Only:
- Same timer for all segments in a queue
- If timer expires, retransmit the first segment in the queue and reset the timer
- If ACK is received, remove the appropriate segment in the queue and reset the timer
### Batch
- Same timer for all segments in the queue
- Retransmit all segments in the queue if timer expires
### Individual
- Timer for each segment
## Acknowledge
- Immediate
- Cumulative: typically used
- Piggyback ACK in an outbound segment with data


For class #data-comm
