Continues [[Data Link Flow Control]].
Continued by [[Frequency Division Multiplexing (FDM)]].
Continued by [[Time Division Multiplexing (TDM)]].
Continued by [[Multiple Channel Access (DATA LINK MUX)]].
Continued by [[Circuit Switching Networks]].
Chapter 8.1
# Multiplexing
- This is a technique that is used **AT THE PHYSICAL LAYER**
- Flow control is a technique used to manage the over-utilization of a data link under heavy load
	- It is generally desirable to have multiple frames along the data link so that the data link does not become a bottleneck between stations
- Consider the opposite problem, two stations not utilizing the full capacity of a link
	- In this case, that capacity should be shared between different stations
	- This can be done using **Multiplexing**
- A common application of multiplexing is in long-haul communications.
	- Trunks on long-haul networks are high-capacity fiver, coaxial, or microwave links. These links carry large numbers of voice and data transmissions simultaneously using multiplexing.
- ![[Pasted image 20240804190238.png]]
- The techniques are as follows:
	- Frequency Division
	- Time Division
	- ![[Pasted image 20240804191046.png]]
## Usefulness
- The higher the data rate, the more cost-effective the transmission facility. Cost per kbps declines with an increase in data rate of the facility. Similarly, cost of TX and RX equipment, per kbps, declines with increasing data rate
	- Economies of scale
- Most devices that use, for example, a 10Gbps link do not need all 10 Gbps. They can get by with maybe 100Mbps.

For class #data-comm