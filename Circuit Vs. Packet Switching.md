Continues [[Packet Switching Networks]]
Chapter 9.5
# Performance and Timing
- Consider the following diagram
- ![[Pasted image 20240806225554.png]]
- There are three types of delay shown in this figure
	- **Propagation delay:**
		- Time it takes for a signal to travel between nodes
		- This time is typically negligible. The speed of an EM signal through a wire for example is typically 200 million meters per second
	- **Transmission Time**:
		- Time it takes for a transmitter to send out a block of data
		- Takes 1s to transmit a 10Kb block of data across a 10-Kbps line
	- **Node Delay:**
		- The time it takes for a node to perform the necessary processing as it switches data
## Circuit Switching
- First, a call request is sent through the network
	- Processing (node) delay is incurred at each node during the call request, as each node has to decide how to connect the call
	- On the return, this is not needed because the circuit has already been established
- Once the call accepted signal signifies that the destination is not busy and a valid path was formed, the user data is sent as a single block with no noticeable node delay
## Virtual Circuit Packet Switching
- A virtual circuit is requested using a Call request packet, which incurs delay at each node.
- The virtual circuit is accepted with a Call Accept packet.
	- Unlike physical circuit switching, the call accept packet and all subsequent traffic experiences node delay.
	- This is because the packets must be queued at each node and wait their turn for transmission
		- Though, this node delay should be shorter because of the lack of routing being done at each node
- Virtual circuit switching can be no faster than physical circuit switching because circuit switching is essentially a transparent process, providing a constant data rate across the network
	- There will be delay at each node because of buffering and queuing
	- This delay is variable and will increase during times of high load
## Datagram Packet Switching
- This technique requires no call setup
- Thus, for short messages, it is faster than virtual packet switching and sometimes physical circuit switching
- However, because each datagram is routed independently, the node delay might be longer due to the routing computations
# Other Characteristics
## Table
![[Pasted image 20240806231031.png]]
For class #data-comm