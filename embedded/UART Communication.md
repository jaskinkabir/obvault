# Uart 

# BAUD Rate
- Speed in signals (bits) per second
- Baud rates can be any value, so long as both devices agree on this value
# Framing
- Each block (usually a byte) of data transmitted is sent in a packet, or frame of bits
	- Can be 5-9 bits in length
	- ASCII is 7 bits, so transmitting ASCII chars is more efficient with chunk size set to 7
- Frames are created by appending synchronization and parity bits to our data
- Data is usually transmitted LSB first
- ![[Pasted image 20251014162648.png]]
# Synchronization Bits
- The synchronization bits are two or three special bits transferred with each chunk of data
	- Start and stop bits
- The line is usually held high. The line being pulled low means data transmission has begun
- The stop bit will then bring the line back high
# Parity Bits
- Parity is optional
- To produce the bit, all 5-9 bits are added up and the evenness of the sum decides whether the bit is set or not
- It is not very wisely used
	- It can be helpful for transmitting across noisy mediums
	- But slows down transfer and requires both TX and RX to implement error-handling
- Only detects odd number of bit errors
# Naming Convention
- (Baud)(Chunk len)(Parity)(Stop bits) 
- 9600 8N1
	- 9600 Bps
	- 8 bits per chunk
	- No parity
	- 1 stop bit
	- ![[Pasted image 20251014163422.png]]
# F901RC USART Registers
## Baud Rate Register BRR
- Defines baud rate according to
- $$\text{BRR}=\frac{f_{CLK}}{\text{Baud Rate}}$$
- $$f_{CLK}=8\text{ MHz},\,\text{Baud }=9600 \implies \text{BRR} \approx 833$$
- ![[Pasted image 20251014163617.png]]
## Control Register 1 CR1
- Enable transmitter
- Enable Receiver
- Enable peripheral
- Enable receive interrupt
- Set word length
- PCE (parity control)
## Control Register 2 CR2
- Stop bit selection
- Other fields are used for synchronous mode or clock settings
## Interrupt and Status Register ISR
- Transmit data register empty
- Receive data register not empty
- TC Transmission Complete
## Data Registers
- TDR, transmit data
- RDR read data
- Both registers are 8 bits wide
