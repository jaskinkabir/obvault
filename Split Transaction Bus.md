Continues [[Caching]]
Continued by [[Chip Interconnection Networks]]

# Split-Transaction Bus
- Allows overlap among bus transactions
- Conceptually, think of two separate request and response buses
- Increases transaction latency, because response also requires arbitration
- But provides substantial gains in concurrency
	- Requests to different memory banks can be handled in parallel
	- A short request (eg BusUpgr) can be handled while a long request (BusRd from memory) is in progress
	- Allows multiple in-flight misses from a cache (lockup-free)
# Transient States
- Need to account for the concurrent bus actions in the state diagrams
- ![[Pasted image 20260223210150.png]]
- If, in the S state, there is a PrWr:
	- Move to transient S-M state
	- If a different processor's BusUpgr is serviced first, must now issue a BusRdX and invalidate current copy
- I-M state
# Conflicting Rqeuests
- In an atomic bus, conflicts can be detected when a request is launched
- In a split-transaction bus, there may be multiple pending requests
- SGI Challenge (90s) Solution
	- Maintain **request table** of all outstanding requests, replicated at each cache
	- New request cannot be launched if address found in request table
	- Also bounds # of outstanding requests–can only launch if space in the table
# How to Report Snoop Results?
- Snoop result must be reported by allacaches at the same time
- However, multiple inbound buffer entries can delay the snoop
- SGI Challenge Solution:
	- Snoop incoming request **before** putting it into the inbound buffer
	- Don't put a snoop request into the buffer and wait for it to pass through the FIFO. Respond to a snoop request when it appears on the bus
	- Actual response (eg flush) can come later
	- Assumes only one request for a given line is in progress at a time
# Associating Responses With Requests
- If both response and request require address, then either
	- Limits parallelism among request and response or
	- Requires address bits in both buses (expensive)
- Issue a unique ID (request number) to each request
- Use this ID to connect response to request
- In SGI, this can be the position in the global request table
# Dealing With Limited FIFO Buffers
- Each request must be acknowledged to indicate that all components have the necessary FIFO space for the request
- If not, a negative acknowledgement (NACK) forces the requester to try again later
- Responses?
	- By limiting the number of outstanding requests, we also limit the number of responses and guarantee their buffering resources

For class #parallel-arch