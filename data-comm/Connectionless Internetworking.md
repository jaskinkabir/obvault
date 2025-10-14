Continues [[Protocol Architecture]]

This page discusses layer 3 (network)
# Connectionless Internetworking
- Unreliable
	- Not guaranteed delivery
		- The network layer does its best effort
	- Not guaranteed order of delivery
		- Packets take different routes
- Reliability is the responsibility of the next layer up (ie TCP)
# Routing
- Routers maintain routing tables
	- Indicate next router to which the datagram should be sent
	- Static: May contain alternative routes
	- Dynamic: Flexible response to congestion and errors
- Source routing
	- Source specifies route as sequential list of routers to be followed
	- Used for security (military)
	- Routers ignore their own routing logic
- Route recording
	- To record a route, each router appends its ip to a list of addresses in the header of the datagram
	- This is useful for debugging
# Datagram Lifetime
- Datagrams could loop indefinitely and waste resources
- Datagrams are thus marked with lifetime
	- Once the lifetime expires, datagram is discarded
	- This is usually done through hop count
- 
For class #data-comm