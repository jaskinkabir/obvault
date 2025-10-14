Continues [[TCP-IP Protocol Architecture]]
# Address Resolution Protocol (ARP)
- Need mapping from an IP address to subnetwork address or MAC address
- The address resolution protocol comes in here
	- Provides dynamic IP to ethernet address mapping
	- Each system in the LAN maintains a table of known IP to MAC address conversions
	- When needed, system uses ARP on LAN to find MAC adddress
	- Source broadcasts ARP request
	- Destination replies with ARP response

For class #data-comm