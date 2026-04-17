[[CAN Bus]]
# CAN and OSI Model
- CAN only provides layers 1 and 2.
- No way to send messages over 8 bytes
- No standard for decoding the raw bytes
# CAN Extensions
## SAE J1939
- A set of standards to define how ECUs communicate in heavy duty vehicles like trucks and buses
### 4 Key Characteristics
- 250K baud rate and 29-bit extended ID
- Broadcast + on-request data
	- Most messages are broadcast, though some data is only available via request
- PGN identifiers and SPN parameters
	- Messages identified by 18-bit Parameter Group Numbers PGN
	- Signals are called Suspect Parameter Numbers SPN
- Multibyte variables and multipackets
	- Multibyte variables are sent least significant byte first
	- PGNs with up to 1785 bytes are supported
### PGNs and SPNs
- A PGN identifies a message type
- A SPN identifies a specific data element or sensor value within a PGN
- ![[Pasted image 20251202151245.png]]
#### The PGN
- The PGN is stored in bits 8-25 of the 29 bit CAN identifier
- It groups related parameters that are transmitted in a single CAN frame
- ![[Pasted image 20251202151426.png]]
#### The SPN
- Allows standardized interpretation of each piece of data
- ![[Pasted image 20251202151448.png]]
### Multi-Packets
- Two types of the transport protocol exist
	- Connection mode: point to point
	- BAM (broadcast announce message): Broadcast
#### BAM Example
- Send an initial BAM packet to set up tx
- Specifies PGN identifier for multi-packet message and data size
- Then sends up to 255 packets of data
	- First data byte is the sequence number
- Max number of bytes is 7 x 255 = 1785 bytes
- Final packet contains at least one byte of data, followed by unused bytes set to FF
### Standards
![[Pasted image 20251202151809.png]]

### Pros and Cons
- PROS
	- Standardized higher layer protocol
	- Predefined PGNs and SPNs make data interpretation uniform across manufacturers
	- Supports large data transfers
	- Widely supported
- CONS
	- High overhead
	- Lower throughput due to parameter broadcasts
	- More complex message management
	- suited for slow to medium update rate, not real time control
## OBD2
- On board diagnostics
- It is a higher level protocol implemented over the CAN bus's physical and data link protocols
### OBD2 Frame Details
![[Pasted image 20251202152101.png]]
#### Identifier
- Standard 11 bit ID used to distinguish between
	- Request (ID 7DF)
	- Response (ID 7E8 to 7EF)
- This is the CAN ID
#### Length
- Number of bytes of the remaining data
	- 03 to 06

For class #embedded 