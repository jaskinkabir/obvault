Jaskin Kabir 801186717
Uses [[Ethernet and MAC]]
1. Why medium access control (MAC) is not found in traditional layer 2 data link control, but defined for local area networks (LANs)? [4]
	1. **The Data Link layer does not need to account for multiple stations occupying the same medium. Only in cases where this problem occurs, like in LANs, is MAC required. To allow for more flexibility in the protocol standard, MAC is omitted from traditional layer 2 control.** 
2. In local area networks, [4+3+3=10]
	1. List four connecting devices which could be used for LANs? _[4]_
		1. **Bridge**
		2. **Repeater**
		3. **Hub**
		4. **Layer 2 Switch**
	2. How is a bridge different from a repeater? _[3]_
		1. **A repeater will simply perform a bitwise copy of all packets from one LAN onto the other, whereas a bridge reads MAC addresses and selectively repeats only the frames that need to be repeated onto the other LAN.**
	3. How is a bridge different from a router? _[3]_
		1. **A bridge connects LANs with similar topologies and uses identical protocols for the physical and data link layers. A router is more general purpose, however, and can interconnect various LANs and WANs with varying topologies and protocols.**
3. For layer-2 switches,
	1. What is the difference between store-and-forward switches and cut-through switches? _[3]_
		1. **Store and forward switches buffer frames until they are fully available to read in its local memory. Then it performs error detection and routes the frame to the appropriate destination. Cut through switches, however, take advantage of the fact that the destination address appears at the beginning of the frame, and simply perform a bitwise copy of the frame to the destination before receiving the full frame**
	2. Store-and-forward switches have an advantage over cut-through switches with respect to damaged frames. Explain why? _[3]_
		1. **Cut-through switches will transmit a frame as soon as it can read the destination address. It forgoes error detection, because the error detection bits are not available before the destination address. This means cut-through switches will transmit bad frames, whereas a store-and-forward switch will not.**
4. For 1-persistent CSMA/CD channel, during the transmission of a frame, two stations A and B arrive. Assume binary exponential backoff algorithm is used _[3+3=6]_
	1. What is the probability A and B will collide at their first attempt of transmission? _[3]_
		1. **Both A and B will attempt to transmit as soon as they sense the medium is idle. Thus, the probability they will collide is 1**
	2. What is the probability A and B will collide at their second attempt of transmission? _[3]_
		1. **After first collision, $k=1$**
		2. **Possible random backoff values = $\{ 0,\,1 \}$**
		3. **With 2 stations there are $2\times 2 = 4$ combinations**
		4. **There are 2 possible combinations that result in collision:** $\{\ (0,\,0),\,(1,\,1)\ \}$
		5. $P(\text{collision})=\frac{2}{4}=50\%$
5. Under heavy loads, how do the behavior of 1-persistent CSMA and _p_-persistent CSMA (0<_p_<1, and _p_ is very small) differ? _[4]_
	1. **Under heavy load, 1-persistent CSMA almost guarantees constant collision, as each station with data to transmit will attempt to transmit as soon as it detects the medium is idle. P-persistent csma, where p is very small, guarantees that $np<1$, which represents the number of stations that are expected to transmit when the medium is idle. Meaning that at any given time when the medium is idle, a maximum of one station is expected to transmit. This greatly reduces the chance of collisions, but results in a long delay between a station having data ready to transmit and that data actually being transmitted across the medium. This is because each station has a low probability that it will transmit data when it senses the medium is idle.**