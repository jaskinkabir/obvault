[[I2C]]
[[UART Communication]]
[[SPI]]
[[CAN Bus]]
# The OSI Layer
## Physical
- Defines how bits are transmitted over a physical medium
- Concerned with voltages, timing, connectors, signal integrity
- Examples:
	- UART TX/RX pins
	- SPI SCK, MOSI, MISO lines
	- I2C SDA/SCL lines
- Key tasks
	- Bit-level synch
	- Line coding and voltage levels
	- Physical connection setup
## Data Link
- Defines how frames are structured and managed on the link
- Adds framing, error detection, and adressing mechanisms
- Examples
	- UART start/stop bits and parity
	- SPI and I2C manage addressing and framing
	- CAN uses frame IDs and CRC
- Key tasks
	- Framing and Synchronization
	- Error detection
	- Flow control and (bus) arbitration 
		- MAC
### Network
- Manages addressing and routing of data between different networks or nodes
- Adds logical addressing independent of the physical link
- Addressing in I2C is different:
	- Data Link layer handles node-node comms across a common physical bus
	- I2C uses 7 or 10 bit addresses to distinguish devices on that bus
# Serial Protocols Are Not Enough!
- A serial interface only describes transferring one byte
- A higher level protocol is needed for more advanced features
	- Larger transfers
	- Multiple data types
	- Error correction/recovery
	- Reliable communication
## Communication Example
- Let's say 1 mcu needs to send a 4 byte float and a 1 byte int to another mcu
- The naive approach is to send bytes in a specific order and expect the rx to read in this order:
	- ![[Pasted image 20251023164025.png]]
- However, if the rx boots up slightly later than the tx, the tx will have already sent 2 bytes before the rx starts reading
- RX will see:
	- ![[Pasted image 20251023164126.png]]
	- It will interpret this data incorrectly and use garbage for its program
# Need For Framing
- Instead, designate a byte 0xFE as a start byte
- ![[Pasted image 20251023164220.png]]
- Now the RX will only start reading and interpreting bytes in order once it receives 0xFE
# Need For a Checksum
- Let's say a higher priority interrupt occurs while the last byte of the frame is transmitted
- The RX will miss the last byte and the start byte for the next message will be interpreted as humidity
- To solve this, add a checksum
- A simple checksum can be created by summing all data bytes and send the least significant byte alongside the data
- The receiver can then read the final (checksum) byte, compute its own sum of the data, and compare to the checksum
# Need for Headers
- What if we want to send data one at a time
- Data must be interpreted in different ways, need to know how many bytes are being sent
- Can add a byte for data type 
	- 0x01 for temp data
	- x02 for humidity data
- Can add two bytes for ddata length
	- Send MSB first
	- Only data length, not header or checksum length
- ![[Pasted image 20251023165707.png]]
# Buffering Data
- The length component of the frame allows efficient parsing from a bufferr
## Buffering via ISR
- Once the RX ISR fires, add data into a buffer and increment a global buffer index
- Somewhere in the main loop, the buffer can be parsed
- 
For class #embedded