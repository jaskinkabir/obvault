Continues [[Local Area Networks (LANs)]]
# Traditional Ethernet
## Medium Access Control
### Random Access or Contention
- Random: no predictable or scheduled time for any station to transmit
- Contention: contend for time on the shared medium
- ALOHA, slotted ALOHA, CSMA, CSMA/CD
### ALOHA (university of Hawaii)
1. When station has frame, it sends
2. If ACK, fine. If not, retransmit
3. If no ACK after repeated transmissions, give up
4. For receiving station: if frame OK and address matches, send ACK
5. Frame may be damaged by noise or collision
	1. Collision region is twice the packet length. If packet length is L:
		1. Packets cannot be on the media Ls before transmission, because they will collide
		2. Packets cannot be on the media L after transmission start because collision
	2. No packets can be on the media during collision region
6. Max utilization of the channel: 18%
### Slotted Aloha
- Split time into uniform slots equal to frame time
- Transmission must begin at slot boundary
- Needs central clock or other sync mechanism
- Frames either miss or overlap totally
- Max utilization: 37%
	- Collision region is only the length of the packet before the current time
		- Any packets on the media before current time will transmit at the same time as current tx, because tx must happen at specific times
		- Any packets that must be transmitted during tx will wait until next time slot
	- Collision region is halved
![[Pasted image 20250911153529.png]]
- Each station requires 10bps to send data
- Pure aloha uses 18% of transmission line so max bandwidth is $56kbps * 0.18 = 10.08Kbps$
- Max number of stations = $\frac{10080 bps}{10bps}=1008$
### CSMA (Carrier Sense Multiple Access)
- Used today
- For LANs, propagation time is much less than transmission time (because stations are close)
	- This means it is easy to tell near instantaneously if the media is in use
	- This is why CSMA is good for LAN
- Station listens (carrier sense)
- If medium idle, station transmits
- If two stations start at the same instant, collision
- Wait for reasonable time, then station retransmits
	- 
- Max utilization depends on propagation time and frame length (80-90%)
	- Longer frames and shorter propagation gives better utilization
#### Types of CSMA
- When carrier senses media is busy:
##### Nonpersistent CSMA: 
- Waits random time and backs off, then repeats
- Capacity is wasted, many stations can be in their random back-off sleep time even when medium is clear
##### 1-Persistent CSMA: 
- Keep listening until medium is clear, then immediately transmit
- 1-persistent stations are selfish
- If two or more stations are waiting, collision is guaranteed
##### P-Persistent CSMA: Most complex
- If medium is idle, station **transmits with probability $p$**, otherwise delay one time slot with probability $1-p$
	-  Time slot typically max prop delay
- If medium busy, station listens until idle and repeats
- If collision, back off
- How to choose the value of $p$?
	- The expected number of stations attempting to transmit is the number of stations ready times p
		- Assume $n$ stations, then $np$
	- If $np>1$ on average, then collision
		- Retries compete with new transmissions
		- Continuous collisions, 0 throughput
	- So $np<1$ for expected peaks of $n$
		- If heavy load expected, lower p
		- However, as p decreases, stations wait longer
		- At low loads, this gives very long delays
##### CSMA/CD (Collision Detection)
- With CSMA, collision occupies medium for duration of transmission
- With CD, whenever collision is detected, stop transmission
- How to detect collision?
	- Collision produces much higher signal voltage
	- Collision detected if signal greater than a single station signal.
	- Signal attenuated over distance, so limit distance
- Sending stations listen while transmitting
	- If collision detected: transmit a jamming signal, then stop transmission
		- Very high voltage but no information
	- After jam, wait random time (backoff) then repeat
- Note that collision detection cannot be done wirelessly, because attenuation is much stronger
### Which Persistence Algorithm is Used?
- IEEE 802.3 (Ethernet) uses 1-persistent CSMA
	- Both nonpersistent and p-persistent have performance problems
- 1 persistent
	- Stations are greedy, and wasted time due to collisions is short
	- With random backoff, unlikely to collide on next tries
	- IEEE 802.3 uses binary exponential backoff
#### Binary Exponential Backoff (BEB)
- First, choose a random backoff delay within some given range
- First 10 attempts, mean value of random delay doubled
	- After experiencing the $c^{th}$ collision in a row, randomly select one of the next $2^{m}$ mini slots as the retransmission time $0,\,1,\,3,\,4,\,\dots,\,2^{m}-1$. Where $m=\text{min}(c,\,10)$
		- The idea is that as consecutive collisions occur, progressively decrease the chance that the stations choose the same delay by increasing the possible delay values
	- Size of the mini slot is round trip propagation delay. Wait 512-bit times according to standard
- This is very efficient
	- At low loads, 1-persistence guarantees usage of medium
	- At higher loads, the system is at least as stable as other techniques
- Drawback: Backoff algorithm gives last in, first out effect
	- Stations who experience fewer collisions transmit first
	- Makes it likely that the first station to try to transmit may not be able to transmit 
#### Collision Probability
- After $N$ stations have experienced $c$ collisions, the probability that there will be a collision can be found with these steps:
- First, select $m$ such that $m=min(c,\,10)$ 
- If $N>2^m$, $P(\text{collision})=1$
- Otherwise use the following formula $$P(\text{collision})=1-\Pi_{i=0}^{N-1} \frac{2^{m}-i}{2^{m}}$$
- How to derive this formula
	- $P(\text{collision})=1-\neg P(\text{collision})$
	- $\neg P(\text{collision})$ is the probability that each station chooses a different delay $k$
	- For this we can use the probability of choosing marbles without replacement formula
##### Example Problem
- In CSMA/CD, after 5th collision, what is the probability that a node chooses $k=4$? The result $k=4$ corresponds to a delay of how many seconds on a 10MBps Ethernet?
	- $n=5$, $K \in \{0,\,1,\,\dots,\,2^{5}-1\}$=32 possible delays
	- Thus the probability that $k=4$ = $\frac{1}{32}$
	- Delay time = $\frac{512 * 4}{10000}=\frac{512}{2500}=204\mu s$

# Ethernet Standard Notation
- \<data rate>\<signaling method>\<max segment length>
	- Data rate in mbps
	- Signaling method (protocol)
	- Max segment length in hundreds of meters
# Full Duplex Operation
- Traditional ethernet is half-duplex
- 100-Mbps ethernet in full-duplex mode has a theoretical transfer rate or throughput of 200Mbps
# Gigabit Ethernet
- Retains CSMA/CD and Ethernet Format
For class #data-comm 