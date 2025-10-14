# The IPv4 Header
![[Pasted image 20250930153320.png]]
- The minimum length of the header is 20 bytes
## Header Fields
- Protocol version(4 bits): Currently 4
- Internet header length (IHL)(4 bits): in 32-bit words
	- Minimum of 5
- DS (6 bits): Supports differentiated service function
	- Different types of traffic are given different treatment
	- This field indicates which type of traffic is within the packet
- ECN (2 bits): Explicit Congestion Notification
	- Enables routers to indicate to end nodes that packets are experiencing congestion
	- 00: Not using ECN
	- 01 or 10: Set by sender, indicate ECN capable
	- 11: Set by router, indicate congestion has been encountered
- Total length (16 bits) in bytes (header + data)
	- Can be used to find length of data
	- Data (bytes) = total length - IHL * 4
- Identification (16 bits*: Sequence number
- Flags (3 bits): Only 2 bits are currently defined
	- More bit
	- Don't fragment
		- If set, datagram discarded if exceeds max size

- Fragmentation offset (13 bits): In 64-bit units
- Time to live (8 bits): Similar to hop count
	- Every router will decrement TTL before retransmitting
	- Any packet with TTL=0 will be discarded by a router
- Protocol (8 bits): Next higher layer to receive data field at destination
	- TCP = 6
	- UDP = 17