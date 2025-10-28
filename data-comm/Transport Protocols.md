# Transport Protocol Overview
- Provides **end-to-end** data transfer service
- Can either be connection-oriented (TCP) or connectionless (UDP)
- Features
	- Addressing
	- Connection establishment
	- Connection release
	- Flow control and buffering
	- Multiplexing
## Transport Vs Data Link Protocols

| **Data Link**                                                      | **Transport**                                                                                        |
| ------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------- |
| Two routers communicate directly via a physical channel            | Channel is an abstraction of an entire subnet                                                        |
| No need to specify endpoint receiver address                       | Explicit dest addressing is required                                                                 |
| Establishing a connection is simple, the other end is always there | Connection establishment is complicated. Large and variable delays complicate flow and error control |
# Addressing
- Target user specified by (host, port)
- Called a socket in TCP
- Host: An attached network device
	- In internet: global IP
- Port represents a particular transport service
	- Each application assigned a unique ID
	- Port 80: web service
- Port is included in transport header
# Connection Establishment
- By mutual agreement
	- Triggers allocation of transport entity resources
- Three-Way Handshake
![[Pasted image 20251028152152.png]]

1. Client host sends TCP SYN segment to server (SYN=1)
	1. Randomly choose client-side initial sequence number (ISN)
	2. No application data
	3. Segment encapsulated within IP datagram and sent to server host
2. Server host receives SYN, replies with SYNACK (SYN=1)
	1. Server allocates buffers
	2. ACK client ISN (acknowledgement field is client_isn+1)
	3. Choose server-side ISN
	4. No application data
3. Client receives SYNACK, replies with ACK segment (SYN=0)
	1. Client allocates buffers
	2. ACK server ISN (put server_isn+1 in ack field)
	3. May contain data
	4. Data sequence # = client_isn+1
- Connection establishment is achieved with 3 packets
	- The Three-way handshake
- 
## Why Not 2-Way Handshake
- The key reason is that the setup phase establishes a two-way link between client and server
### Obsolete segment: 
![[Pasted image 20251028152217.png]]

## Effect of unreliable network service:
- Complications arise when network loses, delays, damages, or duplicates packets
- Solutions can be designed, but solutions can create other problems
- Problem: lost packets; Solution: ACK
- What to do if ACK not received?
	- Retransmit timer
	- If time too large, slow connection.
	- If time too small, many retransmissions
	- Use adaptive timer based on RTT (received transmission time)
- Problems with adaptive timer:
	- Network conditions may change
- Problems with duplicates
	- Use segment sequence numbers
		- Each sequence belongs to a segment
	- May still have problems
		- Case 1: Duplicate is received before the connection is closed
		- Caused by a SN space short
		- Case 2: Duplicate received after connection closed
# Connection Termination
- Mutually agreement, can be initiated by either side
- Abrupt termination (Asymmetric release)
	- Telephone network: One party hangs up
	- May result in data loss
- Graceful termination (symmetric release)
	- Treat connection as two separate unidirectional connections and release each independently
1. Client sends TCP FIN segment (FIN=1)
2. Server receives FIN, replies with ACK, sends FIN
3. Client receives FIN, replies with ACK
	1. Enters timed wait; waits for all segments before FIN seq number
4. Server receives ACK, connection closed
5. Timed wait for outstanding packets
6. Associate sequence number with FIN
![[Pasted image 20251028154206.png]]

For class #data-comm