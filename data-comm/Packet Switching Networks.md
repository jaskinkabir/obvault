Chapter 9.5
Continues [[Circuit Switching Networks]]
Continues [[Circuit Switching Under the Hood]]

Continued by [[Circuit Vs. Packet Switching]]

**PACKET SWITCHING OCCURS AT THE INTERNET LEVEL**
# The Need For Packet Switching
- The long-haul circuit switching network was originally designed to handle voice traffic, and the majority of traffic still continues to be voice
- A key characteristic of circuit switching networks is that resources within the network are dedicated to a particular call or connection
- For voice connections, the resulting circuit will enjoy a high percentage of utilization because someone is pretty much always talking during a phone call
- However, as the circuit-switching network began to be used for data connections, two problems became apparent
	- In a typical server/client data connection, much of the time the line is idle. Thus, a circuit-switching approach is inefficient
	- In a circuit switching network, the connection provides for transmission at a constant data rate. 
		- Thus, each of the two devices must transmit and receive at the same rate as the other
		- This can limit the utility of the network in interconnecting a variety of servers and clients using different hardware configurations
# Summary of Packet Switching Operation
- Data is transmitted in short packets
	- A typical upper bound on packet length is 1000 octets
- If the source has a longer message to send than the max packet length, the message is broken up into a series of packets
- Each packet contains a portion of the user's data plus some control information
	- The control info, at a minimum, contains the information the network requires to be able to route the packet through the network and deliver it to the intended destination
- At each node en route, the packet is received, stored briefly, processed, and passed on to the next node
- Consider the scenario where station A needs to send a packet to station E
	- The packet includes control info that indicates the destination is E
	- The packet is sent from A to node 4
	- Node 4 stores the packet, processes the control information,  determines the next leg of the route to be node 5, and queues the packet to go out on the 4-5 link
	- When the link is available, the packet is transmitted to node 5, which transmits to node 6, and finally to E
# Pros and Cons of Circuit Vs. Packet Switching
- The packet switching approach has a number of advantages over circuit switching
	- **Line efficiency is greater**
		- A single node-to-node link can be dynamically shared by many packets (each representing a top level, station-to-station, channel) over time. 
		- The packets are queued up and transmitted as rapidly as possible over the link
		- By contrast, with circuit switching, time on a node-to-node link is preallocated using TDM.
			- Much of the time, such a link may be idle because a portion of its time is dedicated to an idle connection
	- **A packet-switching network can perform data-rate conversion**
		- Two stations of different data rates can exchange packets because each connects to its node at its proper data rate
	- **Packet-Switching is Non-Blocking**
		- When traffic becomes heavy on a circuit-switching network, some calls are blocked until the load decreases
		- On a packet-switching network, packets are still accepted but delivery delay increases
	- **Priorities can be used**
		- If a node has a number of packets queued for transmission, it can transmit higher-priority packets first
# Switching Technique
- If a station has a message that is larger than the maximum packet size, it breaks the message up into packets and sends these packets one at a time across the network
	- How will the network handle this stream of packets?
	- Two approaches are used: datagram and virtual circuit
## Datagram
- Each packet is treated independently, with no reference to packets that have gone before.
- Each node chooses the next node on a packet's path, taking into account information received from neighboring nodes about traffic, line failures and so on.
	- Thus, the packets that make up a message being sent from one station to another may not all take the same path and may arrive out of sequence at the RX side
	- Either the exit node or the destination station will have to reorder the packet
- It is also possible for a packet to be lost/destroyed in the network
	- For example, if a node crashes momentarily, all of its queued packets may be lost.
	- Again, it is up to either the exit node or the destination to detect packet loss and decide how to recover it
- In this technique, each packet is treated independently and referred to as a datagram
## Virtual Circuit
- A preplanned route is established before any packets are sent.
- Once this route is established, all packets between a pair of stations follow this same route through the network
- Each packet must contain a virtual circuit identifier as well as data
	- VCI is scoped to each switching station, not globally
	- Each node needs a VCI to represent the incoming connection and outgoing connection
	- 
- Each node on the preestablished route knows where to direct such packets, and no routing decisions are required
- While the route between stations is set up before data transfer, this is not a dedicated path as in circuit switching
	- A transmitted packet is buffered for transmission at each node and queued for transmission for output over a line, while other packets may share the use of this line.
- The difference from the datagram approach is that the nodes don't need to make routing decisions for each packet.
## Datagram Vs. Virtual Circuit
- If two stations wish to communicate over an extended period of time, there are certain **advantages to virtual circuits:**
	- The network may provide services related to the virtual circuit:
		- Sequencing: all packets follow the same route and arrive in the same order
		- Error control assures that all packets arrive correctly as well as in order
	- Packets will be sent more rapidly, since the intermediate nodes don't need to make routing decisions\
		- There is also no sequencing logic required
- **Advantages of the datagram approach are:** 
	- The call setup phase is avoided.
		- If a station only wishes to send one or a few packets, datagram delivery will be quicker.
	- Because it is more primitive, it is more flexible.
		- If congestion develops in one part of the network, datagrams can be routed away from the congestion.
		- Virtual circuits use predetermined routes and are therefore more difficult to adapt to congestion
	- Datagram delivery is inherently more reliable
		- In the use of virtual circuits, if a node fails, all virtual circuits that pass through that node are lost and so are their packets
		- With datagram delivery, node failure can be dealt with by routing subsequent packets across routes that bypass that failed node
# Packet Size and Octet Time
- ![[Pasted image 20240806220840.png]]
	- There is a significant relationship between packet size and transmission time, as shown in the example above
	- In this example, it is assumed that there is a virtual circuit between stations X and Y through nodes a and b
	- The message comprises 40 octets, and each packet contains 3 octets of control information.
	- If the entire message is sent as a single packet of 43 octets:
		- The packet is first transmitted from X to a
		- When the entire packet is received, it can then be transmitted to b
		- Then b must receive the entire packet before it can be passed off to Y
		- The total transmission time is 129 octet-times
	- However, if the message is broken up into two 23 octet packets:
		- Node a can begin transmitting the first packet as soon as it arrives from X, without waiting for the second packet (and therefore the full message)
		- Because of this overlap in transmission, the total transmission time drops to 92 octet times
			- Count the height of the stack from $b \to Y$ up to $X \to A$ and multiply by packet size
			- $4 \times 23 = 92$
	- If the message is broken up into 5 packets:
		- Each intermediate node can begin transmission even sooner and the transmission time drops to 77 octet-times
		- $7 \text{ layers } \times 11 \text{ octets per packet } = 77$
	- However, if the message is broken up into 10 packets:
		- $12 \times 7 = 84$ octet-times
		- The performance is actually decreased because each packet contains a fixed amount of header, and more packets mean more headers.
	- The octet time is given by this equation $$T=(N_{p}+N_{i}) \times \left(\lceil \frac{L}{N_{p}}\,\rceil+H\right)$$
		- Where
			-  $T$ is the octet time
			- $N_{p}$ is the number of packets the message is split across
			- $N_{i}$ is the number of intermediary nodes
			- $L$ is the total messsage length
			- $H$ is the header length
		- $N_{p}+N_{i}$ is the number of layers
		- $\lceil \frac{L}{N_{p}}\rceil + H$ is the packet size
		- ![[Pasted image 20240806224443.png]]
			- For a 40 octet message, 3 octet header, two intermediary nodes
			 
# External Network Interface
- In circuit switching, the network provides a transparent communications path for attached devices
- However, packet switching network require the attached stations to organize their data into packets for transmission
	- This requires a level of cooperation between the network and the attached stations
- This cooperation is embodied in an interface standard.
- The standard used for traditional packet-switching networks is **X.25**
	- Another standard is frame relay
- These standards typically define a virtual circuit service

![[Pasted image 20240806224948.png]]
- This service allows any subscriber to set up logical connections, called virtual circuits, to other subscribers
	- This is best termed as an **External Virtual Circuit**
	- The specific preplanned routes through the network should then be called **Internal Virtual Circuits** 
- Typically, there is a one-to-one relationship between external and internal virtual circuits. However, it is possible to employ an external virtual circuit service with a datagram-style newtork under the hood
- What is important for an external virtual circuit is that there is a logical channel established between two stations, and all of the data associated with that channel are considered as a single stream of data between the two stations
	- This is to make the network appear as transparent as possible



For class #data-comm