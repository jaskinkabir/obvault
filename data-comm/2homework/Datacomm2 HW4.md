Jaskin Kabir 801186717
1. In a network that has a maximum packet size of 128 bytes, a maximum packet life-time of 30 seconds, and an 8-bit packet sequence number, what is the maximum data rate (in unit bps) per connection? (Hint: a sender may not send more than $2^8$ = 256 packets at one time) [5]
	1. $\frac{128\text{ Bytes}}{\text{Packet}} \times \frac{256\text{ Packets}}{\text{Connection}} \times \frac{1\text{ Connection}}{30 \text{ Seconds}}= \frac{1092\text{ Bytes}}{\text{Second}} = 8736\text{ bps}$
2. Suppose Host A sends out 1500-byte TCP payloads with a 120-sec maximum packet lifetime. What is the maximum data rate (in unit bps) on the connection without having the sequence numbers wrap around? Take TCP, IP, and Ethernet overhead into consideration. Assume that Ethernet frames may be sent continuously. (Hint: The TCP overhead is 20 bytes. The IP overhead is 20 bytes. The Ethernet overhead is 26 bytes. The TCP sequence number is 32-bit long). [10]
	1. Packet length
		1. $1500 + 20 + 20 + 26 = 1566 \text{ Bytes}$
	2. $\frac{2^{32}\text{ Bytes}}{Connection} \times \frac{1\text{ Connection}}{120\text{ Seconds}} \times \frac{1566\text{ Wire Bytes}}{1500 \text{ Payload Bytes}} = 299 \text{Mbps}$
3. A TCP entity opens a connection and uses slow start. Approximately how many round-trip times are required before TCP can send N segments? [10]

| **RTT** | **CWND** | **Segments Sent** |
| ------- | -------- | ----------------- |
| 0       | 1        | 0                 |
| 1       | 2        | 1                 |
| 2       | 4        | 3                 |
| 3       | 8        | 7                 |
| $T$     | $2^T$    | $2^T-1$           |
After $T$ round-trip times, $2^{T}-1$ segments have been sent
To send $N$ segments, $N \leq 2^T-1$
$N+1 \leq 2^{T}$
$T \geq \log_{2}(N+1)$
**$\lceil \log_{2}(N+1)\rceil$ are required**
1. Suppose that the TCP congestion window is set to 18 KB and a timeout occurs. If the next four transmission bursts are all successful, how big will the window be when the fifth transmission is sent out? Assume that the maximum segment size is 1KB. [5]
	1. $\text{SSTHRESH}=9\text{ KB}$
	2. **On 5th transmission, window size = 9 KB**

| **Burst** | **CWND** |
| :-------- | :------- |
| 1         | 1        |
| 2         | 2        |
| 3         | 4        |
| 4         | 8        |
| 5         | 9        |

