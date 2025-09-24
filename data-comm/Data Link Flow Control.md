Continues [[TCP-IP Protocol Architecture]]
Continued by [[Data Link Error Control ARQs]]
Chapter 7.1
# Flow Control
- A technique for assuring that a transmitting entity does not overwhelm a receiving entity with data.
- The receiving entity typically has an allocated data buffer of some maximum length for transfer. When the data is received, the receiver must process this data and hand it off to a higher protocol layer before it is ready to receive more data.
- It is the job of the flow control system to make sure that the receiver's buffer does not fill up and overflow while it is still processing old data
## Timing terms
- **Transmission Time:** Time it takes for a transmitter to emit all bits of a frame onto the transmission medium
- **Propagation Time**: Time it takes for a bit to traverse the link between TX and RX stations
## Discussion Conditions
- For this examination of flow control, we will assume that all bits transmitted by the TX station are received by the RX without error.
- In the timing diagrams, time flows from top to bottom, and each arrow represents a single frame transiting a data link between two stations.
- Each frame is a portion of the full data packet with control info
- Frames arrive in the order in which they are sent
- However, each transmitted frame suffers an arbitrary and variable amount of delay before each reception
# Flow Control Methods
## Stop and Wait
- ### Procedure
	- TX transmits frame
	- RX receives the frame and sends an acknowledgement that the frame has been received to the TX
	- TX waits until it receives the acknowledgement and then sends another frame
	- RX can stop flow by witholding acknowledgement 
- ### Notes
	- This works well and can hardly be improved when the message is sent in few large frames
	- But in the common case the TX breaks up the message into many small frames because:
		- The RX buffer size may be limited
		- The longer the transmitted frame, the more likely there will be an error that requires retransmission
			- A shorter frame has less probability of error, and retransmission takes less time
		- On a shared medium, such as LAN, one station shouldn't occupy the medium for an extended period. This would cause delays for other stations on the same medium
	- In this case, stop and wait may be inadequate. The essence of the problem is that only one frame can be transmitted at a time
### Link Bit Length  
- First we must define a term known as$$B=R\times \frac{d}{V}$$
	- $B=$ length of the link in bits; the number of bits present on the link at an instance in time when a stream fully occupies the link
	- $R=$ data rate in bps
	- $d=$ length, or distance of the link in meters
	- $V=$ velocity of propagation in $m/s$
	- If you multiply out the units, you get $\frac{bits}{second}\times \frac{meters}{\frac{meters}{second}}$ or $\frac{bits}{second} \times \frac{meters\times seconds}{meters}=bits$
		- In other words, this equation finds the base propagation delay across the link by dividing the distance by the speed, and then multiplies this time by the data rate to just get max bits present on the channel
### Propagation Delay vs. Transmission Time
- In situations where the bit length is greater than the frame length, serious inefficiencies result.
- In the following figure, the transmission time is normalized to 1 and the propagation time is expressed as the variable $a$ where $$a=\frac{B}{L}$$
	- $L$ is the number of bits in a frame 
	- This variable $a$ is a ratio of the max number of bits allowed on the link to the number of bits in a frame. The larger this number, the longer it takes for a frame to pass through the channel.
		- Think of a shift register that is larger than the message you need to shift into it. The zeros at the end of the register have to be passed through
	- When $a<1$, the propagation time is less than the transmission time. This means that the RX station receives the first bits of the frame before the TX station is done emitting the frame
	- When $a>1$, the propagation time is greater than the transmission time. In this case, the sender emits the whole frame before the leading bits of that frame arrive. 
		- Larger values of $a$ are associated with higher data rates and/or longer distances between stations
- ![[Pasted image 20240804164035.png]]
	- #### Inefficient Utilization $\large a<1$
		- 1. at $t_{0}$, the first bits of the frame are transmitted
		- 2. at $t_{0}+a$, the RX station already receives these first bits
		- 3. at $t_{0}+1$ the TX station has sent the last bits of the frame
		- 4. at $t_{0}+1+a$ the RX station has received the full frame
		- 5. at $t_{0}+1+2a$ the TX station has received the acknowledgement
	- #### Underutilization $\large a>1$
		- 1. at $t_{0}$, the first bits of the frame are transmitted
		- 2. at $t_{0}+1$, the last bits of the frame are transmitted
		- 3. at $t_{0}+a$ the first bits of the frame are finally received
		- 4. at $t_{0}+1+a$, the frame is fully received
		- 5. at $t_{0}+1+2a$ the TX station receives acknowledgement
	- The time between each frame's transmission is $t_{0}+1+2a$
		- This means that a very small $a$ results in the fastest data rate
		- However, this would require the frame to be much longer than the data link
		- If there are errors, the very large frame would then have to be resent across the very short data link. This is not ideal
	- When $a<1$ the link is inefficiently utilized;
		- This is because of the waiting time required by acknowledgement
	- When $a>1$ the link is underutilized; there could be more data being sent at a time
		- In this case, the frame is smaller than the link. In high-speed long-distance networks, the propagation delay becomes significant. 
		- If the frame is shorter than the link, multiple frames can be sent at a time before the TX station receives the acknowledgement for the first frame. 
	- #### "larger values of a are consistent with higher data rates and/or longer distances"
		- This is because higher data rates increase $B$. More bits can be in flight at once
		- Longer distances increases $B$ as well. More distance means a longer channel for bits to occupy (increased propagation delay)
		- Typically $a>1$ doesn't mean choosing smaller frames. It means network conditions have increased $B$ to the point that it exceeds $L$
## Sliding Window Flow Control
### Overview of Operation
- Two stations A, and B, are connected via a full-duplex link.
- Station B allocates buffer space for W frames and can accept W frames. A is allowed to send W frames without waiting for acknowledgement.
- Each frame is labeled with a sequence number. B acknowledges a frame by sending an acknowledgement that includes the frame it expects to receive next. 
	- This allows for implicit acknowledgement that B is ready to receive the next W frames, beginning with the number specified
	- This also allows for acknowledgement of multiple frames. If B receives frames 1,2,3,4 but withholds acknowledgement until frame 4, it can send an acknowledgement specifying frame 5 as its next frame. In doing so, it has acknowledged that it has received frames 1,2,3,4
- A maintains a list of frames it is allowed to send, and B maintains a list of frames it is prepared to receive. Each of these lists can be thought of as a window of frames.
### Window Size
- Since the sequence number occupies a field in the frame, it must be limited to a range of values.
- For a $k$-bit field, the range of sequence numbers can range from $0\to{2}^{k}-1$
	- The sequence numbers are modulo $2^{k}$
		- If $k=3$, the frame that follows frame 7 is frame 0
- The maximum window size is $2^{k}-1$
	- This is because of error control
### Simplex Window Mechanism
- The following diagram uses $k=3$
- ![[Pasted image 20240804171926.png]]
	- From the sender's side:
		- The shaded rectangle indicates that the sender is allowed to transmit 5 frames from 0-4
		- Each time a frame is sent, the window shrinks
			- If frame 0 was sent, the window should move its left edge to frame 1
		- Each time an acknowledgement is received, the window expands
			- If frame 4 was acknowledged, the window should move its right edge to frame 5
		- The frames between the vertical line and the shaded window are frames that have been transmitted but not acknowledged
			- These frames must be buffered by the TX in case they must be retransmitted
	- This can be demonstrated in the following diagram
	- ![[Pasted image 20240804173109.png]]
- Most data link protocols allow the receiver to stop the flow of frames by sending a Receive Not Ready (RNR) message, which acknowledges former frames but forbids transfer of future frames
	- The receiver must send a normal acknowledgement to reopen the window
### Full Duplex Window Mechanism
- If two stations are to send and receive data, each station must maintain two windows: one for TX and one for RX
	- Each side needs to send acknowledgements to the other
- This can be supported by a feature known as **Piggybacking**
	- Each **data frame** includes a field that holds the sequence number of that frame plus a field that holds the sequence number used for acknowledgement
- Thus, if a station has data and an acknowledgement of received data to send, it can send both in the same frame.
-  If a station has an ack but no data to send, it can send an **Acknowledgement Frame** such as RR or RNR
- If a station has data but no acknowledgement, it must repeat the last acknowledgement sequence number it sent. When a station receives a duplicate ack number, it is ignored.


For class #data-comm