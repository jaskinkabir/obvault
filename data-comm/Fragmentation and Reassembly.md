Continues [[Protocol Architecture]]
# IP Fragmentation
- IP re-assembles at the destination only
- Uses fields in the header
	- Data unit Identifier
		- Source and dest addresses
	- Data length
		- Length of user data in octets
	- Offset
		- Position of user data in original datagram
		- In multiples of 64 bits, except the last fragment which holds the <64 bit remainder
	- More flag
		- Indicates this is not the last fragment
## Steps
1. Create two new datagrams, and copy the header fields into both
2. Divide the data into two approximately equal portions along a 64-bit boundary
	1. The first portion must be a multiple of 64 bits
		1. 8 bits is also ok
	2. 
3. Figure out the offset and more flag bits
	1. The second datagram's offset value is calculated as follows
		1. Divide the length of the first fragment by 8
	2. 1st datagram: has more = 1, offset = 0
	3. 2nd datagram has more=0, offset = len(1)/8
## Dealing With Failure
- Reassembly may fail if some fragments are lost
	- Need to decide when to give up finishing re-assembly
- Method:
	- Assign reassembly lifetime to first fragment to arrive
	- If timeout expires, discard all partial data

# Error Control
- Delivery is not guaranteed
- Router should attempt to inform source if packet discarded
- Datagram identification needed
# Flow Control
- Allows routers and/or stations to limit rate of incoming data
- Send flow control packets requesting reduced flow
- eg  ICMP (Internet Control Message Protocol)
	- Source quench message

For class #data-comm 