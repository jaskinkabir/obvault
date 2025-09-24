Jaskin Kabir 801186717
Uses 
[[TCP-IP Protocol Architecture]]
[[Data Link Flow Control]]
[[Internet Checksum]]

1. Match the following functions to one of the five TCP/IP layers: [2+2+2+2=8]  
	1. Encoding of bits into appropriate signals such as voltage levels for transmission. [2]  
		1. **Physical**
	2. Making sure that the transmitted data frames do not overflow at the receiver’s buffer. [2]  x
		1. **Transport** (Data link)
	3. Determines the route for forwarding packets to the final destination. [2]  
		1. **Internet**
	4. Recovering from errors caused by a noisy channel. [2]
		1. **Data Link**
2. Consider a sliding window flow control scheme where frames are number modulo-8 and the window size is 7. [4+4=8]
	1. Which frames are in the transmitter’s window and buffer at the time when frames 0, 1, 2, 3 are transmitted and no RR has been received? [4]
		1. **The transmitter has buffered frames 0,1,2 and 3**
		2. **Its window contains frames 4,5,6**
	2. Following the above, now assume that the transmitter receives RR-3 and no other events have occurred. Which frames are currently in the transmitter’s window and buffer? [4]
		1. **The buffer contains frame 3**
		2. **The window contains 4,5,6,7,0,1,2** x (buffer + window = 7; 2 is not windowed)
/|0123456|70123456
send 0-3 (shrink window from left)
/0123|456|70123456
Receive RR3 (remove 012 from buffer)
012/3|4567012|3456

3. Using 4-bit checksum, find the checksum for sending 0111 0111. <u>Show all your steps.</u> [4]
	1. Add words together
		1. 0111 + 0111 = 1110
	2. Invert sum
		1. 0001
	3. **Checksum is 0001**
		1. Full frame is 0111 0111 0001
4. In the following synchronous time-division multiplexer, each TDMA frame consists of one bit taken from each input. [6+4=10]
	1. Sketch the output bit stream, clearly showing the frames and its contents. You should assume that the input is taken from the right hand side of each bit-stream. The output frame is also formed right-to-left. [6]
		1. **\[1xxx\]\[100x\]\[0101\]\[0110\]**
	2. What is the output bit rate? [4]
		1. Output bit rate must be $n$ times the input bit rate. Thus the output bit rate is **20 Kbps**
	3. ![[Pasted image 20250827170843.png]]
5. If the multiplexer in the above figure performs statistical multiplexing and the data rate of the output is maintained to be 20 Kbps, find the output bit stream. Ignore any addressing bits, and clearly describe how the output frame is being constructed. [5]
	1. For the first two time steps all inputs have data to send, so the frames are \[0110\] and \[1010]
	2. The next time step has 1 missing input, so it is buffered until a full frame can be formed
	3. The final time step fills this frame: \[0011\]
	4. The final bitstream, constructed from right to left:
		1. **\[1100\]\[0101\]\[0110\]**
6. What are the significant differences between datagram and virtual circuit operation? [5]
	1. Datagram operation is connectionless, so routing is done separately for each packet within the conversation. This means that, unlike virtual circuit operation, there are no setup or teardown phases and data transfer can begin immediately. Thus, datagram operation is typically faster than virtual circuit operation. However, datagram operation requires each packet be routed separately. This results in greater overhead, as each packet needs source and destination addresses in their headers. Additionally, virtual circuit operation is more reliable, because it sets up a route before any data is transferred. All packets will travel along this path in the correct order, and its resources like buffers and bandwidth can be reserved during the setup phase.

For class #data-comm/2homework