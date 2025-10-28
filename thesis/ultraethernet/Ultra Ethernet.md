# Intro
- UltraEthernet is an answer to limitations posed by InfiniBand and its sister protocol RDMA over Converged Ethernet (RoCE)
- RoCE v2 embedded InfiniBand's transport in a routable layer 3 Ethernet
	- Requires lossless transport with strict in-order packet delivery
	- These requirements impact performance
- The group that became the UEC wanted to converge datacenter and HPC networks into a single technology
# Foundational Tenets
## Massive Scalability
- Designed to support millions of endpoints in flexible arrangements with a **connectionless API**
- Focuses on fat tree deployments, but other optimized topologies have not been tested
	- HammingMesh
	- Dragonfly
	- Slim Fly
## High Performance
- The API is supported by a mechanism to establish p2p reliability context without additional latency
- The initial packet establishes context, even fore massive out-of-order delivery
## Compatibility
- Imposes minimal requirements on switch infrastructure to allow compatibility with existing ethernet deployments
- UE switches only support ECMP and basic ECN from source
- UE does not require changes in layer 1 or 2, but defines optimal extensions to improve layer 2 performance
- Fully ethernet compatible
## Vendor Differentiation
- The specification does not define how its requirements should be achieved or implemented
- Vendors can differentiate themselves in their unique implementations
# Scope
- Ultra Ethernet distinguishes 3 fundamental network types
	- Local (scale up)
	- Backend (scale out)
	- Frontend
	- ![[Pasted image 20251016192313.png]]
- Local (purple) network connects CPUs and accelerators
	- 10m range, sub microsecond latency targets
	- CXL, NVLINK, or Ethernet
	- Node/rack-scale
- Frontend (green) network carries internal and external traffic
- Backend (blue) network is a high performance network that connects compute devices
- Both backend and frontend networks are called scale-out networks and may be realized in a single physical instance
- UE supports both unified and separated implementations
- **UE 1.0 aims mainly at the backend network**
- Uses the following assumptions
	- UE is designed to operate at high bandwidths (400+Gbps)
	- Over medium length links (10-150m)
	- With large messages and packets
- Header size and processing latency are important but not a primary concern
- Cheap bandwidth and scalability are crucial
# Key Features
- Reccomends running UE traffic in its own traffic class, but its congestion control algorithm will likely work with other traffic, sharing switch buffers
- Uses Layer 3 IP compatible (routable) addressing and headers
- UE defines **Fabric Endpoints (FEPs)** as logical entities that terminate two ends of the transport layer
- A FEP is roughly equivalent to a NIC
- Key features include:
1. Connectionless transport protocol using ephemeral Packet Delivery Contexts (PDCs)
2. Removal of connection-oriented dependencies in the semantic layer. The NIC operates statelessly on the semantic (highest) level. Addressing, reliability, and ordering info are carried in the packet headers.
3. Native support for per-packet multipathing ("packet spraying") with flexible load balancing schemes without reordering overhead at the receiver
4. Both in-order and out-of-order reliable and unreliable packet delivery
5. Supports lossy (best effort) operation with optimal packet trimming and other fast loss detection schemes
6. A **novel congestion management scheme** that adapts to incast traffic and in-network congestion
7. Design enables vendors to deliver, hardware software or both
8. Integrated scalable end-to-end encryption and authentication
9. Link-layer optimizations
## ECMP Packet Spraying
- Equal-Cost-Multi-Pathing is a scheme for load balancing flows
- ECMP switches don't resolve a target address to a single port, but multiple ports with similar-cost paths to the destination
- A deterministic hash function $p=H(x)$ is then used to select the output port $p$ for each packet
- The input to the hash function usually includes the full IP five-tuple (source and destination addresses and ports, and protocol type)
- If used without change, ECMP routes all packets of the same flow along the same deterministic path
- UE redefines one of these input fields to the hashing function to contain an Entropy Value (EV)
	- For example. if UDP//IP is used, this field is the UDP source port, which is not used
- UE also supports a native IP-only mode
	- The EV is kept at the same position as the UDP source port
- The source FEP (NIC) can select a different EV for each packet that shall be sent on a different path. Or, it can select in-order delivery when sending packets with the same EV
- ![[Pasted image 20251016200725.png]]
	- Green dots are switches
	- Packets start going through switches upwards. Once the common ancestor switch is reached between source and destination, the packets start going downwards towards a unique path
	- In this network, there are exactly 4 equal-cost (three switch hops) paths between any two nodes in the same group, and 16 between nodes of different groups
	- Different values of EV lead to different paths being taken
- Due to its simplicity ECMP is limiting because a node cannot directly select a path. It only knows that two packets with the same EV are guaranteed to take the same path
- However, different EV values may share the same path due to collisions, which is expected
- If two paths conflict, the bandwidth for each path is halved
	- Especially serious if paths never change, like traditional ethernet, which leads to traffic polarization
- UE packet spraying avoids polarization by changing the EV for each packet, distributing packets evenly across all switches
- Even if hash collisions occur, they will be short, and the imbalance can be absorbed in the switch buffer
- Leads to full utilization and even traffic distribution in best case
- However, if some flows require in-order delivery they will occupy some paths deterministically
- UE proposes optional load balancing schemes to set EV for each packet
- **Finding the best such scheme remains open for vendor differentiation and research**
- 
- The NIC can handle retransmissions, reliability, and reductions

# Ultra Ethernet Profiles
- The specification offers three profiles
## AI Full and AI Base
- AI Full is a superset of the AI Base profile
- In contrast to HPC applications, AI applications do not benefit from point-to-point communication optimizations
- They are more focused on collective communication
	- Combining tensors (sum gradients across GPUs), sending parameters from one node to all, etc
	- The UE CCL offloads these collective communication routines to the NIC or network fabric
	- The NIC will perform reductions and handle synchronization
- Both full and base are aimed at Collective Communication Libraries (CCLs) that do not require wildcard tag matching or any other advanced communication operations
- Both offer deferrable sends
	- Specifically designed for CCL communication offload
	- This allows NICs flexibility to coordinate collective operations independently of the nodes/processes
- AI Full provides exact tag matching, whereas AI Base is designed for the simplest implementation complexity, assuming tag matching and other parts of the protocol are handled on a higher level
- AI Base does not support transport layer message matching
- AI Full provides exact matching without ordering
## HPC
- A superset of the AI Base profile
- Richest set of features including
	- In-order wildcard tag matching at the Transport layer
	- Optimized for MPI and OpenSHMEM workloads
		- See [[MPI]]
		- See [[SHMEM]]
- Also allows for deferable send
- By implementing deferable send, an implementation can provide both HPC and AI Full
- The libfabric definition over UE enables an endpoint to advertise multiple profiles and negotiate to the profile with the greatest common feature set

```tikz
```
```tikz
\begin{document}
\begin{tikzpicture}[
    every node/.style={draw, rounded corners=2pt, thick, fill=blue!10, text centered, minimum width=2.2cm, minimum height=0.8cm},
    level distance=2cm,
    sibling distance=4cm,
    edge from parent/.style={draw, thick, -latex}
]

% Tree
\node (base) {AI Base}
  child { node (hpc) {HPC} }
  child { node (ai) {AI Full} };


\end{tikzpicture}
\end{document}
```
# Ultra Ethernet Architecture
- ![[Pasted image 20251017153125.png]]
## The Protocol Stack
### PHY
- The physical layer is mostly unchanged by UE for compatibility with existing deployments
	- The first UE products will support 100G or 200G over lane signaling
### Data Link
- Also compatible with standard Ethernet
- Two optional and compatible UE extensions
	- Credit-Based Flow Control (CBFC)
	- Link Level Retry (LLR)
### Network
- Utilizes standard IPv4 or IPv6
- Allows legacy datacenter routing and operations
- Switches may implement packet trimming, an optional feature for the destination to detect dropped packets
### Transport Layer
- The most significant change
- Designed specifically for UE
- Designed to run over standard IP/UDP or natively over IP
- Can be broken into 4 sublayers
	- **Transport Security Sublayer (TSS)**
		- The TSS encrypts the PDS and SES (including the payload) and authenticates the IP addresses
			- Limits attacks that exploit spoofing the transport header field
		- Alongside the PDS, the TSS prevents replay attacks
		- TSS is integrated with the SES to reduce protocol layer attacks
	- **Congestion Management Sublayer (CMS)**
		- Works at the byte level
		- Controls the size of the outgoing window using Congestion Control Contexts (CCCs)
	- **Packet Delivery Sublayer (PDS)**
		- Works at the packet level
		- Associates one or more Packet Delivery Contexts (PDCs) with each CCC 
		- Manages reliable transmission of packets
		- Cooperates with SES 
	- **SEmantic Sublayer (SES)**
		- Manages message transactions implemented with packets
		- Directly links to the libfabric interface in the application layer
		- UE 1.0 uses libfabric as the interface to higher-level software and libraries like CCLs and MPI
		- Manages the execution of operations at the target, like committing RMAs into memory
## Transport Semantics Sublayer (SES)
- The libfabric interface utilizes the SES of the UE Transport (UET) layer to provide user-tagged tx/rx RMA operations
- SES defines a wire protocol and semantics that are heavily inspired by [[The Portals 4 Specification]]
- libfabric separates traditional networking semantics (addressing, completion, auth, failure handling) from the notion of a connection
- How this drives the definition of the transport layer is explored below
### Addressing
- UE uses IP addresses (Fabric Address, or FA) to select endpoints (FEPs)
- For scalable addressing, UE uses the following to address a logical context at each endpoint
	- JobIDs (24 bit)
	-  Process identifiers at the destination FEP (12 bit PIDonFEP)
	- Resource Index (12 bit RI)
- UE defines two addressing modes that differ in the interpretation of PIDonFEP
- The RI selects a RX context within the target process
	- A queue for TX/RX or matching buffers and completion queues for RMA
![[Pasted image 20251017161632.png]]
- The two supported addressing modes are distinguished by the *rel* bit in the packet header
	- **Relative Addressing** for distributed parallel jobs in a cluster
		- Each parallel job has a unique JobID
		- The Fabric Address identifies a FEP in the system
		- Each FEP has a global JobID table, which incoming packet is matched to
		- Each JobID table entry identifies one job that has processes on this node, and points to the local PIDonFEP table
		- The PIDonFEP able identifies all of JobID's processes (address spaces)
		- The table entry resolves to a resource index table per process, which has services or other process-local resources attached
		- In the figure, the address identifies the MPI endpoint in process 2313 on the node with FEP FA 1.1.1.2
		- The relative addressing scheme supports decoupling node-local and global addressing if all endpoints have the same # of processes.
		- With direct addressing, each process would have to store $N \times P$ (N is # nodes, P is # processes per node) address entries to know which address to send data to
		- With relative addressing, processes only need to know base addresses of nodes to compute the process id with an offset
	- **Absolute Addressing** for client-server applications to reach finxed network services
		- Ie storage or microservices
		- Such services are not part of jobs, so JobID is not used
			- Field can be used as auth token
	- In this mode, PIDonFEP can be used like a UDP port
	- UE supports merging PIDonFEP and Resource Index (RI) into a single table
#### RMA and RI Tables
- In general, TX/RX, tagged operations, and RMA operations use different RI tables
- RMA operations carry an additional memory key (in 64b match bits) used within RI context to identify a target buffer
- Memory key can be omitted in optimized header format if buffers can be directly associated with RIs
- Auth is ensured through the JobID, which needs to be assigned by a trusted entity
#### Scalability Enhancement From Addressing Scheme
- InfiniBand is a connection-oriented scheme and thus requires each sender and receiver pair to maintain a pair of TX/RX queues
	- For systems with many many nodes, this can balloon memory requirements
	- The solution is to have TX/RX queues shared by many processes
	- The problem is that this introduces bookkeeping overhead
- Since UE is connectionless, receive buffers only need to be allocated per process
- The JobID, PIDonFEP, RI tuple uniquely identifies a single queue at a FEP without any connection context
### Messaging and Matching
- At the receiver, each RI has an associated receive queue, and arriving messages match an entry in this queue
- If the message is unexpected (no entry)
	- The RX can discard the message and send a 'buffer not ready' response or buffer its headers
	- The RX may also buffer part of the payload until the receive buffer is posted
- Hardware message matching is supported through a packet-carried initiator ID (32b) as well as a matching key (64b)
- An MPI or CCL program would encode the source rank in the initiator ID
- The match key bits may be used to encode a communication context (ie an MPI communicator) and a message tag
- The HPC profile supports in-order wildcard matching
- The AI Full profile uses exact matching without ordering
	- To support hash-based or content addressable memory CAM implementations
#### Why Incorporate Matching?
- Matching is fundamental in HPC
- Useful for supporting CCL semantics
- By constraining AI Full to exact matching, and simplifying unexpected message semantics, the implementation can remain small
- Using tagged matching, messages can cross the network using an unordered protocol and yet arrive in the correct buffer
	- This is accomplished by having the upper layer place a sequence number into the match bits
	- If packet #2 arrives before packet #1, the match bits will place packet #2 in the memory address after packet #1's address
### Handling Large Unexpected Messages: Deferrable Send and Rendezvous
- Historically, short, unexpected messages were buffered at the RX until the receive was posted
- Large, unexpected messages require a different mechanism
- The three profiles have different ways of handling large unexpected messages
- A **Large Message** in UE is a message that exceeds the current send window size
	- The window size is often fixed for simplicity
	- Often defined by a parameter called the eager limit $s_{e}$
- A message is **Expected** at the RX if the receive address is known when the message arrives
	- The receive has been posted by the application
- It is called **Unexpected** otherwise
#### Rendezvous
- ![[Pasted image 20251017171605.png]]
- In traditional HPC Rendezvous protocol, small messages are sent in a single step and large messages are sent in two steps
	- First, TX sends a message of length $s_{e}$ alongside the local address of the remaining data
	- Then RX gets the remaining data through an RMA when it is ready
- The implementation may query the current window size $s_{e}$ before sending the first (rendezvous) send to adjust the send size
#### Deferrable Send
- ![[Pasted image 20251017171921.png]]
- An expected message is handled as a normal send
- The message is sent in full and copied into the RX buffer
- If the first packet of a large, unexpected message that cannot be buffered arrives, the RX tells the TX to defer (stop) sending until it is ready
- Large, unexpected messages allow for partial buffering of the packets (eg one window size) at the RX
- After the matching receive for a deferred message is posted at the receiver, a **Request To Resume (RTR)** message is sent to the TX
- To simplify implementation of this mechanism, each deferrable send contains an **Initiator Restart Token (IRT)** that identifies the message
- Each response from the RX carries how much data it has stored of this message and a **Target Restart Token (TRT)**
- This allows for simple, table-based matching on both sides
- Deferrable sends do not require RMA read support **except for in Full AI Profile**
	- This allows for efficient, low-resource, hardware-offloaded implementations

#### Receiver Initiated
- ![[Pasted image 20251017174139.png]]
- AI Base does not require support for Rendezvous or Deferrable Send
- Here, the RX initiates all communication
- The hardware can support only single packet send operations into specialized buffers and RMA write only
- Single packet send sends all information needed for RMA write of the whole payload to the TX
- The TX initiates RMA write from software
- The sender must have some asynchronous activity to initiate the write
#### Timing and Latency Analysis
- Assume that only headers are stored at the receiver
	- UE allows to store either
		- Nothing (requires sender to retransmit after timeout)
		- Headers only
		- Headers and partial payload of the original transaction (requires RX NIC to copy buffer to memory once receive is posted)
- Symbols:
	- $\alpha$: latency ($\frac{1}{2}$RTT)
	- $\beta$: Inverse bandwidth (time per bit)
	- $s:$ Message size
	- $t_{s}$: Time when send is posted
	- $t_{r}$: Time when receive is posted
- Expected vs unexpected
	- Expected ($t_{s} \geq t_{r}-\alpha$)
	- Unexpected ($t_{s} < t_{r} - \alpha)$
- Completion time table ![[Pasted image 20251017180606.png]]
	- Rendezvous and Deferrable Sends are seemingly identical in runtime
		- This is only true when the send window is constant and exact
	- Notes
		- 1: The send window is constant and exact, so the reader already knows the address and size of the remaining data. It does not have to wait for the first packet and can send the read request as the TX sends the rendezvous send
		- 2: Deferrable send can react to changes in send window and optimize the unexpected case
		- 3: Assumes $t_{s} = t_{r}-\alpha$
### RMA Read/Write
- UE uses single-packet reads, where the initiator issues a series of $\leq$ MTU read requests
- The target satisfies these read requests one by one, possibly out of order
- If the target does not need completions, only the initiator needs to maintain per-message state
- Initiator can rate-limit requests
- Many reads from many initiators can be interleaved at the target
#### Avoiding Deadlock
- UE supports lossy and lossless networks
- Lossy networks can avoid deadlock by dropping packets when buffers are full
- Lossless networks are susceptible to deadlock
- Deadlock occurs when dependencies prevent full buffers from being emptied
	- Message-dependent deadlock
		- Messages must be sent in order
		- A must be sent before B
		- Sender sends A but receiver's buffer is full and cannot receive B
		- Network is deadlocked
	- Protocol-dependent deadlock
		- A sends read request to B
		- B must send read response o A
		- B's tx buffer is full of requests that need ACKs from A
		- A cannot send ACKs because it is waiting for B's response
		- Network is deadlocked
- InfiniBand and RoCE solve deadlock by pre-allocating buffers for read responses. 
- This is wasteful
- UE avoids deadlock by using **Two Traffic Classes**
	- Bulk data 
	- Control traffic
- Eliminates both kinds of deadlock
	- Reads and read responses are two different TCs
## Transport Packet Delivery Subsystem (PDS)
- The PDS uses ephemeral **Packet Delivery Contexts (PDCs)** to manage reliable transmission
- UE prohibits fragmentation i the network
- Sends all but the last packet with full MTU payloads
	- Simplifies packet tracking
- PDS defines three packet types
	- **Request Packets**: Send data
	- **ACK Packets**: Carry info about previous request packets
	- **Control Packets:** Used for transport-specific controls
		- Checking status of a packet at RX
	- Check state of a path
### Packet Transport Modes
#### Reliable Unordered Delivery
- Default bulk transfer mode
- Should be used for any large-message transmission
- Should be used for any transmissions if no wildcard matching is required (AI profiles)
- Matching and ordering can be done at the RX through the match bits within the address
- Ordered delivery can be ensured irrespective of packet ordering on the wire
- RUD is considered the most efficient reliable transport mode because it enables packet spraying
#### Reliable Ordered Delivery
- Used if strict in-order guarantees are required at the packet level
- Needed for wildcard matching with in-order guarantees as required by MPI
- A simple protocol could send eager portions of rendezvous messages over ROD, and the read portions over a RUD channel
- ROD may be needed to communicate with minimally resourced endpoints
- Only requires implementing the go-back-N scheme
- ROD uses only a single network path per flowley
- Considered the much less efficient reliable protocol
#### Unreliable Unordered Delivery
- Useful for software-based protocol implementations or system management tasks
- Fastest mode
#### Reliable Unordered Delivery for Idempotent Operations
- Only available in HPC profile
- Allows implementors to omit filtering duplicate packets/messages
- Most scalable option, no receiver state is necessary
- Tricky to use
- Does not apply to nonidempotent operations like atomic addition
- All unordered packet transport modes may lead to out-of-order data in main memory
- SES does not reorder packets
### Dynamic PD Creation
- ![[Pasted image 20251018164149.png]]
- This seems weird. Shouldn't the last pkt y and n be switched? Is this a mistake?
- Packet Delivery Contexts can be created without latency because states necessary to establish connection are carried within the headers
- **Packet Sequence Numbers (PSNs)** identify packets and **PDC IDs** identify PDCs at source or dest
- State machine exclludes much of error/packet drop handling during init
- Consider the scenario on the right
- The initiator starts a 5 packet write in the SYN state
- Once it receives the first ACK it moves into the ESTABLISHED state
- Once the target receives the first packet without the SYN state it moves to the ESTABLISHED state
- Note that the TX sends at full rate during PDC establishment
- The initiator always starts a PDC close when the PDC is idle
	- Not required to immediately close an idle PDC
- Target can request that the initiator close a PDC using control pkt or flags in ACK
- Once source begins closing PDC, it enters QUIESCE state
- Continues to send pkts for messages that started before the close, but refuses new messages
- Once all messages have been sent, enter ACK WAIT until all replies have been received
- Then send final close command, which closes PDC
- Once final ACK for close command has been received, source PDC is freed
### Fast Packet Loss Detection
- Packet loss detection is typically done through timeouts
- Timeouts are inefficient and unreliable
	- A packet may timeout at the source while it is still waiting in a switch buffer
	- Causes unneeded retransmission
- UE defines 3 kinds of packet drops **3 Cs in Networking**
	- **Congestion Drops**: Packets are dropped when switch buffers are full
	- **Corruption Drops:** Packets with bit errors fail the checksum
	- **Configuration Drops:** Network is configured to drop packets (firewalls or TTL limits)
- UE describes 3 optional loss detection mechanisms for Congestion Drops
- Only one for Corruption Drops
#### Packet Trimming
- Simplest scheme
- Requires switch support
- If a switch detects that a packet will be dropped, it will trim the payload and only forward the header
- Upon receiving a trimmed packet, the destination will know the payload was dropped and request a retransmission
- Trimming cannot detect corruption drops
#### Out-Of-Order Count
- Estimates number of packets lost by calculating distance between the last received PSN and the earliest missing PSN
- Can be estimated by dest and sent via optional OOO_COUNT_ACK ext header
- Can be estimated at source
- If the counter exceeds threshold, system can assume packet loss
- More accurate than timeouts, but may send duplicate packets if sprayed packets have different latencies
#### Entropy Value (EV)-Based Schemes
- Very precise
- Each EV maps to a unique path
- Keep an ordered list of (EV, PSN) pairs
- ACKs carry same EV as ack'd packet
- Consider this example

| EV  | PSN | ACK |
| :-- | :-- | :-- |
| 0   | 0   | Y   |
| 0   | 1   | Y   |
| 0   | 2   |     |
| 0   | 3   | Y   |
- PSN 3 has been ACK'd before PSN 2
- Since 1,2,3 are on same EV, they must be on the wire in the same order
- 3 is ACK'd before 2 means 2 must have been dropped
- 

For topic #thesis/ultraethernet



- wrap IP packet in ethernet packet
- Wrap UET packet in IP packet
- Create figure showing where UET fits in the full frame
- Contrast with RDP
- 