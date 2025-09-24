Continues [[LAN and WAN]]
Continued by [[TCP-IP Protocol Architecture]]
Continued by [[Standardization Within a Protocol Architecture]]
## Protocol
- Defined as a set of rules or conventions that allow peer layers to communicate (A common language)
- For example: The tasks that must be performed to transfer a file between two PCs
	- Source must either activate direct data comm path or inform the comm network of the destination's identity
	- It must then ascertain that the destination is prepared to receive the data
	- The file transfer application on the source system must ascertain that the file management system on the destination is prepared to accept and store the file
	- If the file formats are different, one system must perform a format translation
- Protocols define network characteristics
	- Access method
	- Allowed physical topologies
		- Mesh, Star, Ring, etc
	- Types of cabling
	- Speed of data transfer
	- Data format
- All nodes in the network must obey the protocol
## Protocol Architecture
## Layered structure
- Networking protocols are broken up into layers:
	- Starting with the physical medium of transportation, working up in abstraction to the application layer or even higher (presentation)
	- Most broad layers are network access, transport, application
- Network Access layers:
	- Concerned with the exchange of data between the computer and its network
- Transport layers:
	- Converts application layer's data into the format necessary for transport across the network
- Application layers:
	- Concerned with interpreting the data received from the network access layer into a usable format
	- Each application has a unique address within the computer, so the transport layer can support multiple applications
		- Ex: port 25565 for Minecraft
## Data Encapulation
- Data needs to be encapsulated with control info at each layer
	- ![[Pasted image 20240704161212.png]]
- Protocol Data Unit
	- A PDU contains user data + control information from the next higher layer
	- Has different names depending on the layer
	- **Data Link:** Frame
	- **Network:** Packet
	- **Transport:** Segment
	- Segment goes in a packet which goes into a frame
		- The lowest layer has the longest messages
	- ![[Pasted image 20240704161439.png]]
		-  FCS: Frame Check Sequence (error detection code)

For class #data-comm 
