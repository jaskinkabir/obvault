# Part 1
1. What is the IP address of the sending computer?
	1. **192.168.86.61**
2. What is the value in the time-to-live (TTL) field in this IPv4 datagram’s header?
	1. **1**
3. What is the value in the Protocol field in this IPv4 datagram’s header?
	1. **17 (UDP)**
4. How many bytes are in the IP header?
	1. **20**
5. How many bytes are in the payload of the IP datagram? Explain how you determined the number of payload bytes.
	1. Total length field is set to 56. 56-20=36; **Payload is 36 Bytes**
6. Has this IP datagram been fragmented? Explain how you determined whether the datagram has been fragmented.
	1. Fragment offset = 0, More flag = 0; **Datagram Has Not Been Fragmented**

# Part 2
1. Which fields in the IP datagram always change from one datagram to the next within this series of UDP segments sent by the sending computer destined to 128.119.245.12, via traceroute? Why? (List ALL the fields that change)
	1. Identification: Always incrementing to differentiate messages
	2. Header Checksum: Changes because header always changes
2. Which fields in this sequence of IP datagrams (containing UDP segments) stay constant? Why? (List ALL the fields that stay constant)
	1. IP source and dest addr: These don't change because we have filtered to find packets with these two values
	2. Protocol: Filtered to find only UDP
	3. IP version: Dest and src addrs are ipv4 addresses, and those have been filtered to stay the same
	4. Differentiated services: The source computer doesn't wish to send any ECN information
	5. 
3. Describe the pattern you see in the values in the Identification field of the IP datagrams being sent by the sending computer.

# Part 3
1. What is the value in the Protocol field specified in the IP datagrams returned from the routers?
2. Are the values in the Identification fields (across the sequence of all of ICMP packets from all of the routers) similar in behavior to your answer to Question 9 above?
3. Are the values of the TTL fields similar, across all of ICMP packets from all of the routers?


For class #data-comm/labs