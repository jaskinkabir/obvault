# Serial Peripheral Interface
- Synchronous, full-duplex protocol
- Master and slave share a clock
- MISO and MOSI 
	- (Master in slave out) (Master Out Slave In)
# Multiple Slaves
- MISO and MOSI can be on one pin each from the MCU
- Forms a BUS
- The Master selects which slave it wants to talk to by driving the slave select lines
- ![[Pasted image 20251016162419.png]]
# Pros and Cons
- +
	- Faster than asynchronous serial (UART)
	- Receive hardware can be a simple shift register
	- Supports many slaves
- -
	- Requires more signal lines than other comm methods
	- Comms must be well defined in advance
	- Master must control all comms
	- Usually requires SS lines to each slave


For class #embedded