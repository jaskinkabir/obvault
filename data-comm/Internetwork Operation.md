Continues [[IPv6]]
# Multicasting
- Send a packet from 1 source to many destinations
- IP supports multicast using class D addresses:
	- First octet > 224 (0b1110xxxx)
	- $2^{28}$ available group addresses
	- Best-effort attempt to deliver to all members
	- Permanent group addresses are always there
		- All systems on a LAN: 224.0.0.1
		- All routers on a LAN: 224.0.0.2
		- All OSPF routers on a LAN: 224.0.0.5
	- Temporary group addresses:
		- Must be created before use
		- Members can join and leave
		- When the last host leaves, group no longer exists
## Requirements for IP Multiclassing
- Need to identify MC address (Class D)
- Translate between IP address and list of networks containing group members
	- Router must translate between IP multicast address and MAC-level multicast addresses
- Routers may forward more than one copy of the packet
- A mechanism is required for hosts to join and leave multicast groups
- Routers must exchange information
	- Which networks include members of the given group
	- Sufficient information to work out the least-cost path to each network
	- Routing algorithm to calculate the least-cost path to each network
- Routing algorithm to calculate the least-cost path to all group members
## Multicast Routing
- Implemented by special multicast routers: a router that has the above capabilities
- Using spanning tree
	- Multicast routers exchange info with neighbors
	- Constructs a spanning tree per group covering all group members
## IGMP (Internet Group Management Protocol)
- Used by hosts and routers to exchange multicast group membership info
- Messages transmitted in IP datagrams
- Operations
	- Hosts send messages to routers to sub/unsub to a multicast group
		- Group defined by multicast addr
	- Routers check which multicast group of interest to which hosts
- Group membership with IPv6
	- IGMP defined for IPv4 with 32-bit addr
	- For IPv6, IGMP functions are included in ICMPv6
	- ICMPv6 combines ICMPv4 & IGMP


For class #data-comm