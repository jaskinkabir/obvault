[[TCP]]
# Overview
- Timeout caused by packet loss
	- Noise on tx line
	- Packet discarded at a congested router
	- Most timeout on the Internet is due to congestion
- 
# Window Management
##  TX maintains two windows
- Receiver window (rwnd)
	- TCP Header WIN field
	- No buffer overflow at RX
	- This is the max number of packets the RX can handle
- Congestion window (cwnd)
	- Dynamic window size
	- Max number of packets TX can handle
- Allowed segments to be sent out: 
	- MIN\[rwnd,cwnd\]
- Treat ICMP Source quench as timeout
### Slow Start (Exponential Increase)
- Start connection with cwnd=1
- Double cwnd at each ACK, until ssthresh
### Congestion Avoidance (Linear Increase)
- For cwnd >= sstrhesh, increase cwnd by 1 for each ACK
- When timeout occurs
	- Set slow start threshold to half current congestion window
		- ssthresh = cwnd/2
	- Set cwnd = 1 and restart from slow start phase
![[Pasted image 20251104151703.png]]
# ReTX Timer Management
- TCP Estimates round trip delay by observing pattern of delay
- Set retx timer to a value greater than the estimate
### Round Trip Time (RTT) Estimation
- Simple average
- Exponential average: greater weight given to more recent measurements
- Retransmission timeout (RTO) is a function of average and variance of RTT
### Exponential RTO Backoff
- RTO increased each time a segment is retransmitted
- $\text{RTO}=q\times \text{RTO}$
- Commonly, q=2 (binary exponential backoff)
## Karn's Algorithm
- If a segment is re-transmitted, the ACK arriving may be
	- For the first copy of the segment: RTT longer than expected
	- For the second copy
- No way to tell which one
- Do not update RTT for re-transmitted segments
- Use the backoff RTO until segments get through the first time
	- ACK arrives for segment that has not been retx'd
# Fast Retransmit
- Duplicate ACKs (dupacks) may be generated due to
	- Packet loss
	- Out-Of-Order packet delivery
- TCP sender assumes that packet loss has occurred if it receives 3 dupacks consecutively
- ![[Pasted image 20251104153027.png]]
	- If 8 has not been received, the receipt of packets 9, 10, and 11 will generate acks that request packet 8
- Fast retransmit retx's packets immediately, without waiting for RTo
- Occurs when multiple (>=3) dupacks come back
- Fast recovery follows fast retransmit
	- ssthresh = min(cwnd, rwnd)/2
	- Retransmit the missing segment
	- Enter congestion avoidance
		- cwnd=ssthresh (do not slow start at cwnd=1, too conservative)
- 

For class #data-comm