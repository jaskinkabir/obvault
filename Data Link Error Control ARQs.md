Continues [[Data Link Flow Control]]
Chapter 7.2
# Terms
- ## Frame errors
	- **Lost frame:** A frame fails to arrive at the other side. In the case of a network, the network may simply fail to deliver the frame. In the case of a point-to-point link a noise burst may damage a frame to the extent that the receiver is not aware a frame has been transmitted
	- **Damaged Frame:** A recognizable frame arrives, but some bits are in error
- ## Error Control Ingredients
	- **Error Detection:** Discard frames in which errors are detected
	- **Positive Acknowledgement:** The destination returns a positive acknowledgement to successfully received, error-free frames
	- **Retransmission after timeout**: If a frame does not receive acknowledgement after a set amount of time, the frame is retransmitted
	- **Negative Acknowledgement and Retransmission:** The destination returns a negative acknowledgement to frames where errors are detected. The source retransmits these frames
# ARQs
Error control mechanisms are all referred to as **Automatic Repeat Request (ARQ)**
## Stop and Wait ARQ
### Basic Overview
- Source transmits a single frame and waits for acknowledgement (ACK) No other frames can be sent until the reply reaches the source
### Types of Errors Handled
#### Damaged Frame:
- Damaged frame arrives at the receiver
	- Receiver detects this and discards the frame
	- The transmitter has a timer that starts upon each transmission of a frame
	- If the timer runs out before an acknowledgement is received, the frame is retransmitted
#### Damaged Acknowledgement
- Consider the following situation
	- Station A sends a frame
	- Station B receives the frame correctly and sends an ACK
	- The ACK is damaged in transit and cannot be recognized by A, which will therefore timeout and send the same frame
	- Station B now has two copies of the same frame received as if they were separate
- To solve this problem:
	- Frames are alternately labeled 0 and 1, and positive acknowledgements are of the form ACK0 and ACK1
	- ACK0 acknowledges the receiver has received a frame labeled 1 and is ready to receive a frame labeled 0
	- If station B receives two successive frames labeled 0, it knows to discard the second one and resend ACK1
### Timing Diagram
![[Pasted image 20240804182352.png]]
## Go-Back-N ARQ
### Basic Overview
- The form of error control based on sliding-window flow control that is most commonly used is called Go-Back-N ARQ
- A station may send a series of sequentially numbered frames modulo some maximum value
- While no errors occur, the destination will acknowledge incoming frames as usual (RR= Receive Ready, or piggybacked acknowledgement)
- If the destination detects an error, it will send a negative acknowledgement (REJ) for that frame with the following rules. the destination will discard that frame and all future incoming frames until the frame in error is correctly received.
- The source station must then retransmit the frame received in error as well as all subsequent frames
### Types of Errors Handled
- Suppose that station A is sending frames to station B. After each transmission, A sets an ACK timer for the frame just transmitted. 
- Suppose B has successfully received frame $(i-1)$ and A has just transmitted frame $i$. The Go-Back-N technique can handle the following errors
- #### 1. Damaged Frame: 
	- If the received frame is invalid (damaged or lost), B discards the frame and takes no further action. There are two subcases
		- **a.** Within a reasonable period of time, A sends frame $(i+1)$.
			- B receives frame $(i+1)$ without ever receiving frame $i$ and sends REJ $i$
			- A must retransmit frame $i$ and all subsequent frames
		- **b.** A does not soon send additional frames. B receives nothing and returns neither an RR or an REJ
			- When A's timer expires, it transmits an RR frame that includes a bit known as the P bit, which is set to 1
			- B interprets the RR frame with a P bit of 1 as a command that must be acknowledged
			- This command must be acknowledged by sending an RR frame indicating the next frame it expects, which is frame $i$. A then retransmits frame $i$
			- Alternatively, A could just retransmit frame $i$ when the timer runs out
- #### 2. Damaged RR
	- There are two subcases:
	- **a.** B receives frame $i$ and sends RR $(i+1)$, which suffers an error in transit.
		- Because acknowledgements are cumulative, it may be that A will receive an RR for a subsequent frame that will arrive before the timer associated with frame $i$ expires
		- This means that when a subsequent frame is received by B, and its acknowledgement is sent to frame A, that acknowledgement will also acknowledge the correct receipt of frame $i$. No error is raised
	- **b.** If A's timer expires, it transmits an RR command with a P bit of 1, and starts another timer called the P-bit timer
		- If B fails to respond to the RR command, or its response suffers an error in transit, A's P-bit timer will expire
		- A will try again by issuing a new RR command and restarting the P-bit timer
		- After a set number of iterations, A will initiate the reset procedure from frame $i$ onwards. 
- #### 3. Damaged REJ
	- If an REJ is lost, it is equivalent to Case 1b
### Timing Diagram
![[Pasted image 20240804181528.png]]
## Selective-Reject ARQ
### Basic Overview
- In this scheme, the only retransmitted frames are those that received a negative acknowledgement, in this case called SREJ, or those that timed out.
### Efficiency
- Selective Reject may appear to be more efficient than Go-Back-N, due to the minimal amount of retransmission. However, the receiver must hold a buffer large enough to save post-SREJ frames until the frame in error is retransmitted.
	- Additionally, the receiver must contain logic for reinserting that frame into the proper sequence
- The transmitter, too, requires more complex logic to be able to send a frame out of sequence. 
- This increased complexity is why Selective-Reject is much less widely used. 
- It is a useful choice for a satellite link because it more effectively utilizes the channel. The drawbacks are worth it because satellite links have a very long propagation time
### Window Size Limitation
- For Go-Back-N, the size limitation is due to the following effect:
	- Say Station A sends frame 0 and gets back RR1
	- It then sends frames 1,2,3,4,5,6,7,0 (8 frames) and gets another RR1. This can mean one of two things:
		- All eight frames were received properly and the RR1 indicates the receiver is ready to receive the next frame labeled 1
		- All eight frames were damaged or lost in transit, and the receiver is repeating its previous RR1
	- This is avoided if the max window size is limited to 7 ($2^{3}-1$)
- Selective reject is more restrictive. Consider the following scenario with a 3 bit sequence number field
	- 1. Station A sends frames 0 through 6
	- 2. Station B receives all seven frames and cumulatively acknowledges with RR7
	- 3. Because of a noise burst, the RR7 is lost
	- 4. A times out and retransmits frame 0
	- 5. B has already advanced its receive window to accept frames 7,0,1,2,3,4,5. Thus it assumes frame 7 has been lost and that this is a new frame 0, which it accepts. 
- The problem is that there is an overlap between the sending and receiving windows. To overcome the problem, the max window size should be no more than half the range of sequence numbers.
	- Max window size is $2^{k-1}$

For class #data-comm